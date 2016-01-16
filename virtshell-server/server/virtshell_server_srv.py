import services.virtshell_server_hosts

def create_host(host):
    return services.virtshell_server_hosts.create_host(host)

def get_all_hosts():
    return services.virtshell_server_hosts.get_all_hosts()

def get_host(uuid):
    return services.virtshell_server_hosts.get_host(uuid)

def exists_host(uuid):
    return services.virtshell_server_hosts.exists_host(uuid)

def delete_host(uuid):
    if exists_host(uuid):
        return services.virtshell_server_hosts.delete_host(uuid)
    else:
