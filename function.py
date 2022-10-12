from enum import Flag
import re
import ipaddress
from tokenize import Number
from types import NoneType
from unittest import result
import math
from matplotlib.pyplot import flag

import bcrypt
import sqlite3

from traitlets import Int
####
# CONST
####
maskFromClass = {
    "A": "255.0.0.0",
    "B": "255.255.0.0",
    "C": "255.255.255.0",
    "D": "NOT DEFINED",
    "E": "NOT DEFINED"
}


backgroundColorCorrect = "Green"
backgroundColorIncorrect = "darkred"

#####

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
        "nbNetwork" : NoneType,
        "nbHost": NoneType
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
    elif(classOfIp =="D"):
        info["nbNetwork"] = "N/A"
        info["nbHost"] = "  "
    elif(classOfIp =="E"):
        info["nbNetwork"] = "N/A"
        info["nbHost"] = "Réservé/Expérimental"
        
    return info

def isMaskOfRightClass(mask, classOfIp):
    maskAsTab = strIpAndMaskToTab(mask)
    maskOfClassAsTab = strIpAndMaskToTab(maskFromClass[classOfIp])
    maskAsBinary = ""
    maskOfClassAsBinary = ""
    for i in range(len(maskAsTab)):
        maskAsBinary += decimalTobinary(maskAsTab[i])
        maskOfClassAsBinary += decimalTobinary(maskOfClassAsTab[i])
        
    return (maskAsBinary >= maskOfClassAsBinary)
        
        
        

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
    #creation des 2 réseau
    net1 = ipaddress.IPv4Network(ip1 + "/" + mask1, False)
    net2 = ipaddress.IPv4Network(ip2 + "/" + mask2, False)
    
    if(ipaddress.ip_address(ip2) in net1):
        result.append("Le réseau " + ip1 + "/" + mask1 + " considère que l'ip " + ip2 + " est dans son réseau")
    else:
        result.append("Le réseau " + ip1 + "/" + mask1 + " considère que l'ip " +  ip2 + " n'est pas dans son réseau")
    
    if(ipaddress.ip_address(ip1) in net2):
        result.append("Le réseau " + ip2 + "/" + mask2 + " considère que l'ip " +  ip1 +  " est dans son réseau")
    else:
        result.append("Le réseau " + ip2 + "/" + mask2 + " considère que l'ip " +  ip1 +  " n'est pas dans son réseau")
    
    return result


    
def subnetingByNbSR(nbSR, mask):
    
    #if(len(nbHostBySR) <= 0) :return "Veuillez remplir tout les champs"

    nbExposant = 1
    while(nbSR > (2**nbExposant)):
        nbExposant += 1

    if(len(mask) <= 2):
        nbZeroInsindeMask = 32-(int(mask) + nbExposant)
        nbHostBySR = 2**nbZeroInsindeMask -2
        if(nbHostBySR >=2): return str(nbHostBySR)+ "(+2 avec adresse de broadcast et réseau)"
    else:
        maskTab = strIpAndMaskToTab(mask)
        nbZeroInsindeMask = 0
        for oct in maskTab:
            nbZeroInsindeMask += str(decimalTobinary(oct)).count('0')
        nbHostBySR = 2**(nbZeroInsindeMask-nbExposant)-2
        if(nbHostBySR >= 2):return str(nbHostBySR) + "(+2 avec adresse de broadcast et réseau" 

    return "On ne peux pas réaliser de découpe classique\nsur base du nombre de SR avec ces informations"

    
def getNumberOfOneInsideMask(mask):
    maskTab = strIpAndMaskToTab(mask)
    nbZeroInsindeMask = 0
    for oct in maskTab:
        nbZeroInsindeMask += str(decimalTobinary(oct)).count('0')
    return 32-nbZeroInsindeMask
    
     

def subnetingByNbHostPerSR(nbHostTot, nbHostBySR, mask):
   
    if(len(nbHostBySR) <= 0) :return "Veuillez remplir tout les champs"
    maxHost = max(nbHostBySR)


    nbExposant = 1
    while(maxHost > (2**nbExposant)-2):
        nbExposant += 1

    print(nbExposant, "=>nbExposant")
    if(len(mask) <=2):
        OneAdded = 32 - (int(mask) + nbExposant)
       
        if(OneAdded >= 2): return str(2**OneAdded-1)+ "(+1 réseau non utilisable)"
        
    else:
        OneAdded = 32 - (getNumberOfOneInsideMask(mask) + nbExposant)
        print(OneAdded + getNumberOfOneInsideMask(mask))
        if(OneAdded >= 2): return str(2**OneAdded-1)+ "(+1 réseau non utilisable)"

    
    return "On ne peux pas réaliser de découpe classique\nsur base du nombre d'IP par SR avec ces informations"
    

    

    
   
    


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
        if user[0] == userName and bcrypt.checkpw(password, user[1]):
            flag = True
            break
            
    connection.commit()
    connection.close()
    return flag
    

def display(frame):
    frame.tkraise()
    
def getNbHostTot(mask):
    if len(mask) <=2: return (2**(32-int(mask))-2)
    maskTab = strIpAndMaskToTab(mask)
    totalofZero = 0
    for oct in maskTab:
        totalofZero += str(decimalTobinary(oct)).count('0')
    return ((2**totalofZero)-2)


