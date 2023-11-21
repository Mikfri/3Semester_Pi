import json
from socket import *
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from datetime import datetime

reader = SimpleMFRC522()

class Scan:
    def __init__(self, id, time):
        self.id = id
        self.time = time
    
    def __str__(self):
        return "\nID: " + str(self.id) + "\nTime: " + self.time

def takeScan():
    try:
        id, _ = reader.read()  # read card, ignore text
        current_time = datetime.now().isoformat()  # get current datetime
        scan = Scan(id, current_time)  # create object
        send(scan)  # send object to server
        print("Scan sent")
    except Exception as e:
        print("Error reading card:", str(e))

def send(scan):
    while True:
        serverHost = '192.168.8.8'  # host name
        serverPort = 12000  # port number
        
        clientSocket = socket(AF_INET, SOCK_STREAM)  # create socket
        try:
            clientSocket.connect((serverHost, serverPort))  # connect to server
            JSONSubmission = json.dumps(scan.__dict__)  # convert object to JSON
            clientSocket.send(JSONSubmission.encode())  # send object to server
            print("Sent:", JSONSubmission)
        except Exception as e:
            print("Error connecting to the server:", str(e))
        finally:
            clientSocket.close()  # close connection
            return True

def run():
    while True:
        takeScan()
        time.sleep(2)

if __name__ == "__main__":
    run()
