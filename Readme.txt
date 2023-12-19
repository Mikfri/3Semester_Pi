Set up of RFID scanner

1.	Install Raspbian to Raspberry Pi (Raspberry Pi 4 Model B): 
Raspbian Download: www.raspberrypi.com/software/ 

2.	Solder GPIO pins to RC522 RFID Scanner: 
 
3.	Using breadboard cables, connect the RFID Scanner to the Pi:
•	SDA connects to Pin 24.
•	SCK connects to Pin 23.
•	MOSI connects to Pin 19.
•	MISO connects to Pin 21.
•	GND connects to Pin 6.
•	RST connects to Pin 22.
•	3.3v connects to Pin 1.
 
4.	Connect to the Raspberry Pi via SSH (Putty/VS Code) or VNC (RealVNC). (This requires that you know the IP address, but is preferable.) or with the micro-HDMI-to-HDMI for the monitor and USB for keyboard and mouse:
PuTTY Download: www.putty.org
Visual Studio Code Download: code.visualstudio.com
•	For VS Code you must also install the Remote SSH extension. A tutorial for this is out of scope for this document. A link to Microsoft’s documentation and guide is provided below:
Remote Deployment using SSH: code.visualstudio.com/docs/remote/ssh 

5.	Set up the Raspberry Pi for the RFID Scanner:
•	Enter the CMD prompt and execute: sudo raspi-config
•	Using the arrow keys, select “5 Interfacing Options” and press enter
•	Using the arrow keys, select “P4 SPI” and press enter
•	Select “Yes” when asked if you would like to enable SPI Interface
•	The following text will appear if successful “The SPI interface is enabled”
•	Exit back to the CMD prompt
•	From the CMD prompt and execute: sudo reboot

6.	Now that the Pi is restarted, run the following code in the CMD prompt: 
•	sudo apt update
•	sudo apt upgrade

7.	Make sure python and pip are installed

8.	In the CMD Prompt run the following: 
•	python3 -m pip install spidev 
•	python3 -m pip install mfrc522

9.	Create a new python file on the Raspberry Pi

10.	Clone this repo and run the program

11.	Run the code and scan your RFID Cards / Fobs. 
