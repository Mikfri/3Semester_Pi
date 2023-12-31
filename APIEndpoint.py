import json
from socket import *
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from datetime import datetime

reader = SimpleMFRC522()

class Scan: # class for scan object
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
        JSONSubmission = json.dumps(scan.__dict__)  # convert object to JSON
        print("Sent:", JSONSubmission) # print JSON
        SendToApi(JSONSubmission)  # send object to server
    except Exception as e:
        print("Error reading card:", str(e))

def SendToApi(scan_json):    
    print("______________________")
    
    api_url = "api url here"  # API URL
    
    print(scan_json)

    # Send the measurement as JSON in the request body
    headers = {'Content-Type': 'application/json'} # set headers
    response = requests.post(api_url, data=scan_json, headers=headers) # send request
    print(response.text) # print response

    if response.status_code == 201: # check if response is OK
        print("Scan sent successfully")
    else: # if not OK, print error
        print(f"Failed to send scan. Status code: {response.status_code}")
    return scan_json

def run(): # main function
    while True: # loop forever
        takeScan() # take scan
        time.sleep(2) # wait 2 seconds

if __name__ == "__main__": # run main function
    run()
