def updateDictionary(request_param, valuesFileData, selectedVersion):
    if selectedVersion == "12.0R8":
        if request_param.form["input_type"] == "values_ncsBmDpdk":
            update12R8ServicesDictionary(request_param, valuesFileData)
            update12R8NascDictionary(request_param, valuesFileData)
            update12R8LoggingAndMultusDictionary(request_param, valuesFileData)
            update12R8ResourcesDictionary(request_param, valuesFileData)
            update12R8StorageDictionary(request_param, valuesFileData)
            update12R8PeersDictionary(request_param, valuesFileData)
            update12R8NetworkAndVPRNDictionary(request_param, valuesFileData)
        else:
            update12R8DishServicesDictionary(request_param, valuesFileData)
            update12R8NascDishDictionary(request_param, valuesFileData)
            update12R8LoggingAndMultusDishDictionary(request_param, valuesFileData)
            update12R8ResourcesDishDictionary(request_param, valuesFileData)
            update12R8StorageDishDictionary(request_param, valuesFileData)
            update12R8PeersDishDictionary(request_param, valuesFileData)
            update12R8NetworkAndVPRNDishDictionary(request_param, valuesFileData)
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


def update12R8DishServicesDictionary(request_param, valuesFileData):
    valuesFileData["service"]["loam"]["telnet"]["nodePort"] = int(request_param.form.get("nodePort"))
    valuesFileData["service"]["loam"]["telnet"]["port"] = int(request_param.form.get("port"))
    valuesFileData["service"]["loam"]["telnet"]["targetPort"] = int(request_param.form.get("targetPort"))

    valuesFileData["service"]["loam"]["ssh"]["nodePort"] = int(request_param.form.get("sshnodePort"))
    valuesFileData["service"]["loam"]["ssh"]["port"] = int(request_param.form.get("sshport"))
    valuesFileData["service"]["loam"]["ssh"]["targetPort"] = int(request_param.form.get("sshtargetPort"))

    valuesFileData["service"]["loam"]["snmp1"]["nodePort"] = int(request_param.form.get("snmpnodePort"))
    valuesFileData["service"]["loam"]["snmp1"]["port"] = int(request_param.form.get("snmpport"))
    valuesFileData["service"]["loam"]["snmp1"]["targetPort"] = int(request_param.form.get("snmptargetPort"))

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
    valuesFileData["nasc"]["enable"] = convertBooleanStringToInt(request_param.form.get("enable"))
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


def update12R8NascDishDictionary(request_param, valuesFileData):
    valuesFileData["nasc"]["enable"] = convertBooleanStringToInt(request_param.form.get("enable"))
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
    # valuesFileData["multus"]["lmg"]["envName"][0] = request_param.form.get("lmgEnvName")
    # del valuesFileData["multus"]["lmg"]["envName"][1]

    valuesFileData["multus"]["llb"]["numDevices"] = int(request_param.form.get("llbnumDevices"))
    valuesFileData["multus"]["llb"]["netNames"][0] = request_param.form.get("llbnetNames1")
    valuesFileData["multus"]["llb"]["netNames"][1] = request_param.form.get("llbnetNames2")
    valuesFileData["multus"]["llb"]["netNames"][2] = request_param.form.get("llbnetNames3")
    # valuesFileData["multus"]["llb"]["envName"][0] = request_param.form.get("envName1")
    # valuesFileData["multus"]["llb"]["envName"][1] = request_param.form.get("envName2")

    valuesFileData["multus"]["attachDef"][0]["name"] = request_param.form.get("adname")
    valuesFileData["multus"]["attachDef"][0]["cniVersion"] = request_param.form.get("adcniVersion")
    valuesFileData["multus"]["attachDef"][0]["resourceName"] = request_param.form.get("adresourceName")
    valuesFileData["multus"]["attachDef"][1]["name"] = request_param.form.get("adname2")
    valuesFileData["multus"]["attachDef"][1]["cniVersion"] = request_param.form.get("adcniVersion2")
    valuesFileData["multus"]["attachDef"][1]["resourceName"] = request_param.form.get("adresourceName2")
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

    valuesFileData["multus"]["llb"]["numDevices"] = int(request_param.form.get("llbnumDevices"))
    valuesFileData["multus"]["llb"]["netNames"][0] = request_param.form.get("llbnetNames1")
    valuesFileData["multus"]["llb"]["netNames"][1] = request_param.form.get("llbnetNames2")
    valuesFileData["multus"]["llb"]["netNames"][2] = request_param.form.get("llbnetNames3")

    valuesFileData["multus"]["attachDef"][0]["name"] = request_param.form.get("adname")
    valuesFileData["multus"]["attachDef"][0]["cniVersion"] = request_param.form.get("adcniVersion")
    valuesFileData["multus"]["attachDef"][0]["resourceName"] = request_param.form.get("adresourceName")
    valuesFileData["multus"]["attachDef"][1]["name"] = request_param.form.get("adname2")
    valuesFileData["multus"]["attachDef"][1]["cniVersion"] = request_param.form.get("adcniVersion2")
    valuesFileData["multus"]["attachDef"][1]["resourceName"] = request_param.form.get("adresourceName2")
    valuesFileData["multus"]["groFlag"] = convertBooleanStringToInt(request_param.form.get("groFlag"))
    valuesFileData["multus"]["dsf"]["enable"] = convertBooleanStringToInt(request_param.form.get("dsfEnable"))
    valuesFileData["multus"]["dsf"]["numDsfDevices"] = int(
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
    valuesFileData["resources"]["lmg"]["multus"][0]["numDevices"] = int(request_param.form.get("lmgnumDevices"))

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
    valuesFileData["resources"]["logging"]["memory"] =request_param.form.get("loggingmemory")
    valuesFileData.insert(9, "mda", createMdADictionary())
    valuesFileData["mda"]["llb"] = int(request_param.form.get("mdallb"))
    valuesFileData["mda"]["lmg"] = int(request_param.form.get("mdalmg"))
    return valuesFileData


def update12R8ResourcesDishDictionary(request_param, valuesFileData):
    valuesFileData["resources"]["loam"]["cpu"] = int(request_param.form.get("loamcpu"))
    valuesFileData["resources"]["loam"]["memory"] = str(int(request_param.form.get("loammemory"))) + "Gi"
    valuesFileData["resources"]["lmg"]["cpu"] = int(request_param.form.get("lmgcpu"))
    valuesFileData["resources"]["lmg"]["memory"] = str(int(request_param.form.get("lmgmemory"))) + "Gi"
    valuesFileData["resources"]["lmg"]["multus"][0]["resourceName"] = request_param.form.get("lmgresourceName")
    valuesFileData["resources"]["lmg"]["multus"][0]["numDevices"] = int(request_param.form.get("lmgmultusnumDevices"))

    valuesFileData["resources"]["llb"]["cpu"] = int(request_param.form.get("llbcpu"))
    valuesFileData["resources"]["llb"]["memory"] = str(int(request_param.form.get("llbmemory"))) + "Gi"
    valuesFileData["resources"]["llb"]["multus"][0]["resourceName"] = request_param.form.get("llbresourceName")
    valuesFileData["resources"]["llb"]["multus"][0]["numDevices"] = int(request_param.form.get("llbmultusnumDevices"))
    valuesFileData["resources"]["llb"]["multus"][1]["resourceName"] = request_param.form.get("llbresourceName2")
    valuesFileData["resources"]["llb"]["multus"][1]["numDevices"] = int(request_param.form.get("llbmultusnumDevices2"))

    valuesFileData["resources"]["nasc"]["cpu"] = int(request_param.form.get("nasccpu"))
    valuesFileData["resources"]["nasc"]["memory"] = str(int(request_param.form.get("nascmemory"))) + "Gi"
    valuesFileData["resources"]["logging"]["cpu"] = int(request_param.form.get("loggingcpu"))
    valuesFileData["resources"]["logging"]["memory"] = str(int(request_param.form.get("loggingmemory"))) + "Gi"
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
    valuesFileData["podsecuritypolicy"]["privileged"] = convertStringToBoolean(
        request_param.form.get("podsecuritypolicyprivileged"))
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
    valuesFileData["fabMtu"] = int(request_param.form.get("fabMtu"))
    valuesFileData["podsecuritypolicy"]["create"] = convertStringToBoolean(
        request_param.form.get("podsecuritypolicycreate"))
    valuesFileData["gwConfig"] = request_param.form.get("storagegwConfig")
    valuesFileData["gwRedundancy"]["active"] = convertBooleanStringToInt(request_param.form.get("storageactive"))

    return valuesFileData


def update12R8PeersDictionary(request_param, valuesFileData):
    if not convertStringToBoolean(request_param.form.get("skipPeers")):
        valuesFileData["peers"]["cdbx"]["ip"] = request_param.form.get("cdbxip")
        valuesFileData["peers"]["cdbx"]["port"] = int(request_param.form.get("cdbxport"))
        valuesFileData["peers"]["cdbx"]["interface"] = request_param.form.get("cdbxinterface")

        valuesFileData["peers"]["nrf"]["ip"] = request_param.form.get("nrfip")
        valuesFileData["peers"]["nrf"]["port"] = int(request_param.form.get("nrfport"))
        valuesFileData["peers"]["nrf"]["uuid"] = request_param.form.get("nrfuuid")
        valuesFileData["peers"]["nrf"]["interface"] = request_param.form.get("nrfinterface")

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

        valuesFileData["peers"]["pcscf"]["fqdn"] = request_param.form.get("fqdn")

        valuesFileData["slice"][0]["sst"] = int(request_param.form.get("sst"))
        valuesFileData["slice"][0]["sd"] = request_param.form.get("ssd")

        valuesFileData["slice"][1]["sst"] = int(request_param.form.get("sst2"))
        valuesFileData["slice"][1]["sd"] = request_param.form.get("ssd2")"""
    else:
        del valuesFileData["peers"]
        del valuesFileData["slice"]
        del valuesFileData["plmn"][1]
    valuesFileData["plmn"][0]["mcc"] = request_param.form.get("mcc")
    valuesFileData["plmn"][0]["mnc"] = request_param.form.get("mnc")

    valuesFileData["uuid"] = request_param.form.get("uuidfield")
    return valuesFileData


def update12R8PeersDishDictionary(request_param, valuesFileData):
    valuesFileData["peers"]["cdbx"]["ip"] = request_param.form.get("cdbxip")
    valuesFileData["peers"]["cdbx"]["port"] = int(request_param.form.get("cdbxport"))
    valuesFileData["peers"]["cdbx"]["interface"] = request_param.form.get("cdbxinterface")

    valuesFileData["peers"]["nrf"]["ip"] = request_param.form.get("nrfip")
    valuesFileData["peers"]["nrf"]["port"] = int(request_param.form.get("nrfport"))
    valuesFileData["peers"]["nrf"]["uuid"] = request_param.form.get("nrfuuid")
    valuesFileData["peers"]["nrf"]["interface"] = request_param.form.get("nrfinterface")

    valuesFileData["peers"]["upf"]["interface"] = request_param.form.get("upfinterface")
    valuesFileData["peers"]["upf"]["peerList"][0]["ip"] = request_param.form.get("upfip")
    valuesFileData["peers"]["upf"]["peerList"][0]["uuid"] = request_param.form.get("upfuuid")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][0]["name"] = request_param.form.get("apn1name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][0]["uepool"]["name"] = request_param.form.get("uepool1name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][0]["uepool"]["prefix6List"][0][
        "ipv6Prefix"] = request_param.form.get("apn1ipv6Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][0]["uepool"]["prefix6List"][1][
        "ipv6Prefix"] = request_param.form.get("apn1ipv6Prefix2")

    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][1]["name"] = request_param.form.get("apn2name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][1]["uepool"]["name"] = request_param.form.get("uepool2name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][1]["uepool"]["prefix6List"][0][
        "ipv6Prefix"] = request_param.form.get("apn2ipv6Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][1]["uepool"]["prefix6List"][1][
        "ipv6Prefix"] = request_param.form.get("apn2ipv6Prefix2")

    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][2]["name"] = request_param.form.get("apn3name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][2]["uepool"]["name"] = request_param.form.get("uepool3name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][2]["uepool"]["prefix6List"][0][
        "ipv6Prefix"] = request_param.form.get("apn3ipv6Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][2]["uepool"]["prefix6List"][1][
        "ipv6Prefix"] = request_param.form.get("apn3ipv6Prefix2")

    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][3]["name"] = request_param.form.get("apn4name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][3]["uepool"]["name"] = request_param.form.get("uepool4name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][3]["uepool"]["prefix6List"][0][
        "ipv6Prefix"] = request_param.form.get("apn4ipv6Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][3]["uepool"]["prefix6List"][1][
        "ipv6Prefix"] = request_param.form.get("apn4ipv6Prefix2")

    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][4]["name"] = request_param.form.get("apn5name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][4]["uepool"]["name"] = request_param.form.get("uepool5name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][4]["uepool"]["prefix4List"][0][
        "ipv4Prefix"] = request_param.form.get("apn5ipv4Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][4]["uepool"]["prefix6List"][0][
        "ipv6Prefix"] = request_param.form.get("apn5ipv6Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][4]["uepool"]["prefix6List"][1][
        "ipv6Prefix"] = request_param.form.get("apn5ipv6Prefix2")

    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][5]["name"] = request_param.form.get("apn6name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][5]["uepool"]["name"] = request_param.form.get("uepool6name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][5]["uepool"]["prefix4List"][0][
        "ipv4Prefix"] = request_param.form.get("apn6ipv4Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][5]["uepool"]["prefix6List"][0][
        "ipv6Prefix"] = request_param.form.get("apn6ipv6Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][5]["uepool"]["prefix6List"][1][
        "ipv6Prefix"] = request_param.form.get("apn6ipv6Prefix2")

    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][6]["name"] = request_param.form.get("apn7name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][6]["uepool"]["name"] = request_param.form.get("uepool7name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][6]["uepool"]["prefix4List"][0][
        "ipv4Prefix"] = request_param.form.get("apn7ipv4Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][6]["uepool"]["prefix6List"][0][
        "ipv6Prefix"] = request_param.form.get("apn7ipv6Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][6]["uepool"]["prefix6List"][1][
        "ipv6Prefix"] = request_param.form.get("apn7ipv6Prefix2")

    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][7]["name"] = request_param.form.get("apn8name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][7]["uepool"]["name"] = request_param.form.get("uepool8name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][7]["uepool"]["prefix4List"][0][
        "ipv4Prefix"] = request_param.form.get("apn8ipv4Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][7]["uepool"]["prefix6List"][0][
        "ipv6Prefix"] = request_param.form.get("apn8ipv6Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][7]["uepool"]["prefix6List"][1][
        "ipv6Prefix"] = request_param.form.get("apn8ipv6Prefix2")

    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][8]["name"] = request_param.form.get("apn9name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][8]["uepool"]["name"] = request_param.form.get("uepool9name")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][8]["uepool"]["prefix4List"][0][
        "ipv4Prefix"] = request_param.form.get("apn9ipv4Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][8]["uepool"]["prefix6List"][0][
        "ipv6Prefix"] = request_param.form.get("apn9ipv6Prefix")
    valuesFileData["peers"]["upf"]["peerList"][0]["apn"][8]["uepool"]["prefix6List"][1][
        "ipv6Prefix"] = request_param.form.get("apn9ipv6Prefix2")

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

    valuesFileData["peers"]["pcscfv6"]["ip"] = request_param.form.get("pcscfv6")
    valuesFileData["peers"]["pcscfv4"]["ip"] = request_param.form.get("pcscfv4")

    valuesFileData["slice"][0]["sst"] = int(request_param.form.get("sst"))
    valuesFileData["slice"][0]["sd"] = request_param.form.get("ssd")

    valuesFileData["slice"][1]["sst"] = int(request_param.form.get("sst2"))
    valuesFileData["slice"][1]["sd"] = request_param.form.get("ssd2")

    valuesFileData["slice"][2]["sst"] = int(request_param.form.get("sst3"))
    valuesFileData["slice"][2]["sd"] = request_param.form.get("ssd3")

    valuesFileData["slice"][3]["sst"] = int(request_param.form.get("sst4"))
    valuesFileData["slice"][3]["sd"] = request_param.form.get("ssd4")

    valuesFileData["tai"]["taiNamelist"][0]["name"] = request_param.form.get("taiNamelistname")
    valuesFileData["tai"]["taiNamelist"][0]["taimcc"] = request_param.form.get("taimcc")
    valuesFileData["tai"]["taiNamelist"][0]["taimnc"] = request_param.form.get("taimnc")
    valuesFileData["tai"]["taiNamelist"][0]["start"] = request_param.form.get("start")
    valuesFileData["tai"]["taiNamelist"][0]["end"] = request_param.form.get("end")

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
    valuesFileData["network"]["ecmp"] = int(request_param.form.get("ecmp"))
    valuesFileData["network"]["localAs"] = int(request_param.form.get("localAs"))
    valuesFileData["network"]["router_id"] = request_param.form.get("router_id")
    valuesFileData["network"]["peerAs"] = int(request_param.form.get("peerAs"))
    valuesFileData["network"]["authKey"] = request_param.form.get("authKey")
    valuesFileData["network"]["bgpExport"] = request_param.form.get("bgpExport")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][0]["name"] = request_param.form.get("prefixname")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][0]["prefixList"][0]["prefix"] = request_param.form.get(
        "prefix1")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][0]["prefixList"][1]["prefix"] = request_param.form.get(
        "prefix2")

    valuesFileData["network"]["policyOptions"]["prefixNamelist"][1]["name"] = request_param.form.get(
        "prefixNamelist2name")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][1]["prefixList"][0]["prefix"] = request_param.form.get(
        "prefixNamelist2prefix1")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][1]["prefixList"][1]["prefix"] = request_param.form.get(
        "prefixNamelist2prefix2")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][1]["prefixList"][2]["prefix"] = request_param.form.get(
        "prefixNamelist2prefix3")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][1]["prefixList"][3]["prefix"] = request_param.form.get(
        "prefixNamelist2prefix4")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][1]["prefixList"][4]["prefix"] = request_param.form.get(
        "prefixNamelist2prefix5")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][1]["prefixList"][5]["prefix"] = request_param.form.get(
        "prefixNamelist2prefix6")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][1]["prefixList"][6]["prefix"] = request_param.form.get(
        "prefixNamelist2prefix7")

    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["name"] = request_param.form.get(
        "prefixNamelist3name")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][0]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix1")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][1]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix2")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][2]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix3")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][3]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix4")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][4]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix5")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][5]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix6")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][6]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix7")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][7]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix8")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][8]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix9")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][9]["prefix"] = request_param.form.get(
        "prefixNamelist3prefix10")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][10][
        "prefix"] = request_param.form.get("prefixNamelist3prefix11")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][11][
        "prefix"] = request_param.form.get("prefixNamelist3prefix12")
    valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][12][
        "prefix"] = request_param.form.get("prefixNamelist3prefix13")
    # valuesFileData["network"]["policyOptions"]["prefixNamelist"][2]["prefixList"][13][
    #    "prefix"] = request_param.form.get("prefixNamelist3prefix14")

    valuesFileData["network"]["policyOptions"]["policyStatement"][0]["name"] = request_param.form.get("psname")
    valuesFileData["network"]["policyOptions"]["policyStatement"][0]["entryList"][0]["id"] = int(
        request_param.form.get("entryListid"))
    valuesFileData["network"]["policyOptions"]["policyStatement"][0]["entryList"][0][
        "prefixList"] = request_param.form.get(
        "prefixList")

    valuesFileData["network"]["policyOptions"]["policyStatement"][1]["name"] = request_param.form.get("ps2name")
    valuesFileData["network"]["policyOptions"]["policyStatement"][1]["entryList"][0]["id"] = int(
        request_param.form.get("ps2entryListid"))
    valuesFileData["network"]["policyOptions"]["policyStatement"][1]["entryList"][0][
        "prefixList"] = request_param.form.get(
        "ps2prefixList")

    valuesFileData["network"]["policyOptions"]["policyStatement"][2]["name"] = request_param.form.get("ps3name")
    valuesFileData["network"]["policyOptions"]["policyStatement"][2]["entryList"][0]["id"] = int(
        request_param.form.get("ps3entryListid"))
    valuesFileData["network"]["policyOptions"]["policyStatement"][2]["entryList"][0][
        "prefixList"] = request_param.form.get(
        "ps3prefixList")

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

    valuesFileData["network"]["interface"][5]["name"] = request_param.form.get("iname6")
    valuesFileData["network"]["interface"][5]["ip"] = request_param.form.get("ip6")
    valuesFileData["network"]["interface"][5]["subnet"] = int(request_param.form.get("subnet6"))
    valuesFileData["network"]["interface"][5]["port"] = request_param.form.get("port6")
    valuesFileData["network"]["interface"][5]["ip_reassembly"] = request_param.form.get("ip_reassembly")

    valuesFileData["network"]["staticRoute"][0]["subnet"] = request_param.form.get("srsubnet")
    valuesFileData["network"]["staticRoute"][0]["nextHop"][0] = request_param.form.get("nextHop")
    valuesFileData["network"]["staticRoute"][0]["nextHop"][1] = request_param.form.get("nextHop2")
    valuesFileData["network"]["staticRoute"][0]["bfd"] = convertStringToBoolean(request_param.form.get("srbfd"))

    valuesFileData["network"]["staticRoute"][1]["subnet"] = request_param.form.get("srsubnet1")
    valuesFileData["network"]["staticRoute"][1]["nextHop"][0] = request_param.form.get("nextHop3")
    valuesFileData["network"]["staticRoute"][1]["nextHop"][1] = request_param.form.get("nextHop4")
    valuesFileData["network"]["staticRoute"][1]["bfd"] = convertStringToBoolean(request_param.form.get("srbfd2"))

    valuesFileData["network"]["bgp"][0]["peerIp"] = request_param.form.get("peerIp")
    valuesFileData["network"]["bgp"][0]["localAddr"] = request_param.form.get("localAddr")
    valuesFileData["network"]["bgp"][1]["peerIp"] = request_param.form.get("peerIp3")
    valuesFileData["network"]["bgp"][1]["localAddr"] = request_param.form.get("localAddr2")

    valuesFileData["dns"]["priv4"] = request_param.form.get("priv4")
    valuesFileData["dns"]["secv4"] = request_param.form.get("secv4")

    valuesFileData["apn"][0]["name"] = request_param.form.get("networkapnname")
    valuesFileData["apn"][0]["pcoOptionlist"]["pcscfv6"] = convertStringToBoolean(request_param.form.get("apnpcscfv6"))
    valuesFileData["apn"][0]["uepool"][0]["router"] = int(request_param.form.get("apnrouter"))
    valuesFileData["apn"][0]["uepool"][0]["name"] = request_param.form.get("networkuepoolname")

    valuesFileData["apn"][1]["name"] = request_param.form.get("networkapn2name")
    valuesFileData["apn"][1]["pcoOptionlist"]["pcscfv6"] = convertStringToBoolean(request_param.form.get("apn2pcscfv6"))
    valuesFileData["apn"][1]["uepool"][0]["router"] = int(request_param.form.get("apn2router"))
    valuesFileData["apn"][1]["uepool"][0]["name"] = request_param.form.get("networkuepool2name")

    valuesFileData["apn"][2]["name"] = request_param.form.get("networkapn3name")
    valuesFileData["apn"][2]["pcoOptionlist"]["pcscfv4"] = convertStringToBoolean(request_param.form.get("apn3pcscfv6"))
    valuesFileData["apn"][2]["uepool"][0]["router"] = int(request_param.form.get("apn3router"))
    valuesFileData["apn"][2]["uepool"][0]["name"] = request_param.form.get("networkuepool3name")

    valuesFileData["apn"][3]["name"] = request_param.form.get("networkapn4name")
    valuesFileData["apn"][3]["pcoOptionlist"]["pcscfv4"] = convertStringToBoolean(request_param.form.get("apn4pcscfv6"))
    valuesFileData["apn"][3]["uepool"][0]["router"] = int(request_param.form.get("apn4router"))
    valuesFileData["apn"][3]["uepool"][0]["name"] = request_param.form.get("networkuepool4name")

    valuesFileData["apn"][4]["name"] = request_param.form.get("networkapn5name")
    valuesFileData["apn"][4]["pcrfSel"] = request_param.form.get("apn5pcrfSel")
    valuesFileData["apn"][4]["qciPolicy"]["name"] = request_param.form.get("apn5qciPolicy")
    valuesFileData["apn"][4]["pcoOptionlist"]["pcscfv4"] = convertStringToBoolean(request_param.form.get("apn5pcscfv6"))
    valuesFileData["apn"][4]["uepool"][0]["router"] = int(request_param.form.get("apn5router"))
    valuesFileData["apn"][4]["uepool"][0]["name"] = request_param.form.get("networkuepool5name")

    valuesFileData["apn"][5]["name"] = request_param.form.get("networkapn6name")
    valuesFileData["apn"][5]["pcoOptionlist"]["pcscfv6"] = convertStringToBoolean(request_param.form.get("apn6pcscfv6"))
    valuesFileData["apn"][5]["uepool"]["router"] = int(request_param.form.get("apn6router"))
    valuesFileData["apn"][5]["uepool"]["name"] = request_param.form.get("networkuepool6name")

    valuesFileData["apn"][6]["name"] = request_param.form.get("networkapn7name")
    valuesFileData["apn"][6]["pcoOptionlist"]["pcscfv6"] = convertStringToBoolean(request_param.form.get("apn7pcscfv6"))
    valuesFileData["apn"][6]["uepool"]["router"] = int(request_param.form.get("apn7router"))
    valuesFileData["apn"][6]["uepool"]["name"] = request_param.form.get("networkuepool7name")

    valuesFileData["apn"][7]["name"] = request_param.form.get("networkapn8name")
    valuesFileData["apn"][7]["pcoOptionlist"]["pcscfv6"] = convertStringToBoolean(request_param.form.get("apn8pcscfv6"))
    valuesFileData["apn"][7]["uepool"]["router"] = int(request_param.form.get("apn8router"))
    valuesFileData["apn"][7]["uepool"]["name"] = request_param.form.get("networkuepool8name")

    valuesFileData["apn"][8]["name"] = request_param.form.get("networkapn9name")
    valuesFileData["apn"][8]["pcoOptionlist"]["pcscfv6"] = convertStringToBoolean(request_param.form.get("apn9pcscfv6"))
    valuesFileData["apn"][8]["uepool"]["router"] = int(request_param.form.get("apn9router"))
    valuesFileData["apn"][8]["uepool"]["name"] = request_param.form.get("networkuepool9name")
    valuesFileData["apn"][8]["pcrfSel"] = request_param.form.get("apn9pcrfSel")
    valuesFileData["apn"][8]["qciPolicy"]["name"] = request_param.form.get("apn9qciPolicyname")

    valuesFileData["apn"][9]["name"] = request_param.form.get("networkapn10name")
    valuesFileData["apn"][9]["pcoOptionlist"]["pcscfv6"] = convertStringToBoolean(
        request_param.form.get("apn10pcscfv6"))
    valuesFileData["apn"][9]["uepool"]["router"] = int(request_param.form.get("apn10router"))
    valuesFileData["apn"][9]["uepool"]["name"] = request_param.form.get("networkuepool10name")
    valuesFileData["apn"][9]["pcrfSel"] = request_param.form.get("apn10pcrfSel")
    valuesFileData["apn"][9]["qciPolicy"]["name"] = request_param.form.get("apn10qciPolicyname")

    valuesFileData["uepool"][0]["router"] = int(request_param.form.get("uepoolrouter"))
    valuesFileData["uepool"][0]["name"] = request_param.form.get("uepoolnamefield")
    valuesFileData["uepool"][0]["ipv4Prefix"] = request_param.form.get("uepoolipv4Prefix")

    valuesFileData["vprn"][0]["id"] = int(request_param.form.get("vprnid"))
    valuesFileData["vprn"][0]["localAs"] = int(request_param.form.get("vprnlocalAs"))
    valuesFileData["vprn"][0]["ecmp"] = int(request_param.form.get("vprnecmp"))
    valuesFileData["vprn"][0]["router_id"] = request_param.form.get("vprnrouter_id")
    valuesFileData["vprn"][0]["interface"][0]["name"] = request_param.form.get("vprnname")
    valuesFileData["vprn"][0]["interface"][0]["ip"] = request_param.form.get("vprnip")
    valuesFileData["vprn"][0]["interface"][0]["subnet"] = int(request_param.form.get("vprnsubnet"))
    valuesFileData["vprn"][0]["interface"][0]["ipv6"] = request_param.form.get("vprnipv6")
    valuesFileData["vprn"][0]["interface"][0]["v6subnet"] = int(request_param.form.get("vprnv6subnet"))
    valuesFileData["vprn"][0]["interface"][0]["v6bfd"] = convertStringToBoolean(request_param.form.get("vprnv6bfd"))
    valuesFileData["vprn"][0]["interface"][0]["sap"] = request_param.form.get("vprnsap")
    valuesFileData["vprn"][0]["interface"][0]["vlan"] = int(request_param.form.get("vprnvlan"))
    valuesFileData["vprn"][0]["interface"][0]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd"))

    valuesFileData["vprn"][0]["interface"][1]["name"] = request_param.form.get("vprnname2")
    valuesFileData["vprn"][0]["interface"][1]["ip"] = request_param.form.get("vprnip2")
    valuesFileData["vprn"][0]["interface"][1]["subnet"] = int(request_param.form.get("vprnsubnet2"))
    valuesFileData["vprn"][0]["interface"][1]["ipv6"] = request_param.form.get("vprnipv62")
    valuesFileData["vprn"][0]["interface"][1]["v6subnet"] = int(request_param.form.get("vprnv6subnet2"))
    valuesFileData["vprn"][0]["interface"][1]["v6bfd"] = convertStringToBoolean(request_param.form.get("vprnv6bfd2"))
    valuesFileData["vprn"][0]["interface"][1]["sap"] = request_param.form.get("vprnsap2")
    valuesFileData["vprn"][0]["interface"][1]["vlan"] = int(request_param.form.get("vprnvlan2"))
    valuesFileData["vprn"][0]["interface"][1]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd2"))

    valuesFileData["vprn"][0]["interface"][2]["name"] = request_param.form.get("vprnname3")
    valuesFileData["vprn"][0]["interface"][2]["ip"] = request_param.form.get("vprnip3")
    valuesFileData["vprn"][0]["interface"][2]["subnet"] = int(request_param.form.get("vprnsubnet3"))
    valuesFileData["vprn"][0]["interface"][2]["ipv6"] = request_param.form.get("vprnipv63")
    valuesFileData["vprn"][0]["interface"][2]["v6subnet"] = int(request_param.form.get("vprnv6subnet3"))
    valuesFileData["vprn"][0]["interface"][2]["v6bfd"] = convertStringToBoolean(request_param.form.get("vprnv6bfd3"))
    valuesFileData["vprn"][0]["interface"][2]["sap"] = request_param.form.get("vprnsap3")
    valuesFileData["vprn"][0]["interface"][2]["vlan"] = int(request_param.form.get("vprnvlan3"))
    valuesFileData["vprn"][0]["interface"][2]["bfd"] = convertStringToBoolean(request_param.form.get("vprnbfd3"))

    valuesFileData["vprn"][0]["interface"][3]["name"] = request_param.form.get("vprnname4")
    valuesFileData["vprn"][0]["interface"][3]["ip"] = request_param.form.get("vprnip4")
    valuesFileData["vprn"][0]["interface"][3]["subnet"] = int(request_param.form.get("vprnsubnet4"))
    valuesFileData["vprn"][0]["interface"][3]["ipv6"] = request_param.form.get("vprnipv64")
    valuesFileData["vprn"][0]["interface"][3]["v6subnet"] = int(request_param.form.get("vprnv6subnet4"))
    valuesFileData["vprn"][0]["interface"][3]["v6bfd"] = convertStringToBoolean(request_param.form.get("vprnv6bfd4"))
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
    valuesFileData["vprn"][0]["interface"][5]["ipv6"] = request_param.form.get("vprnipv66")
    valuesFileData["vprn"][0]["interface"][5]["v6subnet"] = int(request_param.form.get("vprnv6subnet6"))
    valuesFileData["vprn"][0]["interface"][5]["sap"] = request_param.form.get("vprnsap6")
    valuesFileData["vprn"][0]["interface"][5]["ip_reassembly"] = request_param.form.get("vprnip_reassembly2")

    valuesFileData["vprn"][0]["interface"][6]["name"] = request_param.form.get("vprnname7")
    valuesFileData["vprn"][0]["interface"][6]["ip"] = request_param.form.get("vprnip7")
    valuesFileData["vprn"][0]["interface"][6]["subnet"] = int(request_param.form.get("vprnsubnet7"))
    valuesFileData["vprn"][0]["interface"][6]["ipv6"] = request_param.form.get("vprnipv67")
    valuesFileData["vprn"][0]["interface"][6]["v6subnet"] = int(request_param.form.get("vprnv6subnet7"))
    valuesFileData["vprn"][0]["interface"][6]["sap"] = request_param.form.get("vprnsap7")

    valuesFileData["vprn"][0]["interface"][7]["name"] = request_param.form.get("vprnname8")
    valuesFileData["vprn"][0]["interface"][7]["ip"] = request_param.form.get("vprnip8")
    valuesFileData["vprn"][0]["interface"][7]["subnet"] = int(request_param.form.get("vprnsubnet8"))
    valuesFileData["vprn"][0]["interface"][7]["ipv6"] = request_param.form.get("vprnipv68")
    valuesFileData["vprn"][0]["interface"][7]["v6subnet"] = int(request_param.form.get("vprnv6subnet8"))
    valuesFileData["vprn"][0]["interface"][7]["sap"] = request_param.form.get("vprnsap8")
    valuesFileData["vprn"][0]["interface"][7]["ip_reassembly"] = request_param.form.get("vprnip_reassembly3")

    valuesFileData["vprn"][0]["interface"][8]["name"] = request_param.form.get("vprnname9")
    valuesFileData["vprn"][0]["interface"][8]["ip"] = request_param.form.get("vprnip9")
    valuesFileData["vprn"][0]["interface"][8]["subnet"] = int(request_param.form.get("vprnsubnet9"))
    valuesFileData["vprn"][0]["interface"][8]["ipv6"] = request_param.form.get("vprnipv69")
    valuesFileData["vprn"][0]["interface"][8]["v6subnet"] = int(request_param.form.get("vprnv6subnet9"))
    valuesFileData["vprn"][0]["interface"][8]["sap"] = request_param.form.get("vprnsap9")
    valuesFileData["vprn"][0]["interface"][8]["ip_reassembly"] = request_param.form.get("vprnip_reassembly4")

    valuesFileData["vprn"][0]["interface"][9]["name"] = request_param.form.get("vprnname10")
    valuesFileData["vprn"][0]["interface"][9]["ip"] = request_param.form.get("vprnip10")
    valuesFileData["vprn"][0]["interface"][9]["subnet"] = int(request_param.form.get("vprnsubnet10"))
    valuesFileData["vprn"][0]["interface"][9]["ipv6"] = request_param.form.get("vprnipv610")
    valuesFileData["vprn"][0]["interface"][9]["v6subnet"] = int(request_param.form.get("vprnv6subnet10"))
    valuesFileData["vprn"][0]["interface"][9]["sap"] = request_param.form.get("vprnsap10")
    valuesFileData["vprn"][0]["interface"][9]["ip_reassembly"] = request_param.form.get("vprnip_reassembly5")

    valuesFileData["vprn"][0]["interface"][10]["name"] = request_param.form.get("vprnname11")
    valuesFileData["vprn"][0]["interface"][10]["ip"] = request_param.form.get("vprnip11")
    valuesFileData["vprn"][0]["interface"][10]["subnet"] = int(request_param.form.get("vprnsubnet11"))
    valuesFileData["vprn"][0]["interface"][10]["ipv6"] = request_param.form.get("vprnipv611")
    valuesFileData["vprn"][0]["interface"][10]["v6subnet"] = int(request_param.form.get("vprnv6subnet11"))
    valuesFileData["vprn"][0]["interface"][10]["sap"] = request_param.form.get("vprnsap11")
    valuesFileData["vprn"][0]["interface"][10]["ip_reassembly"] = request_param.form.get("vprnip_reassembly6")

    valuesFileData["vprn"][0]["interface"][11]["name"] = request_param.form.get("vprnname12")
    valuesFileData["vprn"][0]["interface"][11]["ip"] = request_param.form.get("vprnip12")
    valuesFileData["vprn"][0]["interface"][11]["subnet"] = int(request_param.form.get("vprnsubnet12"))
    valuesFileData["vprn"][0]["interface"][11]["ipv6"] = request_param.form.get("vprnipv612")
    valuesFileData["vprn"][0]["interface"][11]["v6subnet"] = int(request_param.form.get("vprnv6subnet12"))
    valuesFileData["vprn"][0]["interface"][11]["sap"] = request_param.form.get("vprnsap12")
    valuesFileData["vprn"][0]["interface"][11]["ip_reassembly"] = request_param.form.get("vprnip_reassembly7")

    valuesFileData["vprn"][0]["interface"][12]["name"] = request_param.form.get("vprnname13")
    valuesFileData["vprn"][0]["interface"][12]["ip"] = request_param.form.get("vprnip13")
    valuesFileData["vprn"][0]["interface"][12]["subnet"] = int(request_param.form.get("vprnsubnet13"))
    valuesFileData["vprn"][0]["interface"][12]["ipv6"] = request_param.form.get("vprnipv613")
    valuesFileData["vprn"][0]["interface"][12]["v6subnet"] = int(request_param.form.get("vprnv6subnet13"))
    valuesFileData["vprn"][0]["interface"][12]["sap"] = request_param.form.get("vprnsap13")

    valuesFileData["vprn"][0]["interface"][13]["name"] = request_param.form.get("vprnname14")
    valuesFileData["vprn"][0]["interface"][13]["ip"] = request_param.form.get("vprnip14")
    valuesFileData["vprn"][0]["interface"][13]["subnet"] = int(request_param.form.get("vprnsubnet14"))
    valuesFileData["vprn"][0]["interface"][13]["ipv6"] = request_param.form.get("vprnipv614")
    valuesFileData["vprn"][0]["interface"][13]["v6subnet"] = int(request_param.form.get("vprnv6subnet14"))
    valuesFileData["vprn"][0]["interface"][13]["sap"] = request_param.form.get("vprnsap14")
    valuesFileData["vprn"][0]["interface"][13]["ip_reassembly"] = request_param.form.get("vprnip_reassembly9")

    valuesFileData["vprn"][0]["interface"][14]["name"] = request_param.form.get("vprnname15")
    valuesFileData["vprn"][0]["interface"][14]["ip"] = request_param.form.get("vprnip15")
    valuesFileData["vprn"][0]["interface"][14]["subnet"] = int(request_param.form.get("vprnsubnet15"))
    valuesFileData["vprn"][0]["interface"][14]["ipv6"] = request_param.form.get("vprnipv615")
    valuesFileData["vprn"][0]["interface"][14]["v6subnet"] = int(request_param.form.get("vprnv6subnet15"))
    valuesFileData["vprn"][0]["interface"][14]["sap"] = request_param.form.get("vprnsap15")
    valuesFileData["vprn"][0]["interface"][14]["ip_reassembly"] = request_param.form.get("vprnip_reassembly10")

    valuesFileData["vprn"][0]["interface"][15]["name"] = request_param.form.get("vprnname16")
    valuesFileData["vprn"][0]["interface"][15]["ip"] = request_param.form.get("vprnip16")
    valuesFileData["vprn"][0]["interface"][15]["subnet"] = int(request_param.form.get("vprnsubnet16"))
    valuesFileData["vprn"][0]["interface"][15]["ipv6"] = request_param.form.get("vprnipv616")
    valuesFileData["vprn"][0]["interface"][15]["v6subnet"] = int(request_param.form.get("vprnv6subnet16"))
    valuesFileData["vprn"][0]["interface"][15]["sap"] = request_param.form.get("vprnsap16")
    valuesFileData["vprn"][0]["interface"][15]["ip_reassembly"] = request_param.form.get("vprnip_reassembly11")

    valuesFileData["vprn"][0]["interface"][16]["name"] = request_param.form.get("vprnname17")
    valuesFileData["vprn"][0]["interface"][16]["ip"] = request_param.form.get("vprnip17")
    valuesFileData["vprn"][0]["interface"][16]["subnet"] = int(request_param.form.get("vprnsubnet17"))
    valuesFileData["vprn"][0]["interface"][16]["ipv6"] = request_param.form.get("vprnipv617")
    valuesFileData["vprn"][0]["interface"][16]["v6subnet"] = int(request_param.form.get("vprnv6subnet17"))
    valuesFileData["vprn"][0]["interface"][16]["sap"] = request_param.form.get("vprnsap17")
    valuesFileData["vprn"][0]["interface"][16]["ip_reassembly"] = request_param.form.get("vprnip_reassembly12")

    valuesFileData["vprn"][0]["interface"][17]["name"] = request_param.form.get("vprnname18")
    valuesFileData["vprn"][0]["interface"][17]["ip"] = request_param.form.get("vprnip18")
    valuesFileData["vprn"][0]["interface"][17]["subnet"] = int(request_param.form.get("vprnsubnet18"))
    valuesFileData["vprn"][0]["interface"][17]["sap"] = request_param.form.get("vprnsap18")
    valuesFileData["vprn"][0]["interface"][17]["ip_reassembly"] = request_param.form.get("vprnip_reassembly13")

    valuesFileData["vprn"][0]["staticRoute"][0]["subnet"] = request_param.form.get("vprnsrsubnet")
    valuesFileData["vprn"][0]["staticRoute"][0]["nextHop"][0] = request_param.form.get("vprnnextHop")
    valuesFileData["vprn"][0]["staticRoute"][0]["nextHop"][1] = request_param.form.get("vprnnextHop2")
    valuesFileData["vprn"][0]["staticRoute"][0]["bfd"] = convertStringToBoolean(request_param.form.get("vprnsrbfd"))

    valuesFileData["vprn"][0]["staticRoute"][1]["subnet"] = request_param.form.get("vprnsrsubnet2")
    valuesFileData["vprn"][0]["staticRoute"][1]["nextHop"][0] = request_param.form.get("vprnnextHop21")
    valuesFileData["vprn"][0]["staticRoute"][1]["nextHop"][1] = request_param.form.get("vprnnextHop22")
    valuesFileData["vprn"][0]["staticRoute"][1]["bfd"] = convertStringToBoolean(
        request_param.form.get("vprnsrbfd2"))

    valuesFileData["vprn"][0]["staticRoute"][2]["subnet"] = request_param.form.get("vprnsrsubnet3")
    valuesFileData["vprn"][0]["staticRoute"][2]["nextHop"][0] = request_param.form.get("vprnnextHop31")
    valuesFileData["vprn"][0]["staticRoute"][2]["nextHop"][1] = request_param.form.get("vprnnextHop32")
    valuesFileData["vprn"][0]["staticRoute"][2]["bfd"] = convertStringToBoolean(
        request_param.form.get("vprnsrbfd3"))

    valuesFileData["vprn"][0]["staticRoute"][3]["subnet"] = request_param.form.get("vprnsrsubnet4")
    valuesFileData["vprn"][0]["staticRoute"][3]["nextHop"][0] = request_param.form.get("vprnnextHop41")
    valuesFileData["vprn"][0]["staticRoute"][3]["nextHop"][1] = request_param.form.get("vprnnextHop42")
    valuesFileData["vprn"][0]["staticRoute"][3]["bfd"] = convertStringToBoolean(
        request_param.form.get("vprnsrbfd4"))

    valuesFileData["vprn"][0]["bgp"]["groupList"][0]["name"] = request_param.form.get("bgpname")
    valuesFileData["vprn"][0]["bgp"]["groupList"][0]["peerAs"] = int(request_param.form.get("bgppeerAs"))
    valuesFileData["vprn"][0]["bgp"]["groupList"][0]["authKey"] = request_param.form.get("bgpauthKey")
    valuesFileData["vprn"][0]["bgp"]["groupList"][0]["bgpExport"] = request_param.form.get("bgpbgpExport")
    valuesFileData["vprn"][0]["bgp"]["groupList"][0]["peerList"][0]["peerIp"] = request_param.form.get("vprnpeerIp")
    valuesFileData["vprn"][0]["bgp"]["groupList"][0]["peerList"][0]["localAddr"] = request_param.form.get(
        "vprnlocalAddr")
    valuesFileData["vprn"][0]["bgp"]["groupList"][0]["peerList"][1]["peerIp"] = request_param.form.get("vprnpeerIp2")
    valuesFileData["vprn"][0]["bgp"]["groupList"][0]["peerList"][1]["localAddr"] = request_param.form.get(
        "vprnlocalAddr2")

    valuesFileData["vprn"][0]["bgp"]["groupList"][1]["name"] = request_param.form.get("grouplist2bgpname")
    valuesFileData["vprn"][0]["bgp"]["groupList"][1]["peerAs"] = int(request_param.form.get("grouplist2bgppeerAs"))
    valuesFileData["vprn"][0]["bgp"]["groupList"][1]["authKey"] = request_param.form.get("grouplist2bgpauthKey")
    valuesFileData["vprn"][0]["bgp"]["groupList"][1]["bgpExport"] = request_param.form.get("grouplist2bgpbgpExport")
    valuesFileData["vprn"][0]["bgp"]["groupList"][1]["peerList"][0]["peerIp"] = request_param.form.get(
        "grouplist2vprnpeerIp")
    valuesFileData["vprn"][0]["bgp"]["groupList"][1]["peerList"][0]["localAddr"] = request_param.form.get(
        "grouplist2vprnlocalAddr")
    valuesFileData["vprn"][0]["bgp"]["groupList"][1]["peerList"][1]["peerIp"] = request_param.form.get(
        "grouplist2vprnpeerIp2")
    valuesFileData["vprn"][0]["bgp"]["groupList"][1]["peerList"][1]["localAddr"] = request_param.form.get(
        "grouplist2vprnlocalAddr2")

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
