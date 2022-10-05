from enum import Flag
import re
import ipaddress
from unittest import result
import math
from matplotlib.pyplot import flag

import bcrypt
import sqlite3


def validiteIP(ip):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    unauthorizedIP = (
        "0.0.0.0",
        "1.1.1.1",
        "255.255.255.255"
    )
    if ip in unauthorizedIP or not((re.search(regex, ip))):
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

def networkAdressCheck(network, netAdress):
    if (str(network.network_address) == netAdress): return True
    else: return False
    
def crossNetworkCheck(ip1, mask1, ip2, mask2):
    #intialisation des resultat 
    result = []
    #creation des 2 reseau
    net1 = ipaddress.IPv4Network(ip1 + "/" + mask1, False)
    net2 = ipaddress.IPv4Network(ip2 + "/" + mask2, False)
    
    if(ipaddress.ip_address(ip2) in net1):
        result.append("le reseau " + ip1 + "/" + mask1 + " considere que l'ip " + ip2 + " est dans son reseau")
    else:
        result.append("le reseau " + ip1 + "/" + mask1 + " considere que l'ip " +  ip2 + " n'est pas dans son reseau")
    
    if(ipaddress.ip_address(ip1) in net2):
        result.append("le reseau " + ip2 + "/" + mask2 + " considere que l'ip " +  ip1 +  " est dans son reseau")
    else:
        result.append("le reseau " + ip2 + "/" + mask2 + " considere que l'ip " +  ip1 +  " n'est pas dans son reseau")
    
    return result

def getNbHostByIpAndMask(ip, mask):
    return sum(1 for _ in ipaddress.IPv4Network(ip+"/"+mask, False).hosts())
    
def subnetingByNbSR(nbHostTot, nbSR):
    nbHostBySR = math.floor(nbHostTot / nbSR)
    if(nbHostBySR >= 4): return nbHostBySR
    return "On ne peux pas réaliser de decoupe classique sur base du nombre de SR avec ces informations"

def subnetingByNbHostPerSR(nbHostTot, nbHostBySR):
    maxHost = max(nbHostBySR)
    nbSRTot = math.floor(nbHostTot/maxHost)
    if(nbSRTot >= len(nbHostBySR)): return nbSRTot
    return "On ne peux pas réaliser de decoupe classique sur base du nombre d'IP par SR avec ces informations"



def OnlyNumbersCallback(input):
    if(len(input.get()) == 0): input.insert(0, '0')
    if(not re.fullmatch(r'\d', input.get()[-1])): input.delete(len(input.get())-1)

def tryToLog(userName, password):
    password = password.encode('utf-8')
    flag = False
    connection = sqlite3.connect("user.db")
    db = connection.cursor()
    db.execute("SELECT * from user ")
    for user in db.fetchall():
        print(user[0], " ", userName , " ", bcrypt.checkpw(password, user[1]))
        if user[0] == userName and bcrypt.checkpw(password, user[1]):
            flag = True
            break
            
    connection.commit()
    connection.close()
    return flag
    

def display(frame):
    frame.tkraise()