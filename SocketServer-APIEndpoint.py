from socket import *
import json
import threading
from datetime import datetime
from time import sleep
import requests

def SendToApi(scan_json):    
    print("______________________")
    
    api_url = "api url here"  # API URL
    
    print(scan_json)

    # Send the measurement as JSON in the request body
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, data=scan_json, headers=headers)
    print(response.text)

    if response.status_code == 201:
        print("Scan sent successfully")
    else:
        print(f"Failed to send scan. Status code: {response.status_code}")
    return scan_json

def runserver():
    serverPort = 12000  # Port number
    serverHost = '192.168.8.8'  # Host name

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen(5)  # Allow up to 5 simultaneous connections
    print("The server is ready to receive")

    while True:
        connectionSocket, address = serverSocket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, address))
        client_thread.start()

def handle_client(connectionSocket, address):
    print("Connection from:", address)

    recv_JSON = connectionSocket.recv(1024).decode()
    print("Received:", recv_JSON)
    
    # Send received JSON to the API
    SendToApi(recv_JSON)
    
    connectionSocket.close()

if __name__ == "__main__":
    runserver()
