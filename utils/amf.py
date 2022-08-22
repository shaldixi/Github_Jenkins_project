from distutils.util import strtobool

def createTagsDictionary(request):
    tagsdic = dict()
    all = request.form.get("all")
    if all == None:
        all = "false"
    amms = request.form.get("amms")
    if amms == None:
        amms = "false"
    dbs = request.form.get("dbs")
    if dbs == None:
        dbs = "false"
    emms = request.form.get("emms")
    if emms == None:
        emms = "false"
    ipds = request.form.get("ipds")
    if ipds == None:
        ipds = "false"
    ipps = request.form.get("ipps")
    if ipps == None:
        ipps = "false"
    necc = request.form.get("necc")
    if necc == None:
        necc = "false"
    paps = request.form.get("paps")
    if paps == None:
        paps = "false"
    networkcrd = request.form.get("networkcrd")
    if networkcrd == None:
        networkcrd = "false"
    alms = request.form.get("alms")
    if alms == None:
        alms = "false"
    ctcs = request.form.get("ctcs")
    if ctcs == None:
        ctcs = "false"
    eems = request.form.get("eems")
    if eems == None:
        eems = "false"
    pvc = request.form.get("pvc")
    if pvc == None:
        pvc = "false"

    tagsdic['all'] = bool(strtobool(all))
    tagsdic['amms'] = bool(strtobool(amms))
    tagsdic['dbs'] = bool(strtobool(dbs))
    tagsdic['emms'] = bool(strtobool(emms))
    tagsdic['ipds'] = bool(strtobool(ipds))
    tagsdic['ipps'] = bool(strtobool(ipps))
    tagsdic['necc'] = bool(strtobool(necc))
    tagsdic['paps'] = bool(strtobool(paps))
    tagsdic['networkcrd'] = bool(strtobool(networkcrd))
    tagsdic['alms'] = bool(strtobool(alms))
    tagsdic['ctcs'] = bool(strtobool(ctcs))
    tagsdic['eems'] = bool(strtobool(eems))
    tagsdic['pvc'] = bool(strtobool(pvc))
    return tagsdic

def createGlobalSecretsDictionary(request):
    secretdic = dict()
    usersdic = dict()
    cmm_passwd = request.form["cmm_passwd"]
    cbamuser_passwd = request.form["cbamuser_passwd"]
    sam5620_passwd = request.form["sam5620_passwd"]
    cgw_passwd = request.form["cgw_passwd"]
    dcae_dfc_passwd = request.form["dcae_dfc_passwd"]
    rsp_passwd = request.form["rsp_passwd"]
    diagnostic_passwd = request.form["diagnostic_passwd"]
    trainee_passwd = request.form["trainee_passwd"]
    ca4mn_passwd = request.form["ca4mn_passwd"]
    cmmsecurity_passwd = request.form["cmmsecurity_passwd"]
    root_passwd = request.form["root_passwd"]
    userstempdic = dict()
    userstempdic['cmm_passwd'] = cmm_passwd
    userstempdic['cbamuser_passwd'] = cbamuser_passwd
    userstempdic['sam5620_passwd'] = sam5620_passwd
    userstempdic['cgw_passwd'] = cgw_passwd
    userstempdic['dcae_dfc_passwd'] = dcae_dfc_passwd
    userstempdic['rsp_passwd'] = rsp_passwd
    userstempdic['diagnostic_passwd'] = diagnostic_passwd
    userstempdic['trainee_passwd'] = trainee_passwd
    userstempdic['ca4mn_passwd'] = ca4mn_passwd
    userstempdic['cmmsecurity_passwd'] = cmmsecurity_passwd
    userstempdic['root_passwd'] = root_passwd
    usersdic['users'] = userstempdic
    secretdic['secrets'] = usersdic
    return secretdic

def createGlobalContainersDictionary(request, cmm_version, customer_name):
    containerdic = dict()
    ne_type = request.form["ne_type"]
    emms_amms_imageName = request.form["emms_amms_imageName"]
    emms_amms_cpu = request.form["emms_amms_cpu"]
    emms_amms_memory = request.form["emms_amms_memory"]
    emms_amms_initialDelaySeconds = request.form["emms_amms_initialDelaySeconds"]
    emms_amms_periodSeconds = request.form["emms_amms_periodSeconds"]
    containertempdic = dict()
    emms_ammsdic = dict()
    emms_ammsdic['imageName'] = emms_amms_imageName
    emms_ammsresourcesdic = dict()
    emms_ammsresourcesdic['cpu'] = int(emms_amms_cpu)
    emms_ammsresourcesdic['memory'] = emms_amms_memory
    emms_ammsdic['resources'] = emms_ammsresourcesdic
    emms_ammsnodeselectordic = dict()
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            emms_amms_region = request.form["emms_amms_region"]
            emms_ammsnodeselectordic['region'] = emms_amms_region
        elif customer_name == 'DISH':
            emms_amms_is_amf = request.form["emms_amms_is_amf"]
            emms_ammsnodeselectordic['is_amf'] = emms_amms_is_amf
    emms_ammsdic['nodeSelector'] = emms_ammsnodeselectordic
    emms_ammsdic['initialDelaySeconds'] = int(emms_amms_initialDelaySeconds)
    emms_ammsdic['periodSeconds'] = int(emms_amms_periodSeconds)
    containertempdic['emms_amms'] = emms_ammsdic
    dbs_imageName = request.form["dbs_imageName"]
    dbs_cpu = request.form["dbs_cpu"]
    dbs_memory = request.form["dbs_memory"]
    dbs_initialDelaySeconds = request.form["dbs_initialDelaySeconds"]
    dbs_periodSeconds = request.form["dbs_periodSeconds"]
    dbsdic = dict()
    dbsdic['imageName'] = dbs_imageName
    dbsresourcesdic = dict()
    dbsresourcesdic['cpu'] = int(dbs_cpu)
    dbsresourcesdic['memory'] = dbs_memory
    dbsdic['resources'] = dbsresourcesdic
    dbsnodeselectordic = dict()
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            dbs_region = request.form["dbs_region"]
            dbsnodeselectordic['region'] = dbs_region
        elif customer_name == 'DISH':
            dbs_is_amf = request.form["dbs_is_amf"]
            dbsnodeselectordic['is_amf'] = dbs_is_amf
    dbsdic['nodeSelector'] = dbsnodeselectordic
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            dbs_antiaffinity = request.form["dbs_antiaffinity"]
            if dbs_antiaffinity != '':
                dbsdic['antiaffinity'] = dbs_antiaffinity.split(",")
            else:
                dbsdic['antiaffinity'] = list(dbs_antiaffinity)
    dbsdic['initialDelaySeconds'] = int(dbs_initialDelaySeconds)
    dbsdic['periodSeconds'] = int(dbs_periodSeconds)
    containertempdic['dbs'] = dbsdic
    ipds_imageName = request.form["ipds_imageName"]
    ipds_cpu = request.form["ipds_cpu"]
    ipds_memory = request.form["ipds_memory"]
    ipds_initialDelaySeconds = request.form["ipds_initialDelaySeconds"]
    ipds_periodSeconds = request.form["ipds_periodSeconds"]
    ipds_antiaffinity = request.form["ipds_antiaffinity"]
    ipdsdic = dict()
    ipdsdic['imageName'] = ipds_imageName
    ipdsresourcesdic = dict()
    ipdsresourcesdic['cpu'] = int(ipds_cpu)
    ipdsresourcesdic['memory'] = ipds_memory
    ipdsdic['resources'] = ipdsresourcesdic
    ipdsnodeselectordic = dict()
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            ipds_region = request.form["ipds_region"]
            ipdsnodeselectordic['region'] = ipds_region
        elif customer_name == 'DISH':
            ipds_is_amf = request.form["ipds_is_amf"]
            ipdsnodeselectordic['is_amf'] = ipds_is_amf
    ipdsdic['nodeSelector'] = ipdsnodeselectordic
    if ipds_antiaffinity != '':
        ipdsdic['antiaffinity'] = ipds_antiaffinity.split(",")
    else:
        ipdsdic['antiaffinity'] = list(ipds_antiaffinity)
    ipdsdic['initialDelaySeconds'] = int(ipds_initialDelaySeconds)
    ipdsdic['periodSeconds'] = int(ipds_periodSeconds)
    containertempdic['ipds'] = ipdsdic
    necc_imageName = request.form["necc_imageName"]
    necc_cpu = request.form["necc_cpu"]
    necc_memory = request.form["necc_memory"]
    necc_pvc = request.form.get("necc_pvc")
    if necc_pvc == None:
        necc_pvc = "false"
    necc_initialDelaySeconds = request.form["necc_initialDelaySeconds"]
    necc_periodSeconds = request.form["necc_periodSeconds"]
    necc_antiaffinity = request.form["necc_antiaffinity"]
    neccdic = dict()
    neccdic['imageName'] = necc_imageName
    neccresourcesdic = dict()
    neccresourcesdic['cpu'] = int(necc_cpu)
    neccresourcesdic['memory'] = necc_memory
    neccdic['resources'] = neccresourcesdic
    neccnodeselectordic = dict()
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            necc_region = request.form["necc_region"]
            neccnodeselectordic['region'] = necc_region
        elif customer_name == 'DISH':
            necc_is_amf = request.form["necc_is_amf"]
            neccnodeselectordic['is_amf'] = necc_is_amf
    neccdic['nodeSelector'] = neccnodeselectordic
    neccdic['pvc'] = bool(strtobool(necc_pvc))
    if necc_antiaffinity != '':
        neccdic['antiaffinity'] = necc_antiaffinity.split(",")
    else:
        neccdic['antiaffinity'] = list(necc_antiaffinity)
    neccdic['initialDelaySeconds'] = int(necc_initialDelaySeconds)
    neccdic['periodSeconds'] = int(necc_periodSeconds)
    containertempdic['necc'] = neccdic
    if ne_type == 'qa' or ne_type == 'ta':
        ipps_imageName = request.form["ipps_imageName"]
        ipps_cpu = request.form["ipps_cpu"]
        ipps_memory = request.form["ipps_memory"]
        ipps_initialDelaySeconds = request.form["ipps_initialDelaySeconds"]
        ipps_periodSeconds = request.form["ipps_periodSeconds"]
        ippsdic = dict()
        ippsdic['imageName'] = ipps_imageName
        ippsresourcesdic = dict()
        ippsresourcesdic['cpu'] = int(ipps_cpu)
        ippsresourcesdic['memory'] = ipps_memory
        ippsdic['resources'] = ippsresourcesdic
        ippsnodeselectordic = dict()
        if cmm_version == '21M2':
            if customer_name == 'M1' or customer_name == 'Others':
                ipps_region = request.form["ipps_region"]
                ippsnodeselectordic['region'] = ipps_region
            elif customer_name == 'DISH':
                ipps_is_amf = request.form["ipps_is_amf"]
                ippsnodeselectordic['is_amf'] = ipps_is_amf
        ippsdic['nodeSelector'] = ippsnodeselectordic
        ippsdic['initialDelaySeconds'] = int(ipps_initialDelaySeconds)
        ippsdic['periodSeconds'] = int(ipps_periodSeconds)
        containertempdic['ipps'] = ippsdic
        paps_imageName = request.form["paps_imageName"]
        paps_cpu = request.form["paps_cpu"]
        paps_memory = request.form["paps_memory"]
        paps_initialDelaySeconds = request.form["paps_initialDelaySeconds"]
        paps_periodSeconds = request.form["paps_periodSeconds"]
        papsdic = dict()
        papsdic['imageName'] = paps_imageName
        papsresourcesdic = dict()
        papsresourcesdic['cpu'] = int(paps_cpu)
        papsresourcesdic['memory'] = paps_memory
        papsdic['resources'] = papsresourcesdic
        papsnodeselectordic = dict()
        if cmm_version == '21M2':
            if customer_name == 'M1' or customer_name == 'Others':
                paps_region = request.form["paps_region"]
                papsnodeselectordic['region'] = paps_region
            elif customer_name == 'DISH':
                paps_is_amf = request.form["paps_is_amf"]
                papsnodeselectordic['is_amf'] = paps_is_amf
        papsdic['nodeSelector'] = papsnodeselectordic
        papsdic['initialDelaySeconds'] = int(paps_initialDelaySeconds)
        papsdic['periodSeconds'] = int(paps_periodSeconds)
        containertempdic['paps'] = papsdic
    alarm_imageName = request.form["alarm_imageName"]
    alarm_cpu = request.form["alarm_cpu"]
    alarm_memory = request.form["alarm_memory"]
    alarm_initialDelaySeconds = request.form["alarm_initialDelaySeconds"]
    alarm_periodSeconds = request.form["alarm_periodSeconds"]
    alarmdic = dict()
    alarmdic['imageName'] = alarm_imageName
    alarmresourcesdic = dict()
    alarmresourcesdic['cpu'] = int(alarm_cpu)
    alarmresourcesdic['memory'] = alarm_memory
    alarmdic['resources'] = alarmresourcesdic
    alarmdic['initialDelaySeconds'] = int(alarm_initialDelaySeconds)
    alarmdic['periodSeconds'] = int(alarm_periodSeconds)
    containertempdic['alarm'] = alarmdic
    alms_imageName = request.form["alms_imageName"]
    alms_cpu = request.form["alms_cpu"]
    alms_memory = request.form["alms_memory"]
    alms_pvc = request.form.get("alms_pvc")
    if alms_pvc == None:
        alms_pvc = "false"
    alms_initialDelaySeconds = request.form["alms_initialDelaySeconds"]
    alms_periodSeconds = request.form["alms_periodSeconds"]
    almsdic = dict()
    almsdic['imageName'] = alms_imageName
    almsresourcesdic = dict()
    almsresourcesdic['cpu'] = int(alms_cpu)
    almsresourcesdic['memory'] = alms_memory
    almsdic['resources'] = almsresourcesdic
    almsnodeselectordic = dict()
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            alms_region = request.form["alms_region"]
            almsnodeselectordic['region'] = alms_region
        elif customer_name == 'DISH':
            alms_is_amf = request.form["alms_is_amf"]
            almsnodeselectordic['is_amf'] = alms_is_amf
    almsdic['nodeSelector'] = almsnodeselectordic
    almsdic['pvc'] = bool(strtobool(alms_pvc))
    almsdic['initialDelaySeconds'] = int(alms_initialDelaySeconds)
    almsdic['periodSeconds'] = int(alms_periodSeconds)
    containertempdic['alms'] = almsdic
    bsp_init_imageName = request.form["bsp_init_imageName"]
    bsp_init_cpu = request.form["bsp_init_cpu"]
    bsp_init_memory = request.form["bsp_init_memory"]
    bsp_initdic = dict()
    bsp_initdic['imageName'] = bsp_init_imageName
    bsp_initresourcesdic = dict()
    bsp_initresourcesdic['cpu'] = int(bsp_init_cpu)
    bsp_initresourcesdic['memory'] = bsp_init_memory
    bsp_initdic['resources'] = bsp_initresourcesdic
    containertempdic['bsp_init'] = bsp_initdic
    ctcs_imageName = request.form["ctcs_imageName"]
    ctcs_cpu = request.form["ctcs_cpu"]
    ctcs_memory = request.form["ctcs_memory"]
    ctcs_pvc = request.form.get("ctcs_pvc")
    if ctcs_pvc == None:
        ctcs_pvc = "false"
    ctcs_initialDelaySeconds = request.form["ctcs_initialDelaySeconds"]
    ctcs_periodSeconds = request.form["ctcs_periodSeconds"]
    ctcsdic = dict()
    ctcsdic['imageName'] = ctcs_imageName
    ctcsresourcesdic = dict()
    ctcsresourcesdic['cpu'] = int(ctcs_cpu)
    ctcsresourcesdic['memory'] = ctcs_memory
    ctcsdic['resources'] = ctcsresourcesdic
    ctcsnodeselectordic = dict()
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            ctcs_region = request.form["ctcs_region"]
            ctcsnodeselectordic['region'] = ctcs_region
        elif customer_name == 'DISH':
            ctcs_is_amf = request.form["ctcs_is_amf"]
            ctcsnodeselectordic['is_amf'] = ctcs_is_amf
    ctcsdic['nodeSelector'] = ctcsnodeselectordic
    ctcsdic['pvc'] = bool(strtobool(ctcs_pvc))
    ctcsdic['initialDelaySeconds'] = int(ctcs_initialDelaySeconds)
    ctcsdic['periodSeconds'] = int(ctcs_periodSeconds)
    containertempdic['ctcs'] = ctcsdic
    eems_imageName = request.form["eems_imageName"]
    eems_cpu = request.form["eems_cpu"]
    eems_memory = request.form["eems_memory"]
    eems_initialDelaySeconds = request.form["eems_initialDelaySeconds"]
    eems_periodSeconds = request.form["eems_periodSeconds"]
    eemsdic = dict()
    eemsdic['imageName'] = eems_imageName
    eemsresourcesdic = dict()
    eemsresourcesdic['cpu'] = int(eems_cpu)
    eemsresourcesdic['memory'] = eems_memory
    eemsdic['resources'] = eemsresourcesdic
    eemsnodeselectordic = dict()
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            eems_region = request.form["eems_region"]
            eemsnodeselectordic['region'] = eems_region
        elif customer_name == 'DISH':
            eems_is_amf = request.form["eems_is_amf"]
            eemsnodeselectordic['is_amf'] = eems_is_amf
    eemsdic['nodeSelector'] = eemsnodeselectordic
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            eems_antiaffinity = request.form["eems_antiaffinity"]
            if eems_antiaffinity != '':
                eemsdic['antiaffinity'] = eems_antiaffinity.split(",")
            else:
                eemsdic['antiaffinity'] = list(eems_antiaffinity)
    eemsdic['initialDelaySeconds'] = int(eems_initialDelaySeconds)
    eemsdic['periodSeconds'] = int(eems_periodSeconds)
    containertempdic['eems'] = eemsdic
    loglocal_imageName = request.form["loglocal_imageName"]
    loglocal_cpu = request.form["loglocal_cpu"]
    loglocal_memory = request.form["loglocal_memory"]
    loglocaldic = dict()
    loglocaldic['imageName'] = loglocal_imageName
    loglocalresourcesdic = dict()
    loglocalresourcesdic['cpu'] = int(loglocal_cpu)
    loglocalresourcesdic['memory'] = loglocal_memory
    loglocaldic['resources'] = loglocalresourcesdic
    containertempdic['loglocal'] = loglocaldic
    lxprofile_imageName = request.form["lxprofile_imageName"]
    lxprofile_cpu = request.form["lxprofile_cpu"]
    lxprofile_memory = request.form["lxprofile_memory"]
    lxprofiledic = dict()
    lxprofiledic['imageName'] = lxprofile_imageName
    lxprofileresourcesdic = dict()
    lxprofileresourcesdic['cpu'] = int(lxprofile_cpu)
    lxprofileresourcesdic['memory'] = lxprofile_memory
    lxprofiledic['resources'] = lxprofileresourcesdic
    containertempdic['lxprofile'] = lxprofiledic
    mmemon_imageName = request.form["mmemon_imageName"]
    mmemon_cpu = request.form["mmemon_cpu"]
    mmemon_memory = request.form["mmemon_memory"]
    mmemondic = dict()
    mmemondic['imageName'] = mmemon_imageName
    mmemonresourcesdic = dict()
    mmemonresourcesdic['cpu'] = int(mmemon_cpu)
    mmemonresourcesdic['memory'] = mmemon_memory
    mmemondic['resources'] = mmemonresourcesdic
    containertempdic['mmemon'] = mmemondic
    platservices_imageName = request.form["platservices_imageName"]
    platservices_cpu = request.form["platservices_cpu"]
    platservices_memory = request.form["platservices_memory"]
    platservicesdic = dict()
    platservicesdic['imageName'] = platservices_imageName
    platservicesresourcesdic = dict()
    platservicesresourcesdic['cpu'] = int(platservices_cpu)
    platservicesresourcesdic['memory'] = platservices_memory
    platservicesdic['resources'] = platservicesresourcesdic
    containertempdic['platservices'] = platservicesdic
    redis_imageName = request.form["redis_imageName"]
    redis_cpu = request.form["redis_cpu"]
    redis_memory = request.form["redis_memory"]
    redisdic = dict()
    redisdic['imageName'] = redis_imageName
    redisresourcesdic = dict()
    redisresourcesdic['cpu'] = int(redis_cpu)
    redisresourcesdic['memory'] = redis_memory
    redisdic['resources'] = redisresourcesdic
    containertempdic['redis'] = redisdic
    containerdic['containers'] = containertempdic
    return containerdic

def createGlobalProvisioningDictionary(request):
    provisioningdic = dict()
    provisioningtempdic = dict()
    network_name = request.form["network_name"]
    network_short_name = request.form["network_short_name"]
    network_short_name = request.form["network_short_name"]
    prometheusGWIp = request.form["prometheusGWIp"]
    prometheusGWPort = request.form["prometheusGWPort"]
    amfregionid = request.form["amfregionid"]
    amfsetid = request.form["amfsetid"]
    amfpointer = request.form["amfpointer"]
    plmn_timezone = request.form["plmn_timezone"]
    mcc = request.form["mcc"]
    mnc = request.form["mnc"]
    amfIdLabels = request.form["amfIdLabels"]
    guamiName = request.form["guamiName"]
    start_supi1 = request.form["start_supi1"]
    end_supi1 = request.form["end_supi1"]
    dnn1 = request.form["dnn1"]
    dnn2 = request.form["dnn2"]
    dnn3 = request.form["dnn3"]
    dnn4 = request.form["dnn4"]
    dnn5 = request.form["dnn5"]
    dnn6 = request.form["dnn6"]
    dnn7 = request.form["dnn7"]
    sst1 = request.form["sst1"]
    sd1 = request.form["sd1"]
    sst2 = request.form["sst2"]
    sd2 = request.form["sd2"]
    sst3 = request.form["sst3"]
    sd3 = request.form["sd3"]
    sst4 = request.form["sst4"]
    sd4 = request.form["sd4"]
    tac = request.form["tac"]
    provisioningtempdic['network_name'] = network_name
    provisioningtempdic['network_short_name'] = network_short_name
    provisioningtempdic['prometheusGWIp'] = prometheusGWIp
    provisioningtempdic['prometheusGWPort'] = int(prometheusGWPort)
    provisioningtempdic['amfregionid'] = int(amfregionid)
    provisioningtempdic['amfsetid'] = int(amfsetid)
    provisioningtempdic['amfpointer'] = int(amfpointer)
    provisioningtempdic['plmn_timezone'] = plmn_timezone
    provisioningtempdic['mcc'] = int(mcc)
    provisioningtempdic['mnc'] = int(mnc)
    provisioningtempdic['amfIdLabels'] = amfIdLabels
    provisioningtempdic['guamiName'] = guamiName
    provisioningtempdic['start_supi1'] = start_supi1
    provisioningtempdic['end_supi1'] = end_supi1
    provisioningtempdic['dnn1'] = dnn1
    provisioningtempdic['dnn2'] = dnn2
    provisioningtempdic['dnn3'] = dnn3
    provisioningtempdic['dnn4'] = dnn4
    provisioningtempdic['dnn5'] = dnn5
    provisioningtempdic['dnn6'] = dnn6
    provisioningtempdic['dnn7'] = dnn7
    provisioningtempdic['sst1'] = int(sst1)
    provisioningtempdic['sd1'] = sd1
    provisioningtempdic['sst2'] = int(sst2)
    provisioningtempdic['sd2'] = sd2
    provisioningtempdic['sst3'] = int(sst3)
    provisioningtempdic['sd3'] = sd3
    provisioningtempdic['sst4'] = int(sst4)
    provisioningtempdic['sd4'] = sd4
    provisioningtempdic['tac'] = [int(i) for i in tac.split(",")]
    provisioningipv4dic = dict()
    provisioningipv4dic['n2_ip'] = '10.141.49.132'
    provisioningipv4dic['n8_ip'] = '10.141.49.4'
    provisioningipv4dic['n11_ip'] = '10.141.49.5'
    provisioningipv4dic['n12_ip'] = '10.141.49.6'
    provisioningipv4dic['n14_ip'] = '10.141.49.7'
    provisioningipv4dic['n15_ip'] = '10.141.49.8'
    provisioningipv4dic['n17_ip'] = '10.141.49.9'
    provisioningipv4dic['n22_ip'] = '10.141.49.10'
    provisioningipv4dic['n20_ip'] = '10.141.49.11'
    provisioningipv4dic['n26_ip'] = '10.141.49.12'
    provisioningipv4dic['nnrf_ip'] = '10.141.49.13'
    provisioningipv4dic['nsms_ip'] = '10.141.49.14'
    provisioningipv4dic['amf_svc_default_ip'] = '10.141.49.15'
    provisioningipv4dic['amf_svc_loc_ip'] = '10.141.49.16'
    provisioningipv4dic['amf_svc_com_ip'] = '10.141.49.17'
    provisioningipv4dic['amf_svc_ee_ip'] = '10.141.49.18'
    provisioningipv4dic['amf_svc_mt_ip'] = '10.141.49.19'
    provisioningipv4dic['nfy_eir_ip'] = '10.141.49.20'
    provisioningipv4dic['nfy_amf_ip'] = '10.141.49.21'
    provisioningipv4dic['nfy_ausf_ip'] = '10.141.49.22'
    provisioningipv4dic['nfy_nrf_ip'] = '10.141.49.23'
    provisioningipv4dic['nfy_nssf_ip'] = '10.141.49.24'
    provisioningipv4dic['nfy_pcf_ip'] = '10.141.49.25'
    provisioningipv4dic['nfy_smf_ip'] = '10.141.49.26'
    provisioningipv4dic['nfy_udm_ip'] = '10.141.49.27'
    provisioningipv4dic['nfy_smsf_ip'] = '10.141.49.28'
    provisioningipv4dic['nfy_cbcf_ip'] = '10.141.49.29'
    provisioningipv4dic['Nlmf_ip'] = '10.141.49.30'
    provisioningipv4dic['Ngmlc_ip'] = '10.141.49.31'
    provisioningipv4dic['NfyLMF_ip'] = '10.141.49.32'
    provisioningipv4dic['NfyGMLC_ip'] = '10.141.49.33'
    provisioningtempdic['ipv4'] = provisioningipv4dic
    provisioningipv6dic = dict()
    provisioningipv6dic['n2_ip'] = '2605:c540:8020:300d::4'
    provisioningipv6dic['n8_ip'] = '2605:c540:8020:300b::4'
    provisioningipv6dic['n11_ip'] = '2605:c540:8020:300b::5'
    provisioningipv6dic['n12_ip'] = '2605:c540:8020:300b::6'
    provisioningipv6dic['n14_ip'] = '2605:c540:8020:300b::7'
    provisioningipv6dic['n15_ip'] = '2605:c540:8020:300b::8'
    provisioningipv6dic['n17_ip'] = '2605:c540:8020:300b::9'
    provisioningipv6dic['n22_ip'] = '2605:c540:8020:300b::10'
    provisioningipv6dic['n26_ip'] = '2605:c540:8020:300b::11'
    provisioningipv6dic['nnrf_ip'] = '2605:c540:8020:300b::12'
    provisioningipv6dic['nsms_ip'] = '2605:c540:8020:300b::13'
    provisioningipv6dic['amf_svc_default_ip'] = '2605:c540:8020:300b::14'
    provisioningipv6dic['amf_svc_loc_ip'] = '2605:c540:8020:300b::15'
    provisioningipv6dic['amf_svc_com_ip'] = '2605:c540:8020:300b::16'
    provisioningipv6dic['amf_svc_ee_ip'] = '2605:c540:8020:300b::17'
    provisioningipv6dic['amf_svc_mt_ip'] = '2605:c540:8020:300b::18'
    provisioningipv6dic['nfy_eir_ip'] = '2605:c540:8020:300b::19'
    provisioningipv6dic['nfy_amf_ip'] = '2605:c540:8020:300b::20'
    provisioningipv6dic['nfy_ausf_ip'] = '2605:c540:8020:300b::21'
    provisioningipv6dic['nfy_nrf_ip'] = '2605:c540:8020:300b::22'
    provisioningipv6dic['nfy_nssf_ip'] = '2605:c540:8020:300b::23'
    provisioningipv6dic['nfy_pcf_ip'] = '2605:c540:8020:300b::24'
    provisioningipv6dic['nfy_smf_ip'] = '2605:c540:8020:300b::25'
    provisioningipv6dic['nfy_udm_ip'] = '2605:c540:8020:300b::26'
    provisioningipv6dic['n20_ip'] = '2605:c540:8020:300b::27'
    provisioningipv6dic['nfy_smsf_ip'] = '2605:c540:8020:300b::28'
    provisioningipv6dic['nfy_cbcf_ip'] = '2605:c540:8020:300b::29'
    provisioningipv6dic['Nlmf_ip'] = '2605:c540:8020:300b::30'
    provisioningipv6dic['Ngmlc_ip'] = '2605:c540:8020:300b::31'
    provisioningipv6dic['NfyLMF_ip'] = '2605:c540:8020:300b::32'
    provisioningipv6dic['NfyGMLC_ip'] = '2605:c540:8020:300b::33'
    provisioningtempdic['ipv6'] = provisioningipv6dic
    dns_ipds_ip1 = request.form["dns_ipds_ip1"]
    dns_ipds_ip2 = request.form["dns_ipds_ip2"]
    primary_dns_ip = request.form["primary_dns_ip"]
    secondary_dns_ip = request.form["secondary_dns_ip"]
    provisioningtempdic['dns_ipds_ip1'] = dns_ipds_ip1
    provisioningtempdic['dns_ipds_ip2'] = dns_ipds_ip2
    provisioningtempdic['primary_dns_ip'] = primary_dns_ip
    provisioningtempdic['secondary_dns_ip'] = secondary_dns_ip
    nrf_endpoint_ip = request.form["nrf_endpoint_ip"]
    nrf_endpoint_port = request.form["nrf_endpoint_port"]
    nssf_endpoint_ip = request.form["nssf_endpoint_ip"]
    nssf_endpoint_port = request.form["nssf_endpoint_port"]
    provisioningtempdic['nrf_endpoint_ip'] = nrf_endpoint_ip
    provisioningtempdic['nrf_endpoint_port'] = int(nrf_endpoint_port)
    provisioningtempdic['nssf_endpoint_ip'] = nssf_endpoint_ip
    provisioningtempdic['nssf_endpoint_port'] = int(nssf_endpoint_port)
    gmlc1_endpoint_ip = request.form["gmlc1_endpoint_ip"]
    gmlc1_endpoint_port = request.form["gmlc1_endpoint_port"]
    gmlc2_endpoint_ip = request.form["gmlc2_endpoint_ip"]
    gmlc2_endpoint_port = request.form["gmlc2_endpoint_port"]
    provisioningtempdic['gmlc1_endpoint_ip'] = gmlc1_endpoint_ip
    provisioningtempdic['gmlc1_endpoint_port'] = int(gmlc1_endpoint_port)
    provisioningtempdic['gmlc2_endpoint_ip'] = gmlc2_endpoint_ip
    provisioningtempdic['gmlc2_endpoint_port'] = int(gmlc2_endpoint_port)
    cbcf1_endpoint_ip = request.form["cbcf1_endpoint_ip"]
    cbcf1_endpoint_port = request.form["cbcf1_endpoint_port"]
    cbcf2_endpoint_ip = request.form["cbcf2_endpoint_ip"]
    cbcf2_endpoint_port = request.form["cbcf2_endpoint_port"]
    provisioningtempdic['cbcf1_endpoint_ip'] = cbcf1_endpoint_ip
    provisioningtempdic['cbcf1_endpoint_port'] = int(cbcf1_endpoint_port)
    provisioningtempdic['cbcf2_endpoint_ip'] = cbcf2_endpoint_ip
    provisioningtempdic['cbcf2_endpoint_port'] = int(cbcf2_endpoint_port)
    provisioningdic['provisioning'] = provisioningtempdic
    return provisioningdic

def createGlobalExtSubnetIpDictionary(request):
    extsubnetdic = dict()
    extsubnetipdic = dict()
    extipdsdiclist = []
    ext_count = request.form["ext_count"]
    for i in range(int(ext_count)):
        i = i + 1
        ext_subnet_name = request.form["ext_subnet_name_"+ str(i)]
        ext_subnet_type = request.form["ext_type_"+ str(i)]
        ext_subnet_cidr = request.form["ext_cidr_"+ str(i)]
        ext_subnet_gateway = request.form["ext_gw_"+ str(i)]
        ext_subnet_ip = request.form["ext_ip_"+ str(i)]
        ext_subnet_interface = request.form["ext_interface_"+ str(i)]
        ext_subnet_host_interface = request.form["ext_host_interface_"+ str(i)]
        try:
            ipv6Option = request.form.get("ipv6Option_" + str(i))
            if ipv6Option == None:
                ipv6Option = 'N'
        except:
            ipv6Option = 'N'
        if ipv6Option == 'Y':
            ext_subnet_type_ipv6 = request.form["ext_type_ipv6_" + str(i)]
            ext_subnet_cidr_ipv6 = request.form["ext_cidr_ipv6_" + str(i)]
            ext_subnet_gateway_ipv6 = request.form["ext_gw_ipv6_" + str(i)]
            ext_subnet_ip_ipv6 = request.form["ext_ip_ipv6_" + str(i)]
        extipdstempdic = dict()
        extipdstempdic['name'] = ext_subnet_name
        if ext_subnet_type is not None and ipv6Option == 'Y':
            extipdstempdic['type'] = "dual"
        elif ext_subnet_type is not None and ipv6Option == 'N':
            extipdstempdic['type'] = ext_subnet_type
        elif ext_subnet_type is None and ipv6Option == 'Y':
            extipdstempdic['type'] = ext_subnet_type_ipv6
        extipdstempdic['host_interface'] = ext_subnet_host_interface
        extipdstempdic['interface'] = ext_subnet_interface
        extipdstempdic['vlan'] = ''
        ipv4dic = dict()
        ipv4dic['cidr'] = ext_subnet_cidr
        ipv4dic['gw'] = ext_subnet_gateway
        ipv4dic['ip'] = ext_subnet_ip.split(",")
        extipdstempdic['ipv4'] = ipv4dic
        if ipv6Option == 'Y':
            ipv6dic = dict()
            ipv6dic['cidr'] = ext_subnet_cidr_ipv6
            ipv6dic['gw'] = ext_subnet_gateway_ipv6
            ipv6dic['ip'] = ext_subnet_ip_ipv6.split(",")
            extipdstempdic['ipv6'] = ipv6dic
        extipdsdiclist.append(extipdstempdic)
    extsubnetipdic['ipds'] = extipdsdiclist
    extsubnetdic['external_cni'] = 'ipvlan'
    extsubnetdic['external'] = extsubnetipdic
    return extsubnetdic

def createGlobalBasicDictionary(request, cmm_version, customer_name):
    globalbasicdic = dict()
    env_name = request.form["env_name"]
    k8s_apiserver_endpoints = request.form["k8s_apiserver_endpoints"]
    k8s_apiserver_port = request.form["k8s_apiserver_port"]
    ne_type = request.form["ne_type"]
    cmm_uuid = request.form["cmm_uuid"]
    necccount = request.form["necccount"]
    storageclass = request.form["storageclass"]
    timezone = request.form["timezone"]
    disable_apparmor = request.form.get("disable_apparmor")
    if disable_apparmor == None:
        disable_apparmor = "false"
    openshift = request.form.get("openshift")
    if openshift == None:
        openshift = "false"
    bcmt = request.form.get("bcmt")
    if bcmt == None:
        bcmt = "false"
    rbac_resourcename = request.form["rbac_resourcename"]
    cluster_cidr = request.form["cluster_cidr"]
    amms_minReplicas = request.form["amms_minReplicas"]
    amms_maxReplicas = request.form["amms_maxReplicas"]
    amms_cpu_utilization = request.form["amms_cpu_utilization"]
    amms_memory_utilization = request.form["amms_memory_utilization"]
    amms_ue_utilization = request.form["amms_ue_utilization"]
    emms_minReplicas = request.form["emms_minReplicas"]
    emms_maxReplicas = request.form["emms_maxReplicas"]
    emms_cpu_utilization = request.form["emms_cpu_utilization"]
    emms_memory_utilization = request.form["emms_memory_utilization"]
    emms_ue_utilization = request.form["emms_ue_utilization"]
    dbs_minReplicas = request.form["dbs_minReplicas"]
    dbs_maxReplicas = request.form["dbs_maxReplicas"]
    dbs_cpu_utilization = request.form["dbs_cpu_utilization"]
    dbs_memory_utilization = request.form["dbs_memory_utilization"]
    ipds_minReplicas = request.form["ipds_minReplicas"]
    ipds_maxReplicas = request.form["ipds_maxReplicas"]
    ipds_cpu_utilization = request.form["ipds_cpu_utilization"]
    alms_minReplicas = request.form["alms_minReplicas"]
    alms_maxReplicas = request.form["alms_maxReplicas"]
    ctcs_minReplicas = request.form["ctcs_minReplicas"]
    ctcs_maxReplicas = request.form["ctcs_maxReplicas"]
    eems_minReplicas = request.form["eems_minReplicas"]
    eems_maxReplicas = request.form["eems_maxReplicas"]
    eems_ue_utilization = request.form["eems_ue_utilization"]
    kubeDNS_ip = request.form["kubeDNS_ip"]
    permission = request.form["permission"]
    app = request.form["app"]
    sbi_net_container_native = request.form.get("sbi_net_container_native")
    if sbi_net_container_native == None:
        sbi_net_container_native = "false"
    pvc_hostpath_prefix = request.form["pvc_hostpath_prefix"]
    skipNeccPvcCleanupJob = request.form.get("skipNeccPvcCleanupJob")
    if skipNeccPvcCleanupJob == None:
        skipNeccPvcCleanupJob = "false"
    dbs_duplex = request.form.get("dbs_duplex")
    if dbs_duplex == None:
        dbs_duplex = "false"
    pcmd_pvc = request.form["pcmd_pvc"]
    perf_pvc = request.form["perf_pvc"]
    logs_pvc = request.form["logs_pvc"]
    kafka_pvc = request.form["kafka_pvc"]
    influx_pvc = request.form["influx_pvc"]
    redis_pvc = request.form["redis_pvc"]
    charging_pvc = request.form["charging_pvc"]
    pm_pvc = request.form["pm_pvc"]
    shared_pvc = request.form["shared_pvc"]
    store_pvc = request.form["store_pvc"]
    mariadb_pvc = request.form["mariadb_pvc"]

    globalbasicdic['env_name'] = env_name
    globalbasicdic['k8s_apiserver_endpoints'] = k8s_apiserver_endpoints.split(",")
    globalbasicdic['k8s_apiserver_port'] = int(k8s_apiserver_port)
    globalbasicdic['env_separator'] = '-'
    globalbasicdic['ne_type'] = ne_type
    globalbasicdic['cmm_uuid'] = cmm_uuid
    globalbasicdic['necccount'] = int(necccount)
    globalbasicdic['storageclass'] = storageclass
    globalbasicdic['timezone'] = timezone
    globalbasicdic['disable_apparmor'] = bool(strtobool(disable_apparmor))
    globalbasicdic['rbac_resourcename'] = rbac_resourcename
    globalbasicdic['openshift'] = bool(strtobool(openshift))
    globalbasicdic['bcmt'] = bool(strtobool(bcmt))
    if cmm_version == '21M2':
        if customer_name == 'DISH':
            disable_hpa = request.form.get("disable_hpa")
            if disable_hpa == None:
                disable_hpa = "false"
            necc_stdout_logging = request.form.get("necc_stdout_logging")
            if necc_stdout_logging == None:
                necc_stdout_logging = "false"
            necc_stdout_logs = request.form["necc_stdout_logs"]
            multi_container = request.form.get("multi_container")
            if multi_container == None:
                multi_container = "false"
            alms_multi_container = request.form.get("alms_multi_container")
            if alms_multi_container == None:
                alms_multi_container = "false"
            ctcs_multi_container = request.form.get("ctcs_multi_container")
            if ctcs_multi_container == None:
                ctcs_multi_container = "false"
            eems_multi_container = request.form.get("eems_multi_container")
            if eems_multi_container == None:
                eems_multi_container = "false"
            globalbasicdic['disable_hpa'] = bool(strtobool(disable_hpa))
            globalbasicdic['necc_stdout_logging'] = bool(strtobool(necc_stdout_logging))
            globalbasicdic['necc_stdout_logs'] = necc_stdout_logs.split(",")
            globalbasicdic['multi_container'] = bool(strtobool(multi_container))
            globalbasicdic['alms_multi_container'] = bool(strtobool(alms_multi_container))
            globalbasicdic['ctcs_multi_container'] = bool(strtobool(ctcs_multi_container))
            globalbasicdic['eems_multi_container'] = bool(strtobool(eems_multi_container))
    globalbasicdic['cluster_cidr'] = list(cluster_cidr)
    scaledic = dict()
    ammsdic =dict()
    ammsdic['minReplicas'] = int(amms_minReplicas)
    ammsdic['maxReplicas'] = int(amms_maxReplicas)
    ammsdic['cpu_utilization'] = int(amms_cpu_utilization)
    ammsdic['memory_utilization'] = int(amms_memory_utilization)
    ammsdic['ue_utilization'] = int(amms_ue_utilization)
    scaledic['amms'] = ammsdic
    dbsdic = dict()
    dbsdic['minReplicas'] = int(dbs_minReplicas)
    dbsdic['maxReplicas'] = int(dbs_maxReplicas)
    dbsdic['cpu_utilization'] = int(dbs_cpu_utilization)
    dbsdic['memory_utilization'] = int(dbs_memory_utilization)
    scaledic['dbs'] = dbsdic
    if cmm_version == '21M2':
        if customer_name == 'DISH':
            emmsdic = dict()
            emmsdic['minReplicas'] = int(emms_minReplicas)
            emmsdic['maxReplicas'] = int(emms_maxReplicas)
            emmsdic['cpu_utilization'] = int(emms_cpu_utilization)
            emmsdic['memory_utilization'] = int(emms_memory_utilization)
            emmsdic['ue_utilization'] = int(emms_ue_utilization)
            scaledic['emms'] = emmsdic
    ipdsdic = dict()
    ipdsdic['minReplicas'] = int(ipds_minReplicas)
    ipdsdic['maxReplicas'] = int(ipds_maxReplicas)
    ipdsdic['cpu_utilization'] = int(ipds_cpu_utilization)
    scaledic['ipds'] = ipdsdic
    if ne_type == 'qa' or ne_type == 'ta':
        ipps_minReplicas = request.form["ipps_minReplicas"]
        ipps_maxReplicas = request.form["ipps_maxReplicas"]
        ipps_cpu_utilization = request.form["ipps_cpu_utilization"]
        paps_minReplicas = request.form["paps_minReplicas"]
        paps_maxReplicas = request.form["paps_maxReplicas"]
        paps_cpu_utilization = request.form["paps_cpu_utilization"]
        ippsdic = dict()
        ippsdic['minReplicas'] = int(ipps_minReplicas)
        ippsdic['maxReplicas'] = int(ipps_maxReplicas)
        ippsdic['cpu_utilization'] = int(ipps_cpu_utilization)
        scaledic['ipps'] = ippsdic
        papsdic = dict()
        papsdic['minReplicas'] = int(paps_minReplicas)
        papsdic['maxReplicas'] = int(paps_maxReplicas)
        papsdic['cpu_utilization'] = int(paps_cpu_utilization)
        scaledic['paps'] = papsdic
    almsdic = dict()
    almsdic['minReplicas'] = int(alms_minReplicas)
    almsdic['maxReplicas'] = int(alms_maxReplicas)
    scaledic['alms'] = almsdic
    ctcsdic = dict()
    ctcsdic['minReplicas'] = int(ctcs_minReplicas)
    ctcsdic['maxReplicas'] = int(ctcs_maxReplicas)
    scaledic['ctcs'] = ctcsdic
    eemsdic = dict()
    eemsdic['minReplicas'] = int(eems_minReplicas)
    eemsdic['maxReplicas'] = int(eems_maxReplicas)
    eemsdic['ue_utilization'] = int(eems_ue_utilization)
    scaledic['eems'] = eemsdic
    globalbasicdic['scale'] = scaledic
    kubeDNSdic = dict()
    kubeDNSdic['ip'] = kubeDNS_ip
    globalbasicdic['kubeDNS'] = kubeDNSdic
    prometheusdic = dict()
    namespaceLabeldic = dict()
    namespaceLabeldic['permission'] = permission
    podLabeldic = dict()
    podLabeldic['app'] = app
    prometheusdic['namespaceLabel'] = namespaceLabeldic
    prometheusdic['podLabel'] = podLabeldic
    globalbasicdic['prometheus'] = prometheusdic
    globalbasicdic['sbi_net_container_native'] = bool(strtobool(sbi_net_container_native))
    if cmm_version == '21M2':
        if customer_name == 'M1' or customer_name == 'Others':
            sbi_net_container_lb = request.form["sbi_net_container_lb"]
            globalbasicdic['sbi_net_container_lb'] = sbi_net_container_lb
            if sbi_net_container_lb == 'istio':
                istiodic = dict()
                createGateway = request.form.get("createGateway")
                if createGateway == None:
                    createGateway = "false"
                istiodic['createGateway'] = bool(strtobool(createGateway))
                gateways = request.form["gateways"]
                privateKey = request.form["privateKey"]
                serverCertificate = request.form["serverCertificate"]
                istiodic['gateways'] = gateways.split(",")
                istiodic['privateKey'] = privateKey
                istiodic['serverCertificate'] = serverCertificate
                globalbasicdic['istio'] = istiodic
            elif sbi_net_container_lb == 'traefik':
                traefikdic = dict()
                entryPoints = request.form["entryPoints"]
                traefikdic['entryPoints'] = entryPoints.split(",")
                globalbasicdic['traefik'] = traefikdic
    globalbasicdic['pvc_hostpath_prefix'] = pvc_hostpath_prefix
    globalbasicdic['skipNeccPvcCleanupJob'] = bool(strtobool(skipNeccPvcCleanupJob))
    globalbasicdic['dbs_duplex'] = bool(strtobool(dbs_duplex))
    ctcs_redis_pvc = request.form["ctcs_redis_pvc"]
    alms_redis_pvc = request.form["alms_redis_pvc"]
    ctcs_redis_dic = dict()
    ctcs_redis_dic['redis_pvc'] = ctcs_redis_pvc
    globalbasicdic['ctcsvolumes'] = ctcs_redis_dic
    alms_redis_dic = dict()
    alms_redis_dic['redis_pvc'] = alms_redis_pvc
    globalbasicdic['almsvolumes'] = alms_redis_dic
    neccvolumesdic = dict()
    neccvolumesdic['pcmd_pvc'] = pcmd_pvc
    neccvolumesdic['perf_pvc'] = perf_pvc
    neccvolumesdic['logs_pvc'] = logs_pvc
    neccvolumesdic['kafka_pvc'] = kafka_pvc
    neccvolumesdic['influx_pvc'] = influx_pvc
    neccvolumesdic['redis_pvc'] = redis_pvc
    neccvolumesdic['charging_pvc'] = charging_pvc
    neccvolumesdic['pm_pvc'] = pm_pvc
    neccvolumesdic['shared_pvc'] = shared_pvc
    neccvolumesdic['store_pvc'] = store_pvc
    neccvolumesdic['mariadb_pvc'] = mariadb_pvc
    globalbasicdic['neccvolumes'] = neccvolumesdic
    return globalbasicdic

def createGlobalOamIpDictionary(request):
    oamdic = dict()
    type = request.form["type"]
    ipv4dic = dict()
    ip = request.form["ip"]
    floating_ip = request.form["floating_ip"]
    cidr = request.form["cidr"]
    gw = request.form["gw"]
    interface = request.form["interface"]
    host_interface = request.form["host_interface"]
    ipv4dic['ip'] = ip.split(",")
    ipv4dic['floating_ip'] = floating_ip
    ipv4dic['cidr'] = cidr
    ipv4dic['gw'] = gw
    oamdictemp = dict()
    oamdictemp['type'] = type
    oamdictemp['ipv4'] = ipv4dic
    oamdictemp['interface'] = interface
    oamdictemp['host_interface'] = host_interface
    oamdic['oam'] = oamdictemp
    return oamdic

def createGlobalalmsIpDictionary(request):
    almsdic = dict()
    type = request.form["alms_type"]
    ipv4dic = dict()
    ip = request.form["alms_ip"]
    floating_ip = request.form["alms_floating_ip"]
    cidr = request.form["alms_cidr"]
    gw = request.form["alms_gw"]
    interface = request.form["alms_interface"]
    host_interface = request.form["alms_host_interface"]
    ipv4dic['ip'] = ip.split(",")
    ipv4dic['floating_ip'] = floating_ip
    ipv4dic['cidr'] = cidr
    ipv4dic['gw'] = gw
    almsdictemp = dict()
    almsdictemp['type'] = type
    almsdictemp['ipv4'] = ipv4dic
    almsdictemp['interface'] = interface
    almsdictemp['host_interface'] = host_interface
    almsdic['alms'] = almsdictemp
    return almsdic

def createCmmConfigMapDictionary(request):
    cmmconfigmapdic = dict()
    security_level = request.form["security_level"]
    ipds_env_multi = request.form.get("ipds_env_multi")
    if ipds_env_multi == None:
        ipds_env_multi = "false"
    cmm_env_l3ns = request.form.get("cmm_env_l3ns")
    if cmm_env_l3ns == None:
        cmm_env_l3ns = "false"
    cmmconfigmapdic['security_level'] = int(security_level)
    cmmconfigmapdic['ipds_env_multi'] = bool(strtobool(ipds_env_multi))
    cmmconfigmapdic['cmm_env_l3ns'] = bool(strtobool(cmm_env_l3ns))
    external_auth_support = request.form.get("external_auth_support")
    if external_auth_support == None:
        external_auth_support = "false"
    cmmconfigmapdic['external_auth_support'] = bool(strtobool(external_auth_support))
    return cmmconfigmapdic
