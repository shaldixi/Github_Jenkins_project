import os
from zipfile import ZipFile
from utils import valuesyamlgen

cwd = os.getcwd()
node_type = "CMG"
zipObj = ZipFile('Output/TBT_Out_values_yaml.zip', 'w')

ciqsheetpath = 'Input/excel_input.xlsx'
eligible_sheet_names, alias_sheet_names = valuesyamlgen.process(ciqsheetpath)
if len(eligible_sheet_names) > 0:
    for sheet_name in eligible_sheet_names:
        alias = alias_sheet_names[sheet_name]
        zipObj.write('Output/' + alias + ".yaml")
try:
    if node_type == "CMG":
        version = "21.8"
        release = "R1"
        helmchart = os.listdir(cwd + "/repo/" + node_type + "/" + str(version) + "/" + release + "/")
        zipObj.write("repo/" + node_type + "/" + str(version) + "/" + release + "/" + helmchart[0])
except Exception as ex:
    print(str(ex))
zipObj.close()
yamlPath = cwd + "TBT_Out_values_yaml.zip"
