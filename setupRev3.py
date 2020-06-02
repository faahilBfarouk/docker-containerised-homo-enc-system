#! /usr/bin/env python3

import os

def setup():
	print("\n****************************Setting Up***********************************\n")
	os.system("docker run -d -t --name sensor python:3.7 /bin/bash")
	os.system("docker exec sensor mkdir finalYr")
	os.system("docker cp ./encSend.py sensor:/finalYr/")
	os.system("docker cp ./decrypt.py sensor:/finalYr/")
	os.system("docker cp ./data.txt sensor:/finalYr/")
	os.system("docker run -d -t --name cloud python:3.7 /bin/bash")
	os.system("docker exec cloud mkdir finalYr")
	os.system("docker cp ./cloud_compute.py cloud:/finalYr/")
	print("\n============================>Setup Completed<============================\n")
	
def view():
	print("\n*****************************Viewing*************************************")
	print("\nThe files in Sensor:")
	os.system("docker exec sensor ls /finalYr/\n")
	print("\nThe files in Cloud:")
	os.system("docker exec cloud ls /finalYr/\n")
	print("\n*************************************************************************\n")	
def ex():
	print("Exiting..")
	exit()

def enc():
	print("\n****************************Encrypt**************************************\n")
	os.system("docker exec sensor python3 /finalYr/encSend.py")
	os.system("docker cp ./data.txt sensor:/finalYr/")
	os.system("docker cp sensor:/finalYr/output.txt .")
	os.system("docker cp ./output.txt cloud:/finalYr/")
	print("\n*************************************************************************\n")	

def cloud():
	print("\n****************************Cloud*****************************************\n")
	os.system("docker exec cloud python3 /finalYr/cloud_compute.py")
	os.system("docker cp cloud:/finalYr/result.txt .")
	os.system("docker cp ./result.txt sensor:/finalYr/")
	os.system("docker exec cloud rm -rf /finalYr/result.txt")
	print("\n*************************************************************************\n")	

def dec():
	print("\n****************************Decrypt***************************************\n")
	os.system("docker exec sensor python3 /finalYr/decrypt.py")
	os.system("docker exec sensor rm -rf /finalYr/output.txt /finalYr/result.txt")
	os.system("docker exec cloud rm -rf /finalYr/output.txt")
	os.system("docker exec sensor mv /finalYr/end.txt /finalYr/yourResult.txt")
	print("\n*************************************************************************\n")	

def size():
	print("\n****************************Size****************************************\n")
	os.system("docker ps --size")
	print("\n*************************************************************************\n")
def stats():
	print("\n****************************stats****************************************\n")
	os.system("docker container stats")
	print("\n*************************************************************************\n")
print("\n")
while(True):
	
	print("1. View Current Docker State.\n2. Setup Containers\n3. View Files In Containers\n4. Encrypt And Send\n5. Execute Cloud Computation\n6. Decrypt At Sensor\n7. Size Of Containers\n8. Stats Of Containers\n9. Exit")
	inp=int(input("command: "))

	if(inp==1):
		print("\n*************************************************************************")
		os.system("docker container ls")
		print("*************************************************************************\n")
	elif(inp==2):
		setup()
	elif(inp==3):
		view()
	elif(inp==4):
		enc()
	elif(inp==5):
		cloud()
	elif(inp==6):
		dec()
	elif(inp==7):
		size()
	elif(inp==8):
		stats
	elif(inp==9):
		ex()
	else:
		cm=out.get(inp,"invalid")
		os.system(cm)
