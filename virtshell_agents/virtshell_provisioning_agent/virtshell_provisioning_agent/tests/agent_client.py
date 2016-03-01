import websocket
import tornado
import json 

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://127.0.0.1:8080/")
    
    data = {'action':'create',
            'drive':'docker',
            'name':'callanor02', 
            'distribution':'ubuntu',
            'release':'trusty',
            'version': '14.04',
            'arch':'amd64',
            'launch':1,
            'cpus':1,
            'provisioner': "https://github.com/janutechnology/VirtShell_Provisioner_Simple_WebSite_Example.git",
            'executor': "install.sh",
            'user':'callanor',
            'password':'callanor',            
            'memory':1024}

    print("Sending", data)
    ws.send(json.dumps(data))
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received {}".format(result))
    ws.close()

# python agent_client.py
#from git import Repo
#Repo.clone_from("https://github.com/CALlanoR/VirtShell.git", "/root/repositories/virtshell")
