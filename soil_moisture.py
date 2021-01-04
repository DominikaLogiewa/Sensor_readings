import re
import serial


def soil_moisture():
	ser = serial.Serial('/dev/ttyACM0', 9600)
	line=''
	while 1:
		if(ser.in_waiting > 0):
			line = ser.readline()
			print(line)
			break

	return line
