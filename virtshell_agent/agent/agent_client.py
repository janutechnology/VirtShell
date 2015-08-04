import websocket
import tornado
import json 

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://127.0.0.1:8080/create_instance")
    
    data = {'type':'vmachine', 'memory':1024}

    print("Sending", data)
    ws.send(json.dumps(data))
    print("Sent")
    # print("Receiving...")
    # result = ws.recv()
    # print("Received {}".format(result))
    ws.close()