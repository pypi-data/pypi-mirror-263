import os
import logging
import pandas as pd
from typing import Dict
import concurrent.futures
import ast

from scarcc.sim_engine.output import MethodDataFiller
from .simulation_workflow import get_simulation_output, unpack_future_result_per_key, concat_result

logger = logging.getLogger(__name__)

def convert_checker_alpha_table_to_dict(checker_alpha_table: pd.DataFrame): # alpha table keys as append ''.join(['_'+ str(ele) for ele in _i_j as suffix 
    d= dict()
    for lv_pairs in checker_alpha_table.lv_pairs.unique():
        d['_'+'.'.join([str(ele) for ele in ast.literal_eval(lv_pairs)])] = checker_alpha_table.query('lv_pairs == @lv_pairs')
    return d

def replace_i_to_suffix(colname: str, sub_alpha_dict: Dict[str, pd.DataFrame]):
    i = colname.split('_')[-1]
    print(i, sub_alpha_dict[i])
    return colname.replace(i, sub_alpha_dict[i]['suffix'])

# TODO: import from SG data that already ran/ BUT IF result has only levels are recorded
# handle only one checkerboard consist of 2 target genes
def run_checkerboard_workflow(alpha_table: pd.DataFrame, data_directory: str,  max_cpus=12,**kwargs):
    def added_Normal_cols(biomass_df):
        def rename_to_Normal(colname):
            splitted = colname.split('_')
            splitted[1] = 'Normal'
            splitted[-1] = '0.0'
            return '_'.join(splitted)
        Normal_df = biomass_df[[col for col in biomass_df.columns if col.endswith('_0.0')]].copy()
        Normal_df.columns = Normal_df.columns.map(rename_to_Normal)
        return pd.concat([Normal_df, biomass_df], axis=1)

    method = 'checkerboard'
    available_cpus = min(os.cpu_count(), max_cpus)
    task_dict = {}
    current_gene = list(alpha_table.index.unique())
    if len(current_gene) > 2:
        raise ValueError('Table contains more than 2 genes, please filter the appropriate gene rows')

    sub_alpha_dict = convert_checker_alpha_table_to_dict(alpha_table)
    SG_lv_alpha_dict = {k: v for k, v in sub_alpha_dict.items() if '0' in k}
    DG_lv_alpha_dict = {k: v for k, v in sub_alpha_dict.items() if '0' not in k}
    with concurrent.futures.ProcessPoolExecutor(max_workers=available_cpus) as executor:
        for XG, lv_alpha_dict in zip(['SG', 'DG'], [SG_lv_alpha_dict, DG_lv_alpha_dict]):
            task_dict[method, XG] = [
                executor.submit(
                    get_simulation_output,
                    current_gene=current_gene,
                    alpha_table=single_lv_alpha_table,
                    checker_suffix=checker_suffix,
                    **kwargs
                )
                for checker_suffix, single_lv_alpha_table in lv_alpha_dict.items() # each level is with key as '_lv1.lv2' and value as alpha_table at that lv_pair
            ]

    df_container = {key: [future.result() for future in future_list] for key, future_list in task_dict.items()}
    df_container = {key: unpack_future_result_per_key(result_list) for key, result_list in df_container.items()} # list of [biomass, flux] into {biomass : biomass_list, flux : flux_list}
    df_container = {k: concat_result(sub_container) for k, sub_container in df_container.items()} # column-wise for biomass, row-wise for flux data frame concatenation
    df_container[method, 'SG']['biomass'] = added_Normal_cols(df_container[method, 'SG']['biomass'])
    
    mdf = MethodDataFiller(df_container, data_directory)
    mdf.fill_container()
    mdf.write_to_csv()
    return df_container