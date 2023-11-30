import json
from socket import *
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import requests

reader = SimpleMFRC522()

class CardData:
    def __init__(self, cardNumber, unixTime):
        self.CardNumber = int(cardNumber)  # Ensure CardNumber is an integer
        self.UnixTime = unixTime

def takeScan():
    try:
        cardNumber, _ = reader.read()  # read card, ignore text
        unixTime = int(time.time())  # get current datetime
        cardData = CardData(cardNumber, unixTime)  # create object
        JSONSubmission = json.dumps(cardData.__dict__)  # convert object to JSON
        print("Sent:", JSONSubmission)  # print JSON
        SendToApi(JSONSubmission)  # send object to server
    except Exception as e:
        print("Error reading card:", str(e))

def SendToApi(scan_json):
    print("__")

    api_url = "https://zealandconnect.azurewebsites.net/api/Card/"  # API URL

    print(scan_json)

    # Send the measurement as JSON in the request body
    headers = {'Content-Type': 'application/json'}  # set headers
    print("Before sending request")
    response = requests.post(api_url, data=scan_json, headers=headers)
    print("After sending request")
    print(response.text)  # print response

    if response.status_code == 200:  # check if response is OK
        print("Scan sent successfully")
    else:  # if not OK, print error
        print(f"Failed to send scan. Status code: {response.status_code}")
    return scan_json

def run():  # main function
    while True:  # loop forever
        takeScan()  # take scan
        time.sleep(2)  # wait 2 seconds

if __name__ == "__main__":  # run main function
    run()
