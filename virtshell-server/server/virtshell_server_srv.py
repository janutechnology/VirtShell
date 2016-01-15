import services.virtshell_server_hosts

def create_host(host):
    return services.virtshell_server_hosts.create_host(host)

def get_all_hosts():
    return services.virtshell_server_hosts.get_all_hosts()
