from distutils.util import strtobool

def createNRDImageDictionary(request):
    nrdimagedic = dict()
    imagetempdic = dict()
    image_registry = request.form['image_registry']
    image_repository = request.form['image_repository']
    image_tag = request.form['image_tag']
    image_pullPolicy = request.form['image_pullPolicy']
    debug = request.form.get("debug")
    if debug == None:
        debug = "false"
    imagetempdic['registry'] = image_registry
    imagetempdic['repository'] = image_repository
    imagetempdic['tag'] = image_tag
    imagetempdic['pullPolicy'] = image_pullPolicy
    imagetempdic['debug'] = bool(strtobool(debug))
    nrdimagedic['image'] = imagetempdic
    nrdimagetempdic = dict()
    nrd_image_registry = request.form['nrd_image_registry']
    nrd_image_repository = request.form['nrd_image_repository']
    nrd_image_tag = request.form['nrd_image_tag']
    nrd_image_pullPolicy = request.form['nrd_image_pullPolicy']
    nrdimagetempdic['registry'] = nrd_image_registry
    nrdimagetempdic['repository'] = nrd_image_repository
    nrdimagetempdic['tag'] = nrd_image_tag
    nrdimagetempdic['pullPolicy'] = nrd_image_pullPolicy
    nrdimagedic['nrdimage'] = nrdimagetempdic
    return nrdimagedic

def createNRDBasicDictionary(request):
    nrdbasicdic = dict()
    servicedic = dict()
    type = request.form['type']
    port = request.form['port']
    servicedic['type'] = type
    servicedic['port'] = int(port)
    nrdbasicdic['service'] = servicedic
    serviceAccountdic = dict()
    create = request.form.get("create")
    if create == None:
        create = "false"
    serviceAccountdic['create'] = bool(strtobool(create))
    nrdbasicdic['serviceAccount'] = serviceAccountdic
    rbacdic = dict()
    rbac_create = request.form.get("rbac_create")
    if rbac_create == None:
        rbac_create = "false"
    rbacdic['create'] = bool(strtobool(rbac_create))
    nrdbasicdic['rbac'] = rbacdic
    securityContextdic = dict()
    enable = request.form.get("enable")
    if enable == None:
        enable = "false"
    securityContextdic['enable'] = bool(strtobool(enable))
    dbdic =dict()
    runAsUser = request.form['runAsUser']
    fsGroup = request.form['fsGroup']
    runAsNonRoot = request.form.get("runAsNonRoot")
    if runAsNonRoot == None:
        runAsNonRoot = "false"
    dbdic['runAsUser'] = int(runAsUser)
    dbdic['fsGroup'] = int(fsGroup)
    dbdic['runAsNonRoot'] = bool(strtobool(runAsNonRoot))
    poddic = dict()
    poddic['db'] = dbdic
    securityContextdic['pod'] = poddic
    nrdbasicdic['securityContext'] = securityContextdic
    rootuserdic = dict()
    password = request.form['password']
    forcePassword = request.form.get("forcePassword")
    if forcePassword == None:
        forcePassword = "false"
    rootuserdic['password'] = password
    rootuserdic['forcePassword'] = bool(strtobool(forcePassword))
    nrdbasicdic['rootUser'] = rootuserdic
    dbuserdic = dict()
    db_user = request.form['db_user']
    db_password = request.form['db_password']
    db_name = request.form['db_name']
    db_forcePassword = request.form.get("db_forcePassword")
    if db_forcePassword == None:
        db_forcePassword = "false"
    dbuserdic['user'] = db_user
    dbuserdic['password'] = db_password
    dbuserdic['name'] = db_name
    dbuserdic['forcePassword'] = bool(strtobool(db_forcePassword))
    nrdbasicdic['db'] = dbuserdic
    replicationuserdic = dict()
    replication_enabled = request.form.get("replication_enabled")
    if replication_enabled == None:
        replication_enabled = "false"
    replication_user = request.form['replication_user']
    replication_password = request.form['replication_password']
    replication_forcePassword = request.form.get("replication_forcePassword")
    if replication_forcePassword == None:
        replication_forcePassword = "false"
    replicationuserdic['enabled'] = bool(strtobool(replication_enabled))
    replicationuserdic['user'] = replication_user
    replicationuserdic['password'] = replication_password
    replicationuserdic['forcePassword'] = bool(strtobool(replication_forcePassword))
    nrdbasicdic['replication'] = replicationuserdic
    return nrdbasicdic

def createMasterDictionary(request):
    masterdic = dict()
    master_affinity = request.form['master_affinity']
    master_antiAffinity = request.form['master_antiAffinity']
    master_nodeSelector = request.form['master_nodeSelector']
    master_tolerations = request.form['master_tolerations']
    masterdic['affinity'] = master_affinity
    masterdic['antiAffinity'] = master_antiAffinity
    masterdic['nodeSelector'] = master_nodeSelector
    masterdic['tolerations'] = master_tolerations
    updateStrategydic = dict()
    master_type = request.form['master_type']
    updateStrategydic['type'] = master_type
    masterdic['updateStrategy'] = updateStrategydic
    persistencedic = dict()
    master_persistence_enabled = request.form.get("master_persistence_enabled")
    if master_persistence_enabled == None:
        master_persistence_enabled = "false"
    master_persistence_create = request.form.get("master_persistence_create")
    if master_persistence_create == None:
        master_persistence_create = "false"
    master_storageClassName = request.form['master_storageClassName']
    master_existingClaim = request.form['master_existingClaim']
    master_mountPath = request.form['master_mountPath']
    master_annotations = request.form['master_annotations']
    master_accessModes = request.form['master_accessModes']
    master_size = request.form['master_size']
    persistencedic['enabled'] = bool(strtobool(master_persistence_enabled))
    persistencedic['create'] = bool(strtobool(master_persistence_create))
    persistencedic['storageClassName'] = master_storageClassName
    persistencedic['existingClaim'] = master_existingClaim
    persistencedic['mountPath'] = master_mountPath
    persistencedic['annotations'] = master_annotations
    persistencedic['accessModes'] = master_accessModes.split(",")
    persistencedic['size'] = master_size
    masterdic['persistence'] = persistencedic
    master_extraInitContainers = request.form['master_extraInitContainers']
    masterdic['extraInitContainers'] = master_extraInitContainers
    configdic = dict()
    master_basedir = request.form['master_basedir']
    master_port = request.form['master_port']
    master_socket = request.form['master_socket']
    master_tmpdir = request.form['master_tmpdir']
    master_bind_address = request.form['master_bind-address']
    master_pid_file = request.form['master_pid-file']
    master_log_error = request.form['master_log-error']
    master_character_set_server = request.form['master_character-set-server']
    master_collation_server = request.form['master_collation-server']
    master_default_storage_engine = request.form['master_default-storage-engine']
    mysqlddic = dict()
    mysqlddic['basedir'] = master_basedir
    mysqlddic['port'] = int(master_port)
    mysqlddic['socket'] = master_socket
    mysqlddic['tmpdir'] = master_tmpdir
    mysqlddic['bind-address'] = master_bind_address
    mysqlddic['pid-file'] = master_pid_file
    mysqlddic['log-error'] = master_log_error
    mysqlddic['character-set-server'] = master_character_set_server
    mysqlddic['collation-server'] = master_collation_server
    mysqlddic['default-storage-engine'] = master_default_storage_engine
    configdic['mysqld'] = mysqlddic
    clientdic = dict()
    master_client_port = request.form['master_client_port']
    master_client_socket = request.form['master_client_socket']
    master_client_default_character_set = request.form['master_client_default-character-set']
    clientdic['port'] = int(master_client_port)
    clientdic['socket'] = master_client_socket
    clientdic['default-character-set'] = master_client_default_character_set
    configdic['client'] = clientdic
    managerdic = dict()
    master_manager_port = request.form['master_manager_port']
    master_manager_socket = request.form['master_manager_socket']
    master_manager_pid_file = request.form['master_manager_pid-file']
    managerdic['port'] = int(master_manager_port)
    managerdic['socket'] = master_manager_socket
    managerdic['pid-file'] = master_manager_pid_file
    configdic['manager'] = managerdic
    masterdic['config'] = configdic
    master_resources = request.form['master_resources']
    masterdic['resources'] = master_resources
    livenessProbedic = dict()
    master_livenessProbe_enabled = request.form.get("master_livenessProbe_enabled")
    if master_livenessProbe_enabled == None:
        master_livenessProbe_enabled = "false"
    master_livenessProbe_initialDelaySeconds = request.form['master_livenessProbe_initialDelaySeconds']
    master_livenessProbe_periodSeconds = request.form['master_livenessProbe_periodSeconds']
    master_livenessProbe_timeoutSeconds = request.form['master_livenessProbe_timeoutSeconds']
    master_livenessProbe_successThreshold = request.form['master_livenessProbe_successThreshold']
    master_livenessProbe_failureThreshold = request.form['master_livenessProbe_failureThreshold']
    livenessProbedic['enabled'] = bool(strtobool(master_livenessProbe_enabled))
    livenessProbedic['initialDelaySeconds'] = int(master_livenessProbe_initialDelaySeconds)
    livenessProbedic['periodSeconds'] = int(master_livenessProbe_periodSeconds)
    livenessProbedic['timeoutSeconds'] = int(master_livenessProbe_timeoutSeconds)
    livenessProbedic['successThreshold'] = int(master_livenessProbe_successThreshold)
    livenessProbedic['failureThreshold'] = int(master_livenessProbe_failureThreshold)
    masterdic['livenessProbe'] = livenessProbedic
    readinessProbedic = dict()
    master_readinessProbe_enabled = request.form.get("master_readinessProbe_enabled")
    if master_readinessProbe_enabled == None:
        master_readinessProbe_enabled = "false"
    master_readinessProbe_initialDelaySeconds = request.form['master_readinessProbe_initialDelaySeconds']
    master_readinessProbe_periodSeconds = request.form['master_readinessProbe_periodSeconds']
    master_readinessProbe_timeoutSeconds = request.form['master_readinessProbe_timeoutSeconds']
    master_readinessProbe_successThreshold = request.form['master_readinessProbe_successThreshold']
    master_readinessProbe_failureThreshold = request.form['master_readinessProbe_failureThreshold']
    readinessProbedic['enabled'] = bool(strtobool(master_readinessProbe_enabled))
    readinessProbedic['initialDelaySeconds'] = int(master_readinessProbe_initialDelaySeconds)
    readinessProbedic['periodSeconds'] = int(master_readinessProbe_periodSeconds)
    readinessProbedic['timeoutSeconds'] = int(master_readinessProbe_timeoutSeconds)
    readinessProbedic['successThreshold'] = int(master_readinessProbe_successThreshold)
    readinessProbedic['failureThreshold'] = int(master_readinessProbe_failureThreshold)
    masterdic['readinessProbe'] = readinessProbedic
    podDisruptionBudgetdic = dict()
    master_podDisruptionBudget_enabled = request.form.get("master_podDisruptionBudget_enabled")
    if master_podDisruptionBudget_enabled == None:
        master_podDisruptionBudget_enabled = "false"
    master_podDisruptionBudget_minAvailable = request.form['master_podDisruptionBudget_minAvailable']
    podDisruptionBudgetdic['enabled'] = bool(strtobool(master_podDisruptionBudget_enabled))
    podDisruptionBudgetdic['minAvailable'] = int(master_podDisruptionBudget_minAvailable)
    masterdic['podDisruptionBudget'] = podDisruptionBudgetdic
    return masterdic

def createSlaveDictionary(request):
    slavedic = dict()
    slave_replicas = request.form['slave_replicas']
    slave_affinity = request.form['slave_affinity']
    slave_antiAffinity = request.form['slave_antiAffinity']
    slave_nodeSelector = request.form['slave_nodeSelector']
    slave_tolerations = request.form['slave_tolerations']
    slavedic['replicas'] = int(slave_replicas)
    slavedic['affinity'] = slave_affinity
    slavedic['antiAffinity'] = slave_antiAffinity
    slavedic['nodeSelector'] = slave_nodeSelector
    slavedic['tolerations'] = slave_tolerations
    updateStrategydic = dict()
    slave_type = request.form['slave_type']
    updateStrategydic['type'] = slave_type
    slavedic['updateStrategy'] = updateStrategydic
    persistencedic = dict()
    slave_persistence_enabled = request.form.get("slave_persistence_enabled")
    if slave_persistence_enabled == None:
        slave_persistence_enabled = "false"
    slave_annotations = request.form['slave_annotations']
    slave_accessModes = request.form['slave_accessModes']
    slave_size = request.form['slave_size']
    persistencedic['enabled'] = bool(strtobool(slave_persistence_enabled))
    persistencedic['annotations'] = slave_annotations
    persistencedic['accessModes'] = slave_accessModes.split(",")
    persistencedic['size'] = slave_size
    slavedic['persistence'] = persistencedic
    slave_extraInitContainers = request.form['slave_extraInitContainers']
    slavedic['extraInitContainers'] = slave_extraInitContainers
    configdic = dict()
    slave_basedir = request.form['slave_basedir']
    slave_port = request.form['slave_port']
    slave_socket = request.form['slave_socket']
    slave_tmpdir = request.form['slave_tmpdir']
    slave_bind_address = request.form['slave_bind-address']
    slave_pid_file = request.form['slave_pid-file']
    slave_log_error = request.form['slave_log-error']
    slave_character_set_server = request.form['slave_character-set-server']
    slave_collation_server = request.form['slave_collation-server']
    mysqlddic = dict()
    mysqlddic['basedir'] = slave_basedir
    mysqlddic['port'] = int(slave_port)
    mysqlddic['socket'] = slave_socket
    mysqlddic['tmpdir'] = slave_tmpdir
    mysqlddic['bind-address'] = slave_bind_address
    mysqlddic['pid-file'] = slave_pid_file
    mysqlddic['log-error'] = slave_log_error
    mysqlddic['character-set-server'] = slave_character_set_server
    mysqlddic['collation-server'] = slave_collation_server
    configdic['mysqld'] = mysqlddic
    clientdic = dict()
    slave_client_port = request.form['slave_client_port']
    slave_client_socket = request.form['slave_client_socket']
    slave_client_default_character_set = request.form['slave_client_default-character-set']
    clientdic['port'] = int(slave_client_port)
    clientdic['socket'] = slave_client_socket
    clientdic['default-character-set'] = slave_client_default_character_set
    configdic['client'] = clientdic
    managerdic = dict()
    slave_manager_port = request.form['slave_manager_port']
    slave_manager_socket = request.form['slave_manager_socket']
    slave_manager_pid_file = request.form['slave_manager_pid-file']
    managerdic['port'] = int(slave_manager_port)
    managerdic['socket'] = slave_manager_socket
    managerdic['pid-file'] = slave_manager_pid_file
    configdic['manager'] = managerdic
    slavedic['config'] = configdic
    slave_resources = request.form['slave_resources']
    slavedic['resources'] = slave_resources
    livenessProbedic = dict()
    slave_livenessProbe_enabled = request.form.get("slave_livenessProbe_enabled")
    if slave_livenessProbe_enabled == None:
        slave_livenessProbe_enabled = "false"
    slave_livenessProbe_initialDelaySeconds = request.form['slave_livenessProbe_initialDelaySeconds']
    slave_livenessProbe_periodSeconds = request.form['slave_livenessProbe_periodSeconds']
    slave_livenessProbe_timeoutSeconds = request.form['slave_livenessProbe_timeoutSeconds']
    slave_livenessProbe_successThreshold = request.form['slave_livenessProbe_successThreshold']
    slave_livenessProbe_failureThreshold = request.form['slave_livenessProbe_failureThreshold']
    livenessProbedic['enabled'] = bool(strtobool(slave_livenessProbe_enabled))
    livenessProbedic['initialDelaySeconds'] = int(slave_livenessProbe_initialDelaySeconds)
    livenessProbedic['periodSeconds'] = int(slave_livenessProbe_periodSeconds)
    livenessProbedic['timeoutSeconds'] = int(slave_livenessProbe_timeoutSeconds)
    livenessProbedic['successThreshold'] = int(slave_livenessProbe_successThreshold)
    livenessProbedic['failureThreshold'] = int(slave_livenessProbe_failureThreshold)
    slavedic['livenessProbe'] = livenessProbedic
    readinessProbedic = dict()
    slave_readinessProbe_enabled = request.form.get("slave_readinessProbe_enabled")
    if slave_readinessProbe_enabled == None:
        slave_readinessProbe_enabled = "false"
    slave_readinessProbe_initialDelaySeconds = request.form['slave_readinessProbe_initialDelaySeconds']
    slave_readinessProbe_periodSeconds = request.form['slave_readinessProbe_periodSeconds']
    slave_readinessProbe_timeoutSeconds = request.form['slave_readinessProbe_timeoutSeconds']
    slave_readinessProbe_successThreshold = request.form['slave_readinessProbe_successThreshold']
    slave_readinessProbe_failureThreshold = request.form['slave_readinessProbe_failureThreshold']
    readinessProbedic['enabled'] = bool(strtobool(slave_readinessProbe_enabled))
    readinessProbedic['initialDelaySeconds'] = int(slave_readinessProbe_initialDelaySeconds)
    readinessProbedic['periodSeconds'] = int(slave_readinessProbe_periodSeconds)
    readinessProbedic['timeoutSeconds'] = int(slave_readinessProbe_timeoutSeconds)
    readinessProbedic['successThreshold'] = int(slave_readinessProbe_successThreshold)
    readinessProbedic['failureThreshold'] = int(slave_readinessProbe_failureThreshold)
    slavedic['readinessProbe'] = readinessProbedic
    podDisruptionBudgetdic = dict()
    slave_podDisruptionBudget_enabled = request.form.get("slave_podDisruptionBudget_enabled")
    if slave_podDisruptionBudget_enabled == None:
        slave_podDisruptionBudget_enabled = "false"
    slave_podDisruptionBudget_minAvailable = request.form['slave_podDisruptionBudget_minAvailable']
    podDisruptionBudgetdic['enabled'] = bool(strtobool(slave_podDisruptionBudget_enabled))
    podDisruptionBudgetdic['minAvailable'] = int(slave_podDisruptionBudget_minAvailable)
    slavedic['podDisruptionBudget'] = podDisruptionBudgetdic
    return slavedic

def createMetricsDictionary(request):
    metricsdic = dict()
    metrics_enabled = request.form.get("metrics_enabled")
    if metrics_enabled == None:
        metrics_enabled = "false"
    metricsdic['enabled'] = bool(strtobool(metrics_enabled))
    metrics_registry = request.form['metrics_registry']
    metrics_repository = request.form['metrics_repository']
    metrics_tag = request.form['metrics_tag']
    metrics_pullPolicy = request.form['metrics_pullPolicy']
    metricsimagedic = dict()
    metricsimagedic['registry'] = metrics_registry
    metricsimagedic['repository'] = metrics_repository
    metricsimagedic['tag'] = metrics_tag
    metricsimagedic['pullPolicy'] = metrics_pullPolicy
    metricsdic['image'] = metricsimagedic
    metrics_resources = request.form['metrics_resources']
    metricsdic['resources'] = metrics_resources
    annotationsdic = dict()
    prometheus_io_scrape = request.form.get("prometheus.io/scrape")
    if prometheus_io_scrape == None:
        prometheus_io_scrape = "false"
    prometheus_io_port = request.form['prometheus.io/port']
    annotationsdic['prometheus.io/scrape'] = bool(strtobool(prometheus_io_scrape))
    annotationsdic['prometheus.io/port'] = int(prometheus_io_port)
    metricsdic['annotations'] = annotationsdic
    serviceMonitordic = dict()
    serviceMonitor_enabled = request.form.get("serviceMonitor_enabled")
    if serviceMonitor_enabled == None:
        serviceMonitor_enabled = "false"
    serviceMonitordic['enabled'] = bool(strtobool(serviceMonitor_enabled))
    selectordic = dict()
    prometheus = request.form['prometheus']
    selectordic['prometheus'] = prometheus
    serviceMonitordic['selector'] = selectordic
    metricsdic['serviceMonitor'] = serviceMonitordic
    return metricsdic

def createOthersDictionary(request):
    othersdic = dict()
    coredumpdic = dict()
    coredump_enabled = request.form.get("coredump_enabled")
    if coredump_enabled == None:
        coredump_enabled = "false"
    coredumpdic['enable'] = bool(strtobool(coredump_enabled))
    othersdic['coredump'] = coredumpdic
    networkPolicydic = dict()
    networkpolicy_create = request.form.get("networkpolicy_create")
    if networkpolicy_create == None:
        networkpolicy_create = "false"
    networkPolicydic['create'] = bool(strtobool(networkpolicy_create))
    namespaceSelector = request.form['namespaceSelector']
    networkPolicydic['namespaceSelector'] = namespaceSelector
    othersdic['networkPolicy'] = networkPolicydic
    pspdic = dict()
    psp_enabled = request.form.get("psp_enabled")
    if psp_enabled == None:
        psp_enabled = "false"
    pspdic['enable'] = bool(strtobool(psp_enabled))
    othersdic['psp'] = pspdic
    nrddic = dict()
    namespace = request.form['namespace']
    service = request.form['service']
    nrddic['namespace'] = namespace
    nrddic['service'] = service
    othersdic['nrd'] = nrddic
    return othersdic