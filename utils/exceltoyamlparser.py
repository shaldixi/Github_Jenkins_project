import pandas as pd
import os
from ruamel.yaml import YAML, ruamel
import re
cwd = os.getcwd()

def processciqsheet(ciqpath, values_yaml):
    ciq = pd.read_excel(ciqpath, sheet_name=None, dtype=str)
    provisioning_df = ciq["Provisioning"].dropna(axis='index', how='all').iloc[1:, 1:3]
    provisioning_order = provisioning_df[provisioning_df['Unnamed: 2'] == "CREATE"]['Unnamed: 1']
    provisioning_sheets = provisioning_order.tolist()
    #config_map_yaml = cwd + "/Output/config_map.yaml"
    if not os.path.exists(values_yaml):
        open(values_yaml, 'w').close()
    final_dic = dict()
    for sheetname in provisioning_sheets:
        current_sheet_data = pd.read_excel(ciqpath, sheet_name=sheetname, index_col=None, header=None)
        print(current_sheet_data)
        maxcolumnlen = current_sheet_data.columns.size
        current_sheet_dic_list = []
        for rowNo in range(len(current_sheet_data)):
            if rowNo >1:
                current_sheet_row_dic = dict()
                for columnNo in range(maxcolumnlen):
                    print(current_sheet_data.iloc[rowNo, columnNo])
                    headerName = current_sheet_data.iloc[1, columnNo]
                    headerName = "_".join(headerName.split(' '))
                    headerName = "_".join(headerName.split('-'))
                    headerName = re.sub("\(.*?\)|\[.*?\]","",headerName)
                    headerName = "".join(("parameter_", headerName)) if headerName[:1].isdigit() else headerName
                    current_sheet_row_dic[headerName] = current_sheet_data.iloc[rowNo, columnNo] if not pd.isnull(current_sheet_data.iloc[rowNo, columnNo]) else ''
                current_sheet_dic_list.append(current_sheet_row_dic)
        sheetname = "_".join(sheetname.split('-'))
        final_dic[sheetname] = current_sheet_dic_list
    yaml = YAML()
    yaml.indent(mapping=4, sequence=6, offset=3)
    yaml.default_flow_style = False
    with open(values_yaml, 'a') as yaml_file:
        yaml.dump(final_dic, yaml_file)
    return values_yaml