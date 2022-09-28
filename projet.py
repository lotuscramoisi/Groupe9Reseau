#Groupe 9

import pandas as pd
import re
import ipaddress
from tkinter import *
import tkinter as tk
from ctypes import windll
#####################################################
# CONST
#####################################################

maskFromClass = {
    "A": "255.0.0.0",
    "B": "255.255.0.0",
    "C": "255.255.255.0",
    "D": "NOT DEFINED",
    "E": "NOT DEFINED"
}

#####################################################
# FUNCTION
#####################################################

def validiteIP(ip):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    unauthorizedIP = (
        "0.0.0.0",
        "1.1.1.1",
        "255.255.255.255"
    )
    if ip in unauthorizedIP or not((re.search(regex, ip))):
        print("Ip invalide !")
        return False 
    return True
    


def decimalTobinary(decimal):
    uncompleteBin = str(bin(decimal))[2:]
    lenOfBin = 8- len(uncompleteBin)
    for i in range(lenOfBin):
        uncompleteBin ="0" + uncompleteBin
        
    return uncompleteBin

def strIpAndMaskToTab(ip):
    tab = ip.split(".")
    tabInt= []
    for values in tab:
        tabInt.append(int(values))
    return tabInt

def findClassOfIp(ipAsTab):
    if(ipAsTab[0] >= 240): return "E"
    elif(ipAsTab[0] >= 224): return "D"
    elif(ipAsTab[0] >= 192): return "C"
    elif(ipAsTab[0] >= 128): return "B"
    return "A"
    
def getInfoByClass(classOfIp):
    info = {
        "nbNetwork": 0,
        "nbHost": 0
    }
    if(classOfIp =="A"): 
        info["nbNetwork"] = 2**7
        info["nbHost"] = (2**24) - 2
    elif(classOfIp =="B"):
        info["nbNetwork"] = 2**14
        info["nbHost"] = (2**16) - 2
    elif(classOfIp =="C"):
        info["nbNetwork"] = 2**21
        info["nbHost"] = (2**8) - 2
        
    return info

def getSubNet(IpAdress, mask):
    result = []
    for i in range(len(mask)):
        binAnd = int(mask[i]) & int(IpAdress[i])
        result.append(binAnd)
    return result

def getBroadcast(IpAdress, mask):
    result = []
    for i in range(len(mask)):
        binAnd = (not int(mask[i])) | int(IpAdress[i])
        result.append(binAnd)
    return result

def ObtainResult():
    ip = strIpAndMaskToTab(IP1.get())
    ipClass = findClassOfIp(ip)
    print(ipClass)
    net = ipaddress.IPv4Network(IP1.get() + "/"+ Mask1.get(), False)
    
    print(networkAdressCheck(net, Network1.get()))
    
    if(isClassFull.get() == 1):
        info = getInfoByClass(ipClass)
        print(info)
        print("Network : " +str(net.network_address) + "///Broadcast : " + str(net.broadcast_address))
        print("SubNetwork : " +str(net.network_address) + "///SubBroadcast : " + str(net.broadcast_address))
        if(Mask1.get() != maskFromClass[ipClass]):
            print("You are in a subnet !")
        
def networkAdressCheck(network, netAdress):
    print(network.network_address)
    print(netAdress)
    if (str(network.network_address) == netAdress): return True
    else: return False

#####################################################
# END FUNCTION
#####################################################

#ToDO pas nécessaire ?
windll.shcore.SetProcessDpiAwareness(1)

#creating main window
root = Tk()
root.geometry("1280x720")

#MainFrame
mainFrame = Frame(root)

# Creating side by side frames
frameLeft = Frame(mainFrame, highlightbackground="grey", highlightthickness=1.5)
frameCenter = Frame(mainFrame, highlightbackground="grey", highlightthickness=1.5)
frameRight = Frame(mainFrame, highlightbackground="grey", highlightthickness=1.5)

#----------------------------------------------
#-----------------LeftFrame--------------------
#----------------------------------------------

# First IP
Label(frameLeft, text="IPV4").pack()
IP1 = Entry(frameLeft)
IP1.pack()

# First Mask
Label(frameLeft, text="Masque").pack()
Mask1 = Entry(frameLeft)
Mask1.pack()

# Network IP
Label(frameLeft, text="IP Reseau").pack()
Network1 = Entry(frameLeft)
Network1.pack()

#Checkbox for classfull 
isClassFull = IntVar()
Checkbutton(frameLeft, text="Classfull", variable=isClassFull, onvalue=1, offvalue=0).pack()

#Obtain result
button = Button(frameLeft, text="display IP", command=ObtainResult).pack()


#----------------------------------------------
#----------------CenterFrame-------------------
#----------------------------------------------




#----------------------------------------------
#-----------------RightFrame--------------------
#----------------------------------------------




#Packing frames
frameLeft.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
frameRight.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)
frameCenter.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

mainFrame.pack(fill=BOTH, expand=True, padx=5, pady=5)

#launching the things
root.mainloop()



listValidateIp = [ "235.67.51.50","150.135.191.53","162.81.229.96","99.185.181.53","120.221.37.133","47.78.22.221","107.197.244.23","190.198.186.206","51.185.12.132","75.175.51.251","87.18.199.129","101.158.10.42","206.174.60.30","140.137.165.101","52.89.92.254","114.56.192.2","134.134.237.41","117.129.59.117","128.139.224.223","73.248.184.133","33.155.73.107","235.214.223.123","208.95.16.190","143.236.219.13","15.142.82.138","44.35.90.1","157.68.208.117","96.71.176.126","51.41.87.178","22.237.167.71","178.10.174.217","138.238.179.164","87.144.171.129","222.37.37.65","167.237.179.247","14.138.156.141","150.87.212.98","156.41.192.74","224.171.69.21","27.152.59.142","151.228.38.164","166.253.70.179","253.226.52.178","172.113.236.157","217.123.13.74","15.2.7.151","114.118.98.72","53.154.128.166","51.176.102.231","56.138.239.22","3.91.74.212","68.181.118.206","46.124.60.60","79.133.236.136","31.138.35.145","134.9.43.252","46.196.218.247","208.65.151.228","198.105.204.31","134.74.68.125","11.207.232.6","134.153.191.20","163.155.145.99","103.86.92.162","35.17.201.125","34.243.175.19","91.149.218.143","42.224.2.8","103.28.105.136","49.134.251.61","66.71.16.179","22.239.51.3","38.231.253.2","92.112.90.127","91.159.55.52","100.233.20.158","136.49.210.137","229.183.89.3","15.16.142.85","120.213.201.206","205.85.96.47","153.21.188.151","180.149.94.4","51.251.88.247","234.202.225.133","31.238.122.43","178.49.214.238","104.77.34.43","85.162.196.241","59.132.11.140","17.41.255.69","93.130.173.153","70.166.226.147","177.193.215.244","36.222.24.78","4.184.246.154","241.75.185.156","56.171.234.52","241.135.132.114","252.199.153.86"]


    
# print(decimalTobinary(2))
# print(strIpAndMaskToTab("255.255.255.255"))
# mask="255.255.255.0"
# ip="192.168.0.1"
# net = ipaddress.IPv4Network(ip + "/" + mask, False)
# print(net.network_address)

# print(1 | (0^255))
# for values in listValidateIp:
#     print(values, " /  ",  findClassOfIp(strIpAndMaskToTab(values)), " / ", getInfoByClass(findClassOfIp(strIpAndMaskToTab(values))))
    
    