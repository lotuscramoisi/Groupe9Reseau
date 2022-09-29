


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

def networkAdressCheck(network, netAdress):
    print(network.network_address)
    print(netAdress)
    if (str(network.network_address) == netAdress): return True
    else: return False