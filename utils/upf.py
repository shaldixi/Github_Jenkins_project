def updateDictionary(request_param, valuesFileData, selectedVersion):
    if selectedVersion == "12.0R8":
        if request_param.form["upf_input_type"] == "values_ncsBmDpdk":
            update12R8ServicesDictionary(request_param, valuesFileData)
            update12R8NascDictionary(request_param, valuesFileData)
            update12R8LoggingAndMultusDictionary(request_param, valuesFileData)
            update12R8ResourcesDictionary(request_param, valuesFileData)
            update12R8StorageDictionary(request_param, valuesFileData)
            update12R8PeersDictionary(request_param, valuesFileData)
            update12R8NetworkAndVPRNDictionary(request_param, valuesFileData)
        else:
            update12R8ServicesDishDictionary(request_param, valuesFileData)
            update12R8NascDishDictionary(request_param, valuesFileData)
            update12R8LoggingAndMultusDishDictionary(request_param, valuesFileData)
            update12R8ResourcesDishDictionary(request_param, valuesFileData)
            update12R8StorageDishDictionary(request_param, valuesFileData)
            # update12R8PeersDishDictionary(request_param, valuesFileData)
            # update12R8NetworkAndVPRNDishDictionary(request_param, valuesFileData)
    return valuesFileData


def update12R8ServicesDictionary(request_param, valuesFileData):
    valuesFileData["service"]["loamA"]["console"]["nodePort"] = int(request_param.form.get("loamAnodePort"))
    valuesFileData["service"]["loamA"]["console"]["port"] = int(request_param.form.get("loamAport"))
    valuesFileData["service"]["loamA"]["console"]["targetPort"] = int(request_param.form.get("loamAtargetPort"))

    valuesFileData["service"]["loamB"]["console"]["nodePort"] = int(request_param.form.get("loamBnodePort"))
    valuesFileData["service"]["loamB"]["console"]["port"] = int(request_param.form.get("loamBport"))
    valuesFileData["service"]["loamB"]["console"]["targetPort"] = int(request_param.form.get("loamBtargetPort"))

    valuesFileData["service"]["lmg"]["console"]["nodePort"] = int(request_param.form.get("lmgnodePort"))
    valuesFileData["service"]["lmg"]["console"]["port"] = int(request_param.form.get("lmgport"))
    valuesFileData["service"]["lmg"]["console"]["targetPort"] = int(request_param.form.get("lmgtargetPort"))

    valuesFileData["service"]["llb"]["console"]["nodePort"] = int(request_param.form.get("llbnodePort"))
    valuesFileData["service"]["llb"]["console"]["port"] = int(request_param.form.get("llbport"))
    valuesFileData["service"]["llb"]["console"]["targetPort"] = int(request_param.form.get("llbtargetPort"))

    valuesFileData["image"]["repository"] = request_param.form.get("repository")
    valuesFileData["image"]["name"] = request_param.form.get("name")
    valuesFileData["image"]["tag"] = request_param.form.get("tag")
    valuesFileData["image"]["pullPolicy"] = request_param.form.get("pullPolicy")
    return valuesFileData


def update12R8ServicesDishDictionary(request_param, valuesFileData):
    valuesFileData["service"]["loamA"]["console"]["nodePort"] = int(request_param.form.get("loamAnodePort"))
    valuesFileData["service"]["loamA"]["console"]["port"] = int(request_param.form.get("loamAport"))
    valuesFileData["service"]["loamA"]["console"]["targetPort"] = int(request_param.form.get("loamAtargetPort"))

    valuesFileData["service"]["loamB"]["console"]["nodePort"] = int(request_param.form.get("loamBnodePort"))
    valuesFileData["service"]["loamB"]["console"]["port"] = int(request_param.form.get("loamBport"))
    valuesFileData["service"]["loamB"]["console"]["targetPort"] = int(request_param.form.get("loamBtargetPort"))

    valuesFileData["service"]["lmg"]["console"]["nodePort"] = int(request_param.form.get("lmgnodePort"))
    valuesFileData["service"]["lmg"]["console"]["port"] = int(request_param.form.get("lmgport"))
    valuesFileData["service"]["lmg"]["console"]["targetPort"] = int(request_param.form.get("lmgtargetPort"))

    valuesFileData["service"]["llb"]["console"]["nodePort"] = int(request_param.form.get("llbnodePort"))
    valuesFileData["service"]["llb"]["console"]["port"] = int(request_param.form.get("llbport"))
    valuesFileData["service"]["llb"]["console"]["targetPort"] = int(request_param.form.get("llbtargetPort"))

    valuesFileData["image"]["repository"] = request_param.form.get("repository")
    valuesFileData["image"]["name"] = request_param.form.get("name")
    valuesFileData["image"]["tag"] = request_param.form.get("tag")
    valuesFileData["image"]["pullPolicy"] = request_param.form.get("pullPolicy")
    return valuesFileData


def update12R8NascDictionary(request_param, valuesFileData):
    valuesFileData.insert(2, "nodeSelector", createNodSelectorDictionary())
    valuesFileData["nodeSelector"]["loamA"][0]["key"] = request_param.form.get("loamAKey")
    valuesFileData["nodeSelector"]["loamA"][0]["value"] = request_param.form.get("loamAValue")
    valuesFileData["nodeSelector"]["loamB"][0]["key"] = request_param.form.get("loamBKey")
    valuesFileData["nodeSelector"]["loamB"][0]["value"] = request_param.form.get("loamBValue")
    valuesFileData["nodeSelector"]["llb"][0]["key"] = request_param.form.get("llbKey")
    valuesFileData["nodeSelector"]["llb"][0]["value"] = request_param.form.get("llbValue")
    valuesFileData["nodeSelector"]["lmg"][0]["key"] = request_param.form.get("lmgKey")
    valuesFileData["nodeSelector"]["lmg"][0]["value"] = request_param.form.get("lmgValue")
    valuesFileData["nasc"]["enable"] = convertBooleanStringToInt(request_param.form.get("nascEnable"))
    valuesFileData["nasc"]["imageRepository"] = request_param.form.get("imageRepository")
    valuesFileData["nasc"]["imageName"] = request_param.form.get("imageName")
    valuesFileData["nasc"]["imageTag"] = request_param.form.get("imageTag")
    valuesFileData["nasc"]["imagePullPolicy"] = request_param.form.get("imagePullPolicy")
    return valuesFileData


def update12R8NascDishDictionary(request_param, valuesFileData):
    # valuesFileData.insert(2, "nodeSelector", createNodSelectorDictionary())
    # valuesFileData["nodeSelector"]["loamA"][0]["key"] = request_param.form.get("loamAKey")
    # valuesFileData["nodeSelector"]["loamA"][0]["value"] = request_param.form.get("loamAValue")
    # valuesFileData["nodeSelector"]["loamB"][0]["key"] = request_param.form.get("loamBKey")
    # valuesFileData["nodeSelector"]["loamB"][0]["value"] = request_param.form.get("loamBValue")
    # valuesFileData["nodeSelector"]["llb"][0]["key"] = request_param.form.get("llbKey")
    # valuesFileData["nodeSelector"]["llb"][0]["value"] = request_param.form.get("llbValue")
    # valuesFileData["nodeSelector"]["lmg"][0]["key"] = request_param.form.get("lmgKey")
    # valuesFileData["nodeSelector"]["lmg"][0]["value"] = request_param.form.get("lmgValue")
    valuesFileData["nasc"]["enable"] = convertBooleanStringToInt(request_param.form.get("nascEnable"))
    valuesFileData["nasc"]["imageRepository"] = request_param.form.get("imageRepository")
    valuesFileData["nasc"]["imageName"] = request_param.form.get("imageName")
    valuesFileData["nasc"]["imageTag"] = request_param.form.get("imageTag")
    valuesFileData["nasc"]["imagePullPolicy"] = request_param.form.get("imagePullPolicy")
    valuesFileData["nasc"]["configReadInterval"] = int(request_param.form.get("configReadInterval"))
    valuesFileData["nasc"]["scrapeInterval"]["loam"]["kciInfo"][0]["name"] = request_param.form.get("loamname")
    valuesFileData["nasc"]["scrapeInterval"]["loam"]["kciInfo"][0]["interval"] = int(
        request_param.form.get("loaminterval"))
    valuesFileData["nasc"]["scrapeInterval"]["loam"]["kciInfo"][1]["name"] = request_param.form.get("loamname2")
    valuesFileData["nasc"]["scrapeInterval"]["loam"]["kciInfo"][1]["interval"] = int(
        request_param.form.get("loaminterval2"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kciInfo"][0]["name"] = request_param.form.get("lmgname")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kciInfo"][0]["interval"] = int(
        request_param.form.get("lmginterval"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kciInfo"][1]["name"] = request_param.form.get("lmgname2")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kciInfo"][1]["interval"] = int(
        request_param.form.get("lmginterval2"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kciInfo"][2]["name"] = request_param.form.get("lmgname3")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kciInfo"][2]["interval"] = int(
        request_param.form.get("lmginterval3"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kciInfo"][3]["name"] = request_param.form.get("lmgname4")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kciInfo"][3]["interval"] = int(
        request_param.form.get("lmginterval4"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][0]["name"] = request_param.form.get("lmgkpiInfoname")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][0]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][1]["name"] = request_param.form.get("lmgkpiInfoname2")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][1]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval2"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][2]["name"] = request_param.form.get("lmgkpiInfoname3")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][2]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval3"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][3]["name"] = request_param.form.get("lmgkpiInfoname4")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][3]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval4"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][4]["name"] = request_param.form.get("lmgkpiInfoname5")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][4]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval5"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][5]["name"] = request_param.form.get("lmgkpiInfoname6")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][5]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval6"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][6]["name"] = request_param.form.get("lmgkpiInfoname7")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][6]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval7"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][7]["name"] = request_param.form.get("lmgkpiInfoname8")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][7]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval8"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][8]["name"] = request_param.form.get("lmgkpiInfoname9")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][8]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval9"))
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][9]["name"] = request_param.form.get("lmgkpiInfoname10")
    valuesFileData["nasc"]["scrapeInterval"]["lmg"]["kpiInfo"][9]["interval"] = int(
        request_param.form.get("lmgkpiInfointerval10"))
    return valuesFileData


def update12R8LoggingAndMultusDictionary(request_param, valuesFileData):
    update12R8LoggingDictionary(request_param, valuesFileData)
    update12R8MultusDictionary(request_param, valuesFileData)


def update12R8LoggingAndMultusDishDictionary(request_param, valuesFileData):
    update12R8LoggingDishDictionary(request_param, valuesFileData)
    update12R8MultusDishDictionary(request_param, valuesFileData)


def update12R8LoggingDictionary(request_param, valuesFileData):
    valuesFileData["logging"]["enable"] = convertBooleanStringToInt(request_param.form.get("logEnable"))
    valuesFileData["logging"]["imageRepository"] = request_param.form.get("logimageRepository")
    valuesFileData["logging"]["imageName"] = request_param.form.get("logimageName")
    valuesFileData["logging"]["imageTag"] = request_param.form.get("logimageTag")
    valuesFileData["logging"]["imagePullPolicy"] = request_param.form.get("logimagePullPolicy")
    return valuesFileData


def update12R8LoggingDishDictionary(request_param, valuesFileData):
    valuesFileData["logging"]["enable"] = convertBooleanStringToInt(request_param.form.get("logEnable"))
    valuesFileData["logging"]["imageRepository"] = request_param.form.get("logimageRepository")
    valuesFileData["logging"]["imageName"] = request_param.form.get("logimageName")
    valuesFileData["logging"]["imageTag"] = request_param.form.get("logimageTag")
    valuesFileData["logging"]["imagePullPolicy"] = request_param.form.get("logimagePullPolicy")
    return valuesFileData


def update12R8MultusDictionary(request_param, valuesFileData):
    valuesFileData["multus"]["loam"]["ip"]["loamA"] = request_param.form.get("loamAIp")
    valuesFileData["multus"]["loam"]["ip"]["loamB"] = request_param.form.get("loamBIp")
    valuesFileData["multus"]["loam"]["ip"]["active"] = request_param.form.get("activeIp")
    valuesFileData["multus"]["loam"]["ip"]["standby"] = request_param.form.get("standbyIp")
    valuesFileData["multus"]["loam"]["netMask"] = int(request_param.form.get("loamnetMask"))
    valuesFileData["multus"]["loam"]["subnet"] = request_param.form.get("loamsubnet")
    valuesFileData["multus"]["loam"]["gw"] = request_param.form.get("loamgw")
    valuesFileData["multus"]["loam"]["hostInterface"] = request_param.form.get("loamhostInterface")
    valuesFileData["multus"]["loam"]["cniVersion"] = request_param.form.get("loamcniVersion")

    valuesFileData["multus"]["lmg"]["numDevices"] = int(request_param.form.get("lmgnumDevices"))
    valuesFileData["multus"]["lmg"]["netNames"][0] = request_param.form.get("lmgnetNames1")
    valuesFileData["multus"]["lmg"]["netNames"][1] = request_param.form.get("lmgnetNames2")
    valuesFileData["multus"]["lmg"]["netNames"].insert(2, request_param.form.get("lmgnetNames3"))
    valuesFileData["multus"]["lmg"]["envName"][0] = request_param.form.get("lmgEnvName")
    valuesFileData["multus"]["lmg"]["envName"][1] = request_param.form.get("lmgEnvName2")

    valuesFileData["multus"]["llb"]["numDevices"] = int(request_param.form.get("llbnumDevices"))
    valuesFileData["multus"]["llb"]["netNames"][0] = request_param.form.get("llbnetNames1")
    valuesFileData["multus"]["llb"]["netNames"][1] = request_param.form.get("llbnetNames2")
    valuesFileData["multus"]["llb"]["netNames"][2] = request_param.form.get("llbnetNames3")
    valuesFileData["multus"]["llb"]["netNames"][3] = request_param.form.get("llbnetNames4")
    valuesFileData["multus"]["llb"]["netNames"][4] = request_param.form.get("llbnetNames5")
    valuesFileData["multus"]["llb"]["envName"][0] = request_param.form.get("envName1")
    valuesFileData["multus"]["llb"]["envName"][1] = request_param.form.get("envName2")

    valuesFileData["multus"]["attachDef"][0]["name"] = request_param.form.get("adname")
    valuesFileData["multus"]["attachDef"][0]["cniVersion"] = request_param.form.get("adcniVersion")
    valuesFileData["multus"]["attachDef"][0]["resourceName"] = request_param.form.get("adresourceName")
    valuesFileData["multus"]["attachDef"][0]["type"] = request_param.form.get("attachDefType")
    valuesFileData["multus"]["attachDef"][1]["name"] = request_param.form.get("adname2")
    valuesFileData["multus"]["attachDef"][1]["cniVersion"] = request_param.form.get("adcniVersion2")
    valuesFileData["multus"]["attachDef"][1]["resourceName"] = request_param.form.get("adresourceName2")
    valuesFileData["multus"]["attachDef"][1]["type"] = request_param.form.get("attachDefType2")
    valuesFileData["multus"]["groFlag"] = convertBooleanStringToInt(request_param.form.get("groFlag"))
    valuesFileData["multus"]["dsf"]["enable"] = convertBooleanStringToInt(request_param.form.get("dsfEnable"))
    valuesFileData["multus"]["dsf"]["numDsfDevices"] = convertBooleanStringToInt(
        request_param.form.get("numDsfDevices"))
    valuesFileData["multus"]["dpdk"]["enable"] = convertBooleanStringToInt(request_param.form.get("dpdkEnable"))
    valuesFileData["lmgScale"]["minReplicas"] = int(request_param.form.get("minReplicas"))
    valuesFileData["lmgScale"]["maxReplicas"] = int(request_param.form.get("maxReplicas"))
    valuesFileData["lmgScale"]["targetCPUUtilizationPercentage"] = int(request_param.form.get(
        "targetCPUUtilizationPercentage"))
    valuesFileData["llbScale"]["minReplicas"] = int(request_param.form.get("lbminReplicas"))
    valuesFileData["llbScale"]["maxReplicas"] = int(request_param.form.get("lbmaxReplicas"))
    valuesFileData["llbScale"]["targetCPUUtilizationPercentage"] = int(request_param.form.get(
        "lbtargetCPUUtilizationPercentage"))
    return valuesFileData


def update12R8MultusDishDictionary(request_param, valuesFileData):
    valuesFileData["multus"]["loam"]["ip"]["loamA"] = request_param.form.get("loamAIP")
    valuesFileData["multus"]["loam"]["ip"]["loamB"] = request_param.form.get("loamBIP")
    valuesFileData["multus"]["loam"]["ip"]["active"] = request_param.form.get("activeIP")
    valuesFileData["multus"]["loam"]["ip"]["standby"] = request_param.form.get("standbyIP")
    valuesFileData["multus"]["loam"]["netMask"] = int(request_param.form.get("loamnetMask"))
    valuesFileData["multus"]["loam"]["subnet"] = request_param.form.get("loamsubnet")
    valuesFileData["multus"]["loam"]["gw"] = request_param.form.get("loamgw")
    valuesFileData["multus"]["loam"]["hostInterface"] = request_param.form.get("loamhostInterface")
    valuesFileData["multus"]["loam"]["cniVersion"] = request_param.form.get("loamcniVersion")

    valuesFileData["multus"]["lmg"]["numDevices"] = int(request_param.form.get("lmgnumDevices"))
    valuesFileData["multus"]["lmg"]["netNames"][0] = request_param.form.get("lmgnetNames1")
    valuesFileData["multus"]["lmg"]["netNames"][1] = request_param.form.get("lmgnetNames2")
    valuesFileData["multus"]["lmg"]["netNames"][2] = request_param.form.get("lmgnetNames3")

    valuesFileData["multus"]["llb"]["numDevices"] = int(request_param.form.get("llbnumDevices"))
    valuesFileData["multus"]["llb"]["netNames"][0] = request_param.form.get("llbnetNames1")
    valuesFileData["multus"]["llb"]["netNames"][1] = request_param.form.get("llbnetNames2")
    valuesFileData["multus"]["llb"]["netNames"][2] = request_param.form.get("llbnetNames3")
    # valuesFileData["multus"]["llb"]["netNames"][3] = request_param.form.get("llbnetNames4")
    # valuesFileData["multus"]["llb"]["netNames"][4] = request_param.form.get("llbnetNames5")
    # valuesFileData["multus"]["llb"]["envName"][0] = request_param.form.get("envName1")
    # valuesFileData["multus"]["llb"]["envName"][1] = request_param.form.get("envName2")

    valuesFileData["multus"]["attachDef"][0]["name"] = request_param.form.get("adname")
    valuesFileData["multus"]["attachDef"][0]["cniVersion"] = request_param.form.get("adcniVersion")
    valuesFileData["multus"]["attachDef"][0]["resourceName"] = request_param.form.get("adresourceName")
    # valuesFileData["multus"]["attachDef"][0]["type"] = request_param.form.get("attachDefType")
    valuesFileData["multus"]["attachDef"][1]["name"] = request_param.form.get("adname2")
    valuesFileData["multus"]["attachDef"][1]["cniVersion"] = request_param.form.get("adcniVersion2")
    valuesFileData["multus"]["attachDef"][1]["resourceName"] = request_param.form.get("adresourceName2")
    # valuesFileData["multus"]["attachDef"][1]["type"] = request_param.form.get("attachDefType2")
    valuesFileData["multus"]["groFlag"] = convertBooleanStringToInt(request_param.form.get("groFlag"))
    valuesFileData["multus"]["dsf"]["enable"] = convertBooleanStringToInt(request_param.form.get("dsfEnable"))
    valuesFileData["multus"]["dsf"]["numDsfDevices"] = convertBooleanStringToInt(
        request_param.form.get("numDsfDevices"))
    valuesFileData["multus"]["xdp"]["enable"] = convertBooleanStringToInt(request_param.form.get("xdpenable"))
    valuesFileData["multus"]["xdp"]["rxRing"] = int(request_param.form.get("rxRing"))
    valuesFileData["multus"]["xdp"]["txRing"] = int(request_param.form.get("txRing"))
    valuesFileData["lmgScale"]["minReplicas"] = int(request_param.form.get("minReplicas"))
    valuesFileData["lmgScale"]["maxReplicas"] = int(request_param.form.get("maxReplicas"))
    valuesFileData["lmgScale"]["targetCPUUtilizationPercentage"] = int(request_param.form.get(
        "targetCPUUtilizationPercentage"))
    valuesFileData["llbScale"]["minReplicas"] = int(request_param.form.get("lbminReplicas"))
    valuesFileData["llbScale"]["maxReplicas"] = int(request_param.form.get("lbmaxReplicas"))
    valuesFileData["llbScale"]["targetCPUUtilizationPercentage"] = int(request_param.form.get(
        "lbtargetCPUUtilizationPercentage"))
    return valuesFileData


def update12R8ResourcesDictionary(request_param, valuesFileData):
    valuesFileData["resources"]["loam"]["cpu"] = int(request_param.form.get("loamcpu"))
    valuesFileData["resources"]["loam"]["memory"] = request_param.form.get("loammemory")
    valuesFileData["resources"]["lmg"]["cpu"] = int(request_param.form.get("lmgcpu"))
    valuesFileData["resources"]["lmg"]["memory"] = request_param.form.get("lmgmemory")
    valuesFileData["resources"]["lmg"]["hugepages1Gi"] = request_param.form.get("lmghugepages1Gi")
    valuesFileData["resources"]["lmg"]["multus"][0]["resourceName"] = request_param.form.get("lmgresourceName")
    valuesFileData["resources"]["lmg"]["multus"][0]["numDevices"] = int(request_param.form.get("lmgmultusnumDevices"))
    valuesFileData["resources"]["lmg"]["multus"][1]["resourceName"] = request_param.form.get("lmgmultusresourceName2")
    valuesFileData["resources"]["lmg"]["multus"][1]["numDevices"] = int(request_param.form.get("lmgnumDevices2"))

    valuesFileData["resources"]["llb"]["cpu"] = int(request_param.form.get("llbcpu"))
    valuesFileData["resources"]["llb"]["memory"] = request_param.form.get("llbmemory")
    valuesFileData["resources"]["llb"]["hugepages1Gi"] = request_param.form.get("llbhugepages1Gi")
    valuesFileData["resources"]["llb"]["multus"][0]["resourceName"] = request_param.form.get("multusresourceName")
    valuesFileData["resources"]["llb"]["multus"][0]["numDevices"] = int(request_param.form.get("multusnumDevices"))
    valuesFileData["resources"]["llb"]["multus"][1]["resourceName"] = request_param.form.get("multusresourceName2")
    valuesFileData["resources"]["llb"]["multus"][1]["numDevices"] = int(request_param.form.get("multusnumDevices2"))

    valuesFileData["resources"]["nasc"]["cpu"] = int(request_param.form.get("nasccpu"))
    valuesFileData["resources"]["nasc"]["memory"] = request_param.form.get("nascmemory")
    valuesFileData["resources"]["logging"]["cpu"] = request_param.form.get("loggingcpu")
    valuesFileData["resources"]["logging"]["memory"] = request_param.form.get("loggingmemory")
    return valuesFileData


def update12R8ResourcesDishDictionary(request_param, valuesFileData):
    valuesFileData["resources"]["loam"]["cpu"] = int(request_param.form.get("loamcpu"))
    valuesFileData["resources"]["loam"]["memory"] = request_param.form.get("loammemory")
    valuesFileData["resources"]["lmg"]["cpu"] = int(request_param.form.get("lmgcpu"))
    valuesFileData["resources"]["lmg"]["memory"] = request_param.form.get("lmgmemory")
    valuesFileData["resources"]["lmg"]["multus"][0]["resourceName"] = request_param.form.get("lmgresourceName")
    valuesFileData["resources"]["lmg"]["multus"][0]["numDevices"] = int(request_param.form.get("mlmgnumDevices"))
    valuesFileData["resources"]["lmg"]["multus"][1]["resourceName"] = request_param.form.get("lmgresourceName2")
    valuesFileData["resources"]["lmg"]["multus"][1]["numDevices"] = int(request_param.form.get("mlmgnumDevices2"))

    valuesFileData["resources"]["llb"]["cpu"] = int(request_param.form.get("llbcpu"))
    valuesFileData["resources"]["llb"]["memory"] = request_param.form.get("llbmemory")
    valuesFileData["resources"]["llb"]["multus"][0]["resourceName"] = request_param.form.get("llbresourceName")
    valuesFileData["resources"]["llb"]["multus"][0]["numDevices"] = int(request_param.form.get("mllbnumDevices"))
    valuesFileData["resources"]["llb"]["multus"][1]["resourceName"] = request_param.form.get("llbresourceName2")
    valuesFileData["resources"]["llb"]["multus"][1]["numDevices"] = int(request_param.form.get("mllbnumDevices2"))

    valuesFileData["resources"]["nasc"]["cpu"] = int(request_param.form.get("nasccpu"))
    valuesFileData["resources"]["nasc"]["memory"] = request_param.form.get("nascmemory")
    valuesFileData["resources"]["logging"]["cpu"] = int(request_param.form.get("loggingcpu"))
    valuesFileData["resources"]["logging"]["memory"] = request_param.form.get("loggingmemory")
    return valuesFileData


def update12R8StorageDictionary(request_param, valuesFileData):
    valuesFileData["storage"]["pvCreation"] = convertBooleanStringToInt(request_param.form.get("pvCreation"))
    # valuesFileData["storage"]["parentPath"] = request_param.form.get("parentPath")
    # valuesFileData["storage"]["pvLogsName"] = request_param.form.get("pvLogsName")
    valuesFileData["storage"]["pvStorageClass"] = request_param.form.get("pvStorageClass")
    # valuesFileData["storage"]["pvLogsClaimName"] = request_param.form.get("pvLogsClaimName")
    valuesFileData["storage"]["pvSize"] = str(int(request_param.form.get("pvSize"))) + "Gi"
    valuesFileData["storage"]["cfSize"] = str(int(request_param.form.get("cfSize"))) + "Gi"
    valuesFileData["storage"]["cfAInfo"][0]["pvName"] = request_param.form.get("cfApvName")
    valuesFileData["storage"]["cfAInfo"][0]["pvcName"] = request_param.form.get("cfApvcName")
    valuesFileData["storage"]["cfAInfo"][1]["pvName"] = request_param.form.get("cfApvName1")
    valuesFileData["storage"]["cfAInfo"][1]["pvcName"] = request_param.form.get("cfApvcName1")
    valuesFileData["storage"]["cfBInfo"][0]["pvName"] = request_param.form.get("cfBpvName")
    valuesFileData["storage"]["cfBInfo"][0]["pvcName"] = request_param.form.get("cfBpvcName")
    valuesFileData["storage"]["cfBInfo"][1]["pvName"] = request_param.form.get("cfBpvName1")
    valuesFileData["storage"]["cfBInfo"][1]["pvcName"] = request_param.form.get("cfBpvcName1")
    valuesFileData["rtScheduling"]["enable"] = int(request_param.form.get("rtenable"))
    valuesFileData["rtScheduling"]["cgroupHostPath"] = request_param.form.get("cgroupHostPath")
    valuesFileData["loamB"]["enable"] = convertBooleanStringToInt(request_param.form.get("loamBenable"))
    valuesFileData["bootString"]["ht"] = int(request_param.form.get("ht"))
    valuesFileData["bootString"]["fswo"] = int(request_param.form.get("fswo"))
    valuesFileData["bootString"]["dsfInfo"][0]["vlan"] = int(request_param.form.get("dsfInfovlan"))
    valuesFileData["bootString"]["dsfInfo"][0]["dsfString"] = request_param.form.get("dsfInfodsfString")
    valuesFileData["podsecuritypolicy"]["create"] = convertStringToBoolean(
        request_param.form.get("podsecuritypolicycreate"))
    valuesFileData["gwConfig"] = request_param.form.get("gwConfig")
    valuesFileData["gwRedundancy"]["active"] = convertBooleanStringToInt(request_param.form.get("gwRedundancyactive"))

    return valuesFileData


def update12R8StorageDishDictionary(request_param, valuesFileData):
    valuesFileData["storage"]["pvCreation"] = convertBooleanStringToInt(request_param.form.get("pvCreation"))
    valuesFileData["storage"]["parentPath"] = request_param.form.get("parentPath")
    valuesFileData["storage"]["pvLogsName"] = request_param.form.get("pvLogsName")
    valuesFileData["storage"]["pvStorageClass"] = request_param.form.get("pvStorageClass")
    valuesFileData["storage"]["pvLogsClaimName"] = request_param.form.get("pvLogsClaimName")
    valuesFileData["storage"]["pvSize"] = str(int(request_param.form.get("pvSize"))) + "Gi"
    valuesFileData["storage"]["cfSize"] = str(int(request_param.form.get("cfSize"))) + "Gi"
    valuesFileData["storage"]["cfAInfo"][0]["pvName"] = request_param.form.get("cfApvName")
    valuesFileData["storage"]["cfAInfo"][0]["pvcName"] = request_param.form.get("cfApvcName")
    valuesFileData["storage"]["cfAInfo"][1]["pvName"] = request_param.form.get("cfApvName1")
    valuesFileData["storage"]["cfAInfo"][1]["pvcName"] = request_param.form.get("cfApvcName1")
    valuesFileData["storage"]["cfBInfo"][0]["pvName"] = request_param.form.get("cfBpvName")
    valuesFileData["storage"]["cfBInfo"][0]["pvcName"] = request_param.form.get("cfBpvcName")
    valuesFileData["storage"]["cfBInfo"][1]["pvName"] = request_param.form.get("cfBpvName1")
    valuesFileData["storage"]["cfBInfo"][1]["pvcName"] = request_param.form.get("cfBpvcName1")
    valuesFileData["rtScheduling"]["enable"] = int(request_param.form.get("rtenable"))
    valuesFileData["rtScheduling"]["cgroupHostPath"] = request_param.form.get("cgroupHostPath")
    valuesFileData["loamB"]["enable"] = convertBooleanStringToInt(request_param.form.get("loamBenable"))
    valuesFileData["antiAffinity"]["loam"] = request_param.form.get("antiAffinityloam")
    valuesFileData["antiAffinity"]["lmg"] = request_param.form.get("antiAffinitylmg")
    valuesFileData["antiAffinity"]["llb"] = request_param.form.get("antiAffinityllb")
    valuesFileData["bootString"]["ht"] = int(request_param.form.get("ht"))
    valuesFileData["bootString"]["fswo"] = int(request_param.form.get("fswo"))
    valuesFileData["bootString"]["dsfInfo"][0]["vlan"] = int(request_param.form.get("dsfInfovlan"))
    valuesFileData["bootString"]["dsfInfo"][0]["dsfString"] = request_param.form.get("dsfInfodsfString")
    valuesFileData["bootString"]["lmg"]["cpcores"] = int(request_param.form.get("cpcores"))
    valuesFileData["bootString"]["lmg"]["cfp"] = int(request_param.form.get("cfp"))
    valuesFileData["bootString"]["llb"]["cpcores"] = int(request_param.form.get("llbcpcores"))
    valuesFileData["bootString"]["llb"]["cfp"] = int(request_param.form.get("llbcfp"))
    valuesFileData["podsecuritypolicy"]["create"] = convertStringToBoolean(
        request_param.form.get("podsecuritypolicycreate"))
    valuesFileData["gwConfig"] = request_param.form.get("gwConfig")
    valuesFileData["gwRedundancy"]["active"] = convertBooleanStringToInt(request_param.form.get("gwRedundancyactive"))

    return valuesFileData


def update12R8PeersDictionary(request_param, valuesFileData):
    if not convertStringToBoolean(request_param.form.get("skipPeers")):
        valuesFileData["peers"]["cdbx"]["ip"] = request_param.form.get("cdbxip")
        valuesFileData["peers"]["cdbx"]["port"] = int(request_param.form.get("cdbxport"))
        valuesFileData["peers"]["cdbx"]["interface"] = request_param.form.get("cdbxinterface")

        valuesFileData["peers"]["smf"]["ip"] = request_param.form.get("nrfip")
        valuesFileData["peers"]["smf"]["interface"] = request_param.form.get("nrfinterface")

        """valuesFileData["peers"]["upf"]["ip"] = request_param.form.get("upfip")
        valuesFileData["peers"]["upf"]["interface"] = request_param.form.get("upfinterface")
        valuesFileData["peers"]["upf"]["uuid"] = request_param.form.get("upfuuid")

        valuesFileData["peers"]["chf"]["ip"] = request_param.form.get("chfip")
        valuesFileData["peers"]["chf"]["port"] = int(request_param.form.get("chfport"))
        valuesFileData["peers"]["chf"]["interface"] = request_param.form.get("chfinterface")
        valuesFileData["peers"]["chf"]["uuid"] = request_param.form.get("chfuuid")

        valuesFileData["peers"]["pcf"]["ip"] = request_param.form.get("pcfip")
        valuesFileData["peers"]["pcf"]["port"] = int(request_param.form.get("pcfport"))
        valuesFileData["peers"]["pcf"]["interface"] = request_param.form.get("pcfinterface")
        valuesFileData["peers"]["pcf"]["uuid"] = request_param.form.get("pcfuuid")

        valuesFileData["peers"]["udmSdm"]["ip"] = request_param.form.get("udmSdmip")
        valuesFileData["peers"]["udmSdm"]["port"] = int(request_param.form.get("udmSdmport"))
        valuesFileData["peers"]["udmSdm"]["interface"] = request_param.form.get("udmSdminterface")
        valuesFileData["peers"]["udmSdm"]["uuid"] = request_param.form.get("udmSdmuuid")

        valuesFileData["peers"]["udmUecm"]["ip"] = request_param.form.get("udmUecmip")
        valuesFileData["peers"]["udmUecm"]["port"] = int(request_param.form.get("udmUecmport"))
        valuesFileData["peers"]["udmUecm"]["interface"] = request_param.form.get("udmUecminterface")
        valuesFileData["peers"]["udmUecm"]["uuid"] = request_param.form.get("udmUecmuuid")

        valuesFileData["peers"]["amf"]["ip"] = request_param.form.get("amfip")
        valuesFileData["peers"]["amf"]["port"] = int(request_param.form.get("amfport"))
        valuesFileData["peers"]["amf"]["interface"] = request_param.form.get("amfinterface")
        valuesFileData["peers"]["amf"]["uuid"] = request_param.form.get("amfuuid")

        valuesFileData["peers"]["pcscf"]["fqdn"] = request_param.form.get("fqdn")"""
    else:
        del valuesFileData["peers"]
        del valuesFileData["plmn"][1]
    valuesFileData["plmn"][0]["mcc"] = request_param.form.get("mcc")
    valuesFileData["plmn"][0]["mnc"] = request_param.form.get("mnc")

    valuesFileData["uuid"] = request_param.form.get("uuidfield")
    return valuesFileData


def update12R8PeersDishDictionary(request_param, valuesFileData):
    if not convertStringToBoolean(request_param.form.get("skipPeers")):
        valuesFileData["peers"]["cdbx"]["ip"] = request_param.form.get("cdbxip")
        valuesFileData["peers"]["cdbx"]["port"] = int(request_param.form.get("cdbxport"))
        valuesFileData["peers"]["cdbx"]["interface"] = request_param.form.get("cdbxinterface")

        valuesFileData["peers"]["smf"]["ip"] = request_param.form.get("nrfip")
        valuesFileData["peers"]["smf"]["interface"] = request_param.form.get("nrfinterface")

        """valuesFileData["peers"]["upf"]["ip"] = request_param.form.get("upfip")
        valuesFileData["peers"]["upf"]["interface"] = request_param.form.get("upfinterface")
        valuesFileData["peers"]["upf"]["uuid"] = request_param.form.get("upfuuid")

        valuesFileData["peers"]["chf"]["ip"] = request_param.form.get("chfip")
        valuesFileData["peers"]["chf"]["port"] = int(request_param.form.get("chfport"))
        valuesFileData["peers"]["chf"]["interface"] = request_param.form.get("chfinterface")
        valuesFileData["peers"]["chf"]["uuid"] = request_param.form.get("chfuuid")

        valuesFileData["peers"]["pcf"]["ip"] = request_param.form.get("pcfip")
        valuesFileData["peers"]["pcf"]["port"] = int(request_param.form.get("pcfport"))
        valuesFileData["peers"]["pcf"]["interface"] = request_param.form.get("pcfinterface")
        valuesFileData["peers"]["pcf"]["uuid"] = request_param.form.get("pcfuuid")

        valuesFileData["peers"]["udmSdm"]["ip"] = request_param.form.get("udmSdmip")
        valuesFileData["peers"]["udmSdm"]["port"] = int(request_param.form.get("udmSdmport"))
        valuesFileData["peers"]["udmSdm"]["interface"] = request_param.form.get("udmSdminterface")
        valuesFileData["peers"]["udmSdm"]["uuid"] = request_param.form.get("udmSdmuuid")

        valuesFileData["peers"]["udmUecm"]["ip"] = request_param.form.get("udmUecmip")
        valuesFileData["peers"]["udmUecm"]["port"] = int(request_param.form.get("udmUecmport"))
        valuesFileData["peers"]["udmUecm"]["interface"] = request_param.form.get("udmUecminterface")
        valuesFileData["peers"]["udmUecm"]["uuid"] = request_param.form.get("udmUecmuuid")

        valuesFileData["peers"]["amf"]["ip"] = request_param.form.get("amfip")
        valuesFileData["peers"]["amf"]["port"] = int(request_param.form.get("amfport"))
        valuesFileData["peers"]["amf"]["interface"] = request_param.form.get("amfinterface")
        valuesFileData["peers"]["amf"]["uuid"] = request_param.form.get("amfuuid")

        valuesFileData["peers"]["pcscf"]["fqdn"] = request_param.form.get("fqdn")"""
    else:
        del valuesFileData["peers"]
        del valuesFileData["plmn"][1]
    valuesFileData["plmn"][0]["mcc"] = request_param.form.get("mcc")
    valuesFileData["plmn"][0]["mnc"] = request_param.form.get("mnc")

    valuesFileData["uuid"] = request_param.form.get("uuidfield")
    return valuesFileData


def update12R8NetworkAndVPRNDictionary(request_param, valuesFileData):
    if not convertStringToBoolean(request_param.form.get("skipNetwork")):
        """valuesFileData["network"]["ecmp"] = int(request_param.form.get("ecmp"))
        valuesFileData["network"]["localAs"] = int(request_param.form.get("localAs"))
        valuesFileData["network"]["peerAs"] = int(request_param.form.get("peerAs"))
        valuesFileData["network"]["authKey"] = request_param.form.get("authKey")
        valuesFileData["network"]["policyOptions"]["prefixList"][0]["name"] = request_param.form.get("prefixname")
        valuesFileData["network"]["policyOptions"]["prefixList"][0]["prefix"] = request_param.form.get("prefix")
        valuesFileData["network"]["policyStatement"][0]["name"] = request_param.form.get("psname")
        valuesFileData["network"]["policyStatement"][0]["entryList"][0]["id"] = int(
            request_param.form.get("entryListid"))
        valuesFileData["network"]["policyStatement"][0]["entryList"][0]["prefixList"] = request_param.form.get(
            "prefixList")
        valuesFileData["network"]["policyStatement"][0]["entryList"][0]["georedState"] = request_param.form.get(
            "georedState")
        valuesFileData["network"]["interface"][0]["name"] = request_param.form.get("interfacename")
        valuesFileData["network"]["interface"][0]["ip"] = request_param.form.get("interfaceip")
        valuesFileData["network"]["interface"][0]["subnet"] = int(request_param.form.get("interfacesubnet"))
        valuesFileData["network"]["interface"][0]["port"] = request_param.form.get("interfaceport")
        valuesFileData["network"]["interface"][0]["vlan"] = int(request_param.form.get("interfacevlan"))
        valuesFileData["network"]["interface"][0]["bfd"] = convertStringToBoolean(request_param.form.get("bfd"))

        valuesFileData["network"]["interface"][1]["name"] = request_param.form.get("iname2")
        valuesFileData["network"]["interface"][1]["ip"] = request_param.form.get("ip2")
        valuesFileData["network"]["interface"][1]["subnet"] = int(request_param.form.get("subnet2"))
        valuesFileData["network"]["interface"][1]["port"] = request_param.form.get("port2")
        valuesFileData["network"]["interface"][1]["vlan"] = int(request_param.form.get("vlan2"))
        valuesFileData["network"]["interface"][1]["bfd"] = convertStringToBoolean(request_param.form.get("bfd2"))

        valuesFileData["network"]["interface"][2]["name"] = request_param.form.get("iname3")
        valuesFileData["network"]["interface"][2]["ip"] = request_param.form.get("ip3")
        valuesFileData["network"]["interface"][2]["subnet"] = int(request_param.form.get("subnet3"))
        valuesFileData["network"]["interface"][2]["port"] = request_param.form.get("port3")
        valuesFileData["network"]["interface"][2]["vlan"] = int(request_param.form.get("vlan3"))
        valuesFileData["network"]["interface"][2]["bfd"] = convertStringToBoolean(request_param.form.get("bfd3"))

        valuesFileData["network"]["interface"][3]["name"] = request_param.form.get("iname4")
        valuesFileData["network"]["interface"][3]["ip"] = request_param.form.get("ip4")
        valuesFileData["network"]["interface"][3]["subnet"] = int(request_param.form.get("subnet4"))
        valuesFileData["network"]["interface"][3]["port"] = request_param.form.get("port4")
        valuesFileData["network"]["interface"][3]["vlan"] = int(request_param.form.get("vlan4"))
        valuesFileData["network"]["interface"][3]["bfd"] = convertStringToBoolean(request_param.form.get("bfd4"))

        valuesFileData["network"]["interface"][4]["name"] = request_param.form.get("iname5")
        valuesFileData["network"]["interface"][4]["ip"] = request_param.form.get("ip5")
        valuesFileData["network"]["interface"][4]["subnet"] = int(request_param.form.get("subnet5"))
        valuesFileData["network"]["interface"][4]["port"] = request_param.form.get("port5")
        valuesFileData["network"]["interface"][4]["ip_reassembly"] = request_param.form.get("ip_reassembly")

        valuesFileData["network"]["interface"][5]["name"] = request_param.form.get("iname6")
        valuesFileData["network"]["interface"][5]["ip"] = request_param.form.get("ip6")
        valuesFileData["network"]["interface"][5]["subnet"] = int(request_param.form.get("subnet6"))
        valuesFileData["network"]["interface"][5]["port"] = request_param.form.get("port6")
        valuesFileData["network"]["interface"][5]["bfd"] = convertStringToBoolean(request_param.form.get("bfd6"))

        valuesFileData["network"]["staticRoute"][0]["subnet"] = request_param.form.get("srsubnet")
        valuesFileData["network"]["staticRoute"][0]["nextHop"][0] = request_param.form.get("nextHop")
        valuesFileData["network"]["staticRoute"][0]["nextHop"][1] = request_param.form.get("nextHop2")
        valuesFileData["network"]["staticRoute"][0]["bfd"] = convertStringToBoolean(request_param.form.get("srbfd"))

        valuesFileData["network"]["staticRoute"][1]["subnet"] = request_param.form.get("srsubnet1")
        valuesFileData["network"]["staticRoute"][1]["nextHop"][0] = request_param.form.get("nextHop3")
        valuesFileData["network"]["staticRoute"][1]["nextHop"][1] = request_param.form.get("nextHop4")
        valuesFileData["network"]["staticRoute"][1]["bfd"] = convertStringToBoolean(request_param.form.get("srbfd2"))

        valuesFileData["network"]["bgp"][0]["peerIp"] = request_param.form.get("peerIp")
        valuesFileData["network"]["bgp"][1]["peerIp"] = request_param.form.get("peerIp2")
        valuesFileData["network"]["bgp"][2]["peerIp"] = request_param.form.get("peerIp3")
        valuesFileData["network"]["bgp"][3]["peerIp"] = request_param.form.get("peerIp4")

        valuesFileData["apn"][0] = request_param.form.get("apn")

        valuesFileData["uepool"]["ipv4Prefix"] = request_param.form.get("ipv4Prefix")

        valuesFileData["vprn"][0]["id"] = int(request_param.form.get("vprnid"))
        valuesFileData["vprn"][0]["localAs"] = int(request_param.form.get("vprnlocalAs"))
        valuesFileData["vprn"][0]["peerAs"] = int(request_param.form.get("vprnpeerAs"))
        valuesFileData["vprn"][0]["authKey"] = request_param.form.get("vprnauthKey")
        valuesFileData["vprn"][0]["ecmp"] = int(request_param.form.get("vprnecmp"))
        valuesFileData["vprn"][0]["router_id"] = request_param.form.get("vprnrouter_id")
        valuesFileData["vprn"][0]["interface"][0]["name"] = request_param.form.get("vprnname")
        valuesFileData["vprn"][0]["interface"][0]["ip"] = request_param.form.get("vprnip")
        valuesFileData["vprn"][0]["interface"][0]["subnet"] = int(request_param.form.get("vprnsubnet"))
        valuesFileData["vprn"][0]["interface"][0]["sap"] = request_param.form.get("vprnsap")
        valuesFileData["vprn"][0]["interface"][0]["vlan"] = int(request_param.form.get("vprnvlan"))
        valuesFileData["vprn"][0]["interface"][0]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd"))

        valuesFileData["vprn"][0]["interface"][1]["name"] = request_param.form.get("vprnname2")
        valuesFileData["vprn"][0]["interface"][1]["ip"] = request_param.form.get("vprnip2")
        valuesFileData["vprn"][0]["interface"][1]["subnet"] = int(request_param.form.get("vprnsubnet2"))
        valuesFileData["vprn"][0]["interface"][1]["sap"] = request_param.form.get("vprnsap2")
        valuesFileData["vprn"][0]["interface"][1]["vlan"] = int(request_param.form.get("vprnvlan2"))
        valuesFileData["vprn"][0]["interface"][1]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd2"))

        valuesFileData["vprn"][0]["interface"][2]["name"] = request_param.form.get("vprnname3")
        valuesFileData["vprn"][0]["interface"][2]["ip"] = request_param.form.get("vprnip3")
        valuesFileData["vprn"][0]["interface"][2]["subnet"] = int(request_param.form.get("vprnsubnet3"))
        valuesFileData["vprn"][0]["interface"][2]["sap"] = request_param.form.get("vprnsap3")
        valuesFileData["vprn"][0]["interface"][2]["vlan"] = int(request_param.form.get("vprnvlan3"))
        valuesFileData["vprn"][0]["interface"][2]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd3"))

        valuesFileData["vprn"][0]["interface"][3]["name"] = request_param.form.get("vprnname4")
        valuesFileData["vprn"][0]["interface"][3]["ip"] = request_param.form.get("vprnip4")
        valuesFileData["vprn"][0]["interface"][3]["subnet"] = int(request_param.form.get("vprnsubnet4"))
        valuesFileData["vprn"][0]["interface"][3]["sap"] = request_param.form.get("vprnsap4")
        valuesFileData["vprn"][0]["interface"][3]["vlan"] = int(request_param.form.get("vprnvlan4"))
        valuesFileData["vprn"][0]["interface"][3]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd4"))

        valuesFileData["vprn"][0]["interface"][4]["name"] = request_param.form.get("vprnname5")
        valuesFileData["vprn"][0]["interface"][4]["ip"] = request_param.form.get("vprnip5")
        valuesFileData["vprn"][0]["interface"][4]["subnet"] = int(request_param.form.get("vprnsubnet5"))
        valuesFileData["vprn"][0]["interface"][4]["sap"] = request_param.form.get("vprnsap5")
        valuesFileData["vprn"][0]["interface"][4]["ip_reassembly"] = request_param.form.get("vprnip_reassembly")

        valuesFileData["vprn"][0]["interface"][5]["name"] = request_param.form.get("vprnname6")
        valuesFileData["vprn"][0]["interface"][5]["ip"] = request_param.form.get("vprnip6")
        valuesFileData["vprn"][0]["interface"][5]["subnet"] = int(request_param.form.get("vprnsubnet6"))
        valuesFileData["vprn"][0]["interface"][5]["sap"] = request_param.form.get("vprnsap6")
        valuesFileData["vprn"][0]["interface"][5]["ip_reassembly"] = request_param.form.get("vprnip_reassembly2")

        valuesFileData["vprn"][0]["interface"][6]["name"] = request_param.form.get("vprnname7")
        valuesFileData["vprn"][0]["interface"][6]["ip"] = request_param.form.get("vprnip7")
        valuesFileData["vprn"][0]["interface"][6]["subnet"] = int(request_param.form.get("vprnsubnet7"))
        valuesFileData["vprn"][0]["interface"][6]["sap"] = request_param.form.get("vprnsap7")

        valuesFileData["vprn"][0]["interface"][7]["name"] = request_param.form.get("vprnname8")
        valuesFileData["vprn"][0]["interface"][7]["ip"] = request_param.form.get("vprnip8")
        valuesFileData["vprn"][0]["interface"][7]["subnet"] = int(request_param.form.get("vprnsubnet8"))
        valuesFileData["vprn"][0]["interface"][7]["sap"] = request_param.form.get("vprnsap8")
        valuesFileData["vprn"][0]["interface"][7]["ip_reassembly"] = request_param.form.get("vprnip_reassembly3")

        valuesFileData["vprn"][0]["interface"][8]["name"] = request_param.form.get("vprnname9")
        valuesFileData["vprn"][0]["interface"][8]["ip"] = request_param.form.get("vprnip9")
        valuesFileData["vprn"][0]["interface"][8]["subnet"] = int(request_param.form.get("vprnsubnet9"))
        valuesFileData["vprn"][0]["interface"][8]["sap"] = request_param.form.get("vprnsap9")
        valuesFileData["vprn"][0]["interface"][8]["ip_reassembly"] = request_param.form.get("vprnip_reassembly4")

        valuesFileData["vprn"][0]["interface"][9]["name"] = request_param.form.get("vprnname10")
        valuesFileData["vprn"][0]["interface"][9]["ip"] = request_param.form.get("vprnip10")
        valuesFileData["vprn"][0]["interface"][9]["subnet"] = int(request_param.form.get("vprnsubnet10"))
        valuesFileData["vprn"][0]["interface"][9]["sap"] = request_param.form.get("vprnsap10")
        valuesFileData["vprn"][0]["interface"][9]["ip_reassembly"] = request_param.form.get("vprnip_reassembly5")

        valuesFileData["vprn"][0]["interface"][10]["name"] = request_param.form.get("vprnname11")
        valuesFileData["vprn"][0]["interface"][10]["ip"] = request_param.form.get("vprnip11")
        valuesFileData["vprn"][0]["interface"][10]["subnet"] = int(request_param.form.get("vprnsubnet11"))
        valuesFileData["vprn"][0]["interface"][10]["sap"] = request_param.form.get("vprnsap11")
        valuesFileData["vprn"][0]["interface"][10]["ip_reassembly"] = request_param.form.get("vprnip_reassembly6")

        valuesFileData["vprn"][0]["interface"][11]["name"] = request_param.form.get("vprnname12")
        valuesFileData["vprn"][0]["interface"][11]["ip"] = request_param.form.get("vprnip12")
        valuesFileData["vprn"][0]["interface"][11]["subnet"] = int(request_param.form.get("vprnsubnet12"))
        valuesFileData["vprn"][0]["interface"][11]["sap"] = request_param.form.get("vprnsap12")

        valuesFileData["vprn"][0]["interface"][12]["name"] = request_param.form.get("vprnname13")
        valuesFileData["vprn"][0]["interface"][12]["ip"] = request_param.form.get("vprnip13")
        valuesFileData["vprn"][0]["interface"][12]["subnet"] = int(request_param.form.get("vprnsubnet13"))
        valuesFileData["vprn"][0]["interface"][12]["sap"] = request_param.form.get("vprnsap13")
        valuesFileData["vprn"][0]["interface"][12]["ip_reassembly"] = request_param.form.get("vprnip_reassembly7")

        valuesFileData["vprn"][0]["interface"][13]["name"] = request_param.form.get("vprnname14")
        valuesFileData["vprn"][0]["interface"][13]["ip"] = request_param.form.get("vprnip14")
        valuesFileData["vprn"][0]["interface"][13]["subnet"] = int(request_param.form.get("vprnsubnet14"))
        valuesFileData["vprn"][0]["interface"][13]["sap"] = request_param.form.get("vprnsap14")
        valuesFileData["vprn"][0]["interface"][13]["ip_reassembly"] = request_param.form.get("vprnip_reassembly8")

        valuesFileData["vprn"][0]["staticRoute"][0]["subnet"] = request_param.form.get("vprnsrsubnet")
        valuesFileData["vprn"][0]["staticRoute"][0]["nextHop"][0] = request_param.form.get("vprnnextHop")
        valuesFileData["vprn"][0]["staticRoute"][0]["nextHop"][1] = request_param.form.get("vprnnextHop2")
        valuesFileData["vprn"][0]["staticRoute"][0]["bfd"] = convertStringToBoolean(request_param.form.get("vprnsrbfd"))

        valuesFileData["vprn"][0]["staticRoute"][1]["subnet"] = request_param.form.get("vprnsrsubnet1")
        valuesFileData["vprn"][0]["staticRoute"][1]["nextHop"][0] = request_param.form.get("vprnnextHop3")
        valuesFileData["vprn"][0]["staticRoute"][1]["nextHop"][1] = request_param.form.get("vprnnextHop4")
        valuesFileData["vprn"][0]["staticRoute"][1]["bfd"] = convertStringToBoolean(
            request_param.form.get("vprnsrbfd2"))

        valuesFileData["vprn"][0]["bgp"][0]["peerIp"] = request_param.form.get("vprnpeerIp")
        valuesFileData["vprn"][0]["bgp"][1]["peerIp"] = request_param.form.get("vprnpeerIp2")
        valuesFileData["vprn"][0]["bgp"][2]["peerIp"] = request_param.form.get("vprnpeerIp3")
        valuesFileData["vprn"][0]["bgp"][3]["peerIp"] = request_param.form.get("vprnpeerIp4")
        valuesFileData["uepool"]["ipv4Prefix"] = request_param.form.get("ipv4Prefix")"""
    else:
        del valuesFileData["network"]
        del valuesFileData["apn"]
    valuesFileData["cnfName"] = request_param.form.get("cnfName")

    return valuesFileData


def update12R8NetworkAndVPRNDishDictionary(request_param, valuesFileData):
    if not convertStringToBoolean(request_param.form.get("skipNetwork")):
        """valuesFileData["network"]["ecmp"] = int(request_param.form.get("ecmp"))
        valuesFileData["network"]["localAs"] = int(request_param.form.get("localAs"))
        valuesFileData["network"]["peerAs"] = int(request_param.form.get("peerAs"))
        valuesFileData["network"]["authKey"] = request_param.form.get("authKey")
        valuesFileData["network"]["policyOptions"]["prefixList"][0]["name"] = request_param.form.get("prefixname")
        valuesFileData["network"]["policyOptions"]["prefixList"][0]["prefix"] = request_param.form.get("prefix")
        valuesFileData["network"]["policyStatement"][0]["name"] = request_param.form.get("psname")
        valuesFileData["network"]["policyStatement"][0]["entryList"][0]["id"] = int(
            request_param.form.get("entryListid"))
        valuesFileData["network"]["policyStatement"][0]["entryList"][0]["prefixList"] = request_param.form.get(
            "prefixList")
        valuesFileData["network"]["policyStatement"][0]["entryList"][0]["georedState"] = request_param.form.get(
            "georedState")
        valuesFileData["network"]["interface"][0]["name"] = request_param.form.get("interfacename")
        valuesFileData["network"]["interface"][0]["ip"] = request_param.form.get("interfaceip")
        valuesFileData["network"]["interface"][0]["subnet"] = int(request_param.form.get("interfacesubnet"))
        valuesFileData["network"]["interface"][0]["port"] = request_param.form.get("interfaceport")
        valuesFileData["network"]["interface"][0]["vlan"] = int(request_param.form.get("interfacevlan"))
        valuesFileData["network"]["interface"][0]["bfd"] = convertStringToBoolean(request_param.form.get("bfd"))

        valuesFileData["network"]["interface"][1]["name"] = request_param.form.get("iname2")
        valuesFileData["network"]["interface"][1]["ip"] = request_param.form.get("ip2")
        valuesFileData["network"]["interface"][1]["subnet"] = int(request_param.form.get("subnet2"))
        valuesFileData["network"]["interface"][1]["port"] = request_param.form.get("port2")
        valuesFileData["network"]["interface"][1]["vlan"] = int(request_param.form.get("vlan2"))
        valuesFileData["network"]["interface"][1]["bfd"] = convertStringToBoolean(request_param.form.get("bfd2"))

        valuesFileData["network"]["interface"][2]["name"] = request_param.form.get("iname3")
        valuesFileData["network"]["interface"][2]["ip"] = request_param.form.get("ip3")
        valuesFileData["network"]["interface"][2]["subnet"] = int(request_param.form.get("subnet3"))
        valuesFileData["network"]["interface"][2]["port"] = request_param.form.get("port3")
        valuesFileData["network"]["interface"][2]["vlan"] = int(request_param.form.get("vlan3"))
        valuesFileData["network"]["interface"][2]["bfd"] = convertStringToBoolean(request_param.form.get("bfd3"))

        valuesFileData["network"]["interface"][3]["name"] = request_param.form.get("iname4")
        valuesFileData["network"]["interface"][3]["ip"] = request_param.form.get("ip4")
        valuesFileData["network"]["interface"][3]["subnet"] = int(request_param.form.get("subnet4"))
        valuesFileData["network"]["interface"][3]["port"] = request_param.form.get("port4")
        valuesFileData["network"]["interface"][3]["vlan"] = int(request_param.form.get("vlan4"))
        valuesFileData["network"]["interface"][3]["bfd"] = convertStringToBoolean(request_param.form.get("bfd4"))

        valuesFileData["network"]["interface"][4]["name"] = request_param.form.get("iname5")
        valuesFileData["network"]["interface"][4]["ip"] = request_param.form.get("ip5")
        valuesFileData["network"]["interface"][4]["subnet"] = int(request_param.form.get("subnet5"))
        valuesFileData["network"]["interface"][4]["port"] = request_param.form.get("port5")
        valuesFileData["network"]["interface"][4]["ip_reassembly"] = request_param.form.get("ip_reassembly")

        valuesFileData["network"]["interface"][5]["name"] = request_param.form.get("iname6")
        valuesFileData["network"]["interface"][5]["ip"] = request_param.form.get("ip6")
        valuesFileData["network"]["interface"][5]["subnet"] = int(request_param.form.get("subnet6"))
        valuesFileData["network"]["interface"][5]["port"] = request_param.form.get("port6")
        valuesFileData["network"]["interface"][5]["bfd"] = convertStringToBoolean(request_param.form.get("bfd6"))

        valuesFileData["network"]["staticRoute"][0]["subnet"] = request_param.form.get("srsubnet")
        valuesFileData["network"]["staticRoute"][0]["nextHop"][0] = request_param.form.get("nextHop")
        valuesFileData["network"]["staticRoute"][0]["nextHop"][1] = request_param.form.get("nextHop2")
        valuesFileData["network"]["staticRoute"][0]["bfd"] = convertStringToBoolean(request_param.form.get("srbfd"))

        valuesFileData["network"]["staticRoute"][1]["subnet"] = request_param.form.get("srsubnet1")
        valuesFileData["network"]["staticRoute"][1]["nextHop"][0] = request_param.form.get("nextHop3")
        valuesFileData["network"]["staticRoute"][1]["nextHop"][1] = request_param.form.get("nextHop4")
        valuesFileData["network"]["staticRoute"][1]["bfd"] = convertStringToBoolean(request_param.form.get("srbfd2"))

        valuesFileData["network"]["bgp"][0]["peerIp"] = request_param.form.get("peerIp")
        valuesFileData["network"]["bgp"][1]["peerIp"] = request_param.form.get("peerIp2")
        valuesFileData["network"]["bgp"][2]["peerIp"] = request_param.form.get("peerIp3")
        valuesFileData["network"]["bgp"][3]["peerIp"] = request_param.form.get("peerIp4")

        valuesFileData["apn"][0] = request_param.form.get("apn")

        valuesFileData["uepool"]["ipv4Prefix"] = request_param.form.get("ipv4Prefix")

        valuesFileData["vprn"][0]["id"] = int(request_param.form.get("vprnid"))
        valuesFileData["vprn"][0]["localAs"] = int(request_param.form.get("vprnlocalAs"))
        valuesFileData["vprn"][0]["peerAs"] = int(request_param.form.get("vprnpeerAs"))
        valuesFileData["vprn"][0]["authKey"] = request_param.form.get("vprnauthKey")
        valuesFileData["vprn"][0]["ecmp"] = int(request_param.form.get("vprnecmp"))
        valuesFileData["vprn"][0]["router_id"] = request_param.form.get("vprnrouter_id")
        valuesFileData["vprn"][0]["interface"][0]["name"] = request_param.form.get("vprnname")
        valuesFileData["vprn"][0]["interface"][0]["ip"] = request_param.form.get("vprnip")
        valuesFileData["vprn"][0]["interface"][0]["subnet"] = int(request_param.form.get("vprnsubnet"))
        valuesFileData["vprn"][0]["interface"][0]["sap"] = request_param.form.get("vprnsap")
        valuesFileData["vprn"][0]["interface"][0]["vlan"] = int(request_param.form.get("vprnvlan"))
        valuesFileData["vprn"][0]["interface"][0]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd"))

        valuesFileData["vprn"][0]["interface"][1]["name"] = request_param.form.get("vprnname2")
        valuesFileData["vprn"][0]["interface"][1]["ip"] = request_param.form.get("vprnip2")
        valuesFileData["vprn"][0]["interface"][1]["subnet"] = int(request_param.form.get("vprnsubnet2"))
        valuesFileData["vprn"][0]["interface"][1]["sap"] = request_param.form.get("vprnsap2")
        valuesFileData["vprn"][0]["interface"][1]["vlan"] = int(request_param.form.get("vprnvlan2"))
        valuesFileData["vprn"][0]["interface"][1]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd2"))

        valuesFileData["vprn"][0]["interface"][2]["name"] = request_param.form.get("vprnname3")
        valuesFileData["vprn"][0]["interface"][2]["ip"] = request_param.form.get("vprnip3")
        valuesFileData["vprn"][0]["interface"][2]["subnet"] = int(request_param.form.get("vprnsubnet3"))
        valuesFileData["vprn"][0]["interface"][2]["sap"] = request_param.form.get("vprnsap3")
        valuesFileData["vprn"][0]["interface"][2]["vlan"] = int(request_param.form.get("vprnvlan3"))
        valuesFileData["vprn"][0]["interface"][2]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd3"))

        valuesFileData["vprn"][0]["interface"][3]["name"] = request_param.form.get("vprnname4")
        valuesFileData["vprn"][0]["interface"][3]["ip"] = request_param.form.get("vprnip4")
        valuesFileData["vprn"][0]["interface"][3]["subnet"] = int(request_param.form.get("vprnsubnet4"))
        valuesFileData["vprn"][0]["interface"][3]["sap"] = request_param.form.get("vprnsap4")
        valuesFileData["vprn"][0]["interface"][3]["vlan"] = int(request_param.form.get("vprnvlan4"))
        valuesFileData["vprn"][0]["interface"][3]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd4"))

        valuesFileData["vprn"][0]["interface"][4]["name"] = request_param.form.get("vprnname5")
        valuesFileData["vprn"][0]["interface"][4]["ip"] = request_param.form.get("vprnip5")
        valuesFileData["vprn"][0]["interface"][4]["subnet"] = int(request_param.form.get("vprnsubnet5"))
        valuesFileData["vprn"][0]["interface"][4]["sap"] = request_param.form.get("vprnsap5")
        valuesFileData["vprn"][0]["interface"][4]["ip_reassembly"] = request_param.form.get("vprnip_reassembly")

        valuesFileData["vprn"][0]["interface"][5]["name"] = request_param.form.get("vprnname6")
        valuesFileData["vprn"][0]["interface"][5]["ip"] = request_param.form.get("vprnip6")
        valuesFileData["vprn"][0]["interface"][5]["subnet"] = int(request_param.form.get("vprnsubnet6"))
        valuesFileData["vprn"][0]["interface"][5]["sap"] = request_param.form.get("vprnsap6")
        valuesFileData["vprn"][0]["interface"][5]["ip_reassembly"] = request_param.form.get("vprnip_reassembly2")

        valuesFileData["vprn"][0]["interface"][6]["name"] = request_param.form.get("vprnname7")
        valuesFileData["vprn"][0]["interface"][6]["ip"] = request_param.form.get("vprnip7")
        valuesFileData["vprn"][0]["interface"][6]["subnet"] = int(request_param.form.get("vprnsubnet7"))
        valuesFileData["vprn"][0]["interface"][6]["sap"] = request_param.form.get("vprnsap7")

        valuesFileData["vprn"][0]["interface"][7]["name"] = request_param.form.get("vprnname8")
        valuesFileData["vprn"][0]["interface"][7]["ip"] = request_param.form.get("vprnip8")
        valuesFileData["vprn"][0]["interface"][7]["subnet"] = int(request_param.form.get("vprnsubnet8"))
        valuesFileData["vprn"][0]["interface"][7]["sap"] = request_param.form.get("vprnsap8")
        valuesFileData["vprn"][0]["interface"][7]["ip_reassembly"] = request_param.form.get("vprnip_reassembly3")

        valuesFileData["vprn"][0]["interface"][8]["name"] = request_param.form.get("vprnname9")
        valuesFileData["vprn"][0]["interface"][8]["ip"] = request_param.form.get("vprnip9")
        valuesFileData["vprn"][0]["interface"][8]["subnet"] = int(request_param.form.get("vprnsubnet9"))
        valuesFileData["vprn"][0]["interface"][8]["sap"] = request_param.form.get("vprnsap9")
        valuesFileData["vprn"][0]["interface"][8]["ip_reassembly"] = request_param.form.get("vprnip_reassembly4")

        valuesFileData["vprn"][0]["interface"][9]["name"] = request_param.form.get("vprnname10")
        valuesFileData["vprn"][0]["interface"][9]["ip"] = request_param.form.get("vprnip10")
        valuesFileData["vprn"][0]["interface"][9]["subnet"] = int(request_param.form.get("vprnsubnet10"))
        valuesFileData["vprn"][0]["interface"][9]["sap"] = request_param.form.get("vprnsap10")
        valuesFileData["vprn"][0]["interface"][9]["ip_reassembly"] = request_param.form.get("vprnip_reassembly5")

        valuesFileData["vprn"][0]["interface"][10]["name"] = request_param.form.get("vprnname11")
        valuesFileData["vprn"][0]["interface"][10]["ip"] = request_param.form.get("vprnip11")
        valuesFileData["vprn"][0]["interface"][10]["subnet"] = int(request_param.form.get("vprnsubnet11"))
        valuesFileData["vprn"][0]["interface"][10]["sap"] = request_param.form.get("vprnsap11")
        valuesFileData["vprn"][0]["interface"][10]["ip_reassembly"] = request_param.form.get("vprnip_reassembly6")

        valuesFileData["vprn"][0]["interface"][11]["name"] = request_param.form.get("vprnname12")
        valuesFileData["vprn"][0]["interface"][11]["ip"] = request_param.form.get("vprnip12")
        valuesFileData["vprn"][0]["interface"][11]["subnet"] = int(request_param.form.get("vprnsubnet12"))
        valuesFileData["vprn"][0]["interface"][11]["sap"] = request_param.form.get("vprnsap12")

        valuesFileData["vprn"][0]["interface"][12]["name"] = request_param.form.get("vprnname13")
        valuesFileData["vprn"][0]["interface"][12]["ip"] = request_param.form.get("vprnip13")
        valuesFileData["vprn"][0]["interface"][12]["subnet"] = int(request_param.form.get("vprnsubnet13"))
        valuesFileData["vprn"][0]["interface"][12]["sap"] = request_param.form.get("vprnsap13")
        valuesFileData["vprn"][0]["interface"][12]["ip_reassembly"] = request_param.form.get("vprnip_reassembly7")

        valuesFileData["vprn"][0]["interface"][13]["name"] = request_param.form.get("vprnname14")
        valuesFileData["vprn"][0]["interface"][13]["ip"] = request_param.form.get("vprnip14")
        valuesFileData["vprn"][0]["interface"][13]["subnet"] = int(request_param.form.get("vprnsubnet14"))
        valuesFileData["vprn"][0]["interface"][13]["sap"] = request_param.form.get("vprnsap14")
        valuesFileData["vprn"][0]["interface"][13]["ip_reassembly"] = request_param.form.get("vprnip_reassembly8")

        valuesFileData["vprn"][0]["staticRoute"][0]["subnet"] = request_param.form.get("vprnsrsubnet")
        valuesFileData["vprn"][0]["staticRoute"][0]["nextHop"][0] = request_param.form.get("vprnnextHop")
        valuesFileData["vprn"][0]["staticRoute"][0]["nextHop"][1] = request_param.form.get("vprnnextHop2")
        valuesFileData["vprn"][0]["staticRoute"][0]["bfd"] = convertStringToBoolean(request_param.form.get("vprnsrbfd"))

        valuesFileData["vprn"][0]["staticRoute"][1]["subnet"] = request_param.form.get("vprnsrsubnet1")
        valuesFileData["vprn"][0]["staticRoute"][1]["nextHop"][0] = request_param.form.get("vprnnextHop3")
        valuesFileData["vprn"][0]["staticRoute"][1]["nextHop"][1] = request_param.form.get("vprnnextHop4")
        valuesFileData["vprn"][0]["staticRoute"][1]["bfd"] = convertStringToBoolean(
            request_param.form.get("vprnsrbfd2"))

        valuesFileData["vprn"][0]["bgp"][0]["peerIp"] = request_param.form.get("vprnpeerIp")
        valuesFileData["vprn"][0]["bgp"][1]["peerIp"] = request_param.form.get("vprnpeerIp2")
        valuesFileData["vprn"][0]["bgp"][2]["peerIp"] = request_param.form.get("vprnpeerIp3")
        valuesFileData["vprn"][0]["bgp"][3]["peerIp"] = request_param.form.get("vprnpeerIp4")
        valuesFileData["uepool"]["ipv4Prefix"] = request_param.form.get("ipv4Prefix")"""
    else:
        del valuesFileData["network"]
        del valuesFileData["apn"]
    valuesFileData["cnfName"] = request_param.form.get("cnfName")

    return valuesFileData


def convertStringToBoolean(value):
    if value == "True" or value == "true" or value == "1":
        return True
    else:
        return False


def convertBooleanStringToInt(value):
    print(value)
    if value == "True" or value == "true" or value == "1":
        return 1
    else:
        return 0


def createNodSelectorDictionary():
    nodeSelector = {'loamA': [{'key': "", 'value': ""}], 'loamB': [{'key': "", 'value': ""}],
                    'llb': [{'key': "", 'value': ""}], 'lmg': [{'key': "", 'value': ""}]}
    return nodeSelector


def createMdADictionary():
    mdaDict = {'llb': 1, 'lmg': 2}
    return mdaDict
