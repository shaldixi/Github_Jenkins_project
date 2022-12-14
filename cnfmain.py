import json
import os
import zipfile
from utils import valuesyamlgen
import shutil
from utils import exceltoyamlparser
from utils import configmap

cwd = os.getcwd()
ciqsheetpath = 'Input/excel_input.xlsx'
pacinputsheetpath = 'Input/PAC_LLD.xlsx'
json_path = "Input/input.json"
with open(json_path, 'r') as f:
    data = json.loads(f.read())
    # print(data)

node_type = data["Node_Type"]
version = data["Version"]
release = data["Release"]


def generateHelmChart():
    try:
        helmchart = os.listdir(cwd + "/repo/" + node_type + "/" + str(version) + "/" + release + "/")
        output_path = "repo/" + node_type + "/" + str(version) + "/" + release + "/" + helmchart[0]
        folder_name = helmchart[0].replace(".zip", "")
        zip_folder = "Output/helm_chart/" + folder_name
        with zipfile.ZipFile(output_path, "r") as zip_ref:
            zip_ref.extractall(zip_folder)
        deployment_values_yaml = valuesyamlgen.process(ciqsheetpath, folder_name + "/cmg/")
        if pacinputsheetpath:
            exceltoyamlparser.processciqsheet(pacinputsheetpath, deployment_values_yaml)
        configmap.readAllTemplates(cwd + "/Output/helm_chart/" + folder_name + "/cmg/templates/"+"Dut_ConfigMap.yaml")
        shutil.make_archive("Output/" + folder_name, 'zip', zip_folder)
    except Exception as ex:
        print(str(ex))


generateHelmChart()
