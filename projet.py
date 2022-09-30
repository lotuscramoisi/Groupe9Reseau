#Groupe 9

from cgitb import text
from turtle import left
import pandas as pd
import ipaddress
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from ctypes import windll
from function import *
import re

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



# def ObtainResult():
#     #### INTERFACE RESET
#     classResult.config(text= "Class: ")
#     numberOfNetworkResult.config( text="Number of network: ")
#     numberOfHostResult.config( text="Number of host: ")
#     networkAdressResult.config( text="Network adress: ")
#     broadcastAdressResult.config( text="Broadcast adress: ")
#     subnetworkAdressResult.config( text="")
#     isSecondIpInFirstNetwork.config( text="")
#     exercice4Result1.config( text="")
#     exercice4Result2.config( text="")
#     ###
#     ip = strIpAndMaskToTab(IP1.get())
#     # Network creation with user mask
#     net = ipaddress.IPv4Network(IP1.get() + "/"+ Mask1.get(), False)

#     # Tell user if the ip/mask combination is in the network he entered
#     if(networkAdressCheck(net, Network1.get())): isSecondIpInFirstNetwork.config(text="l'ip " + IP1.get() + " appartient au reseau " + Network1.get())

#     if(isClassFull.get() == 1):
#         # class determination
#         ipClass = findClassOfIp(ip)
#         classResult.config(text= "Class: "+ ipClass)
        

#         # Network creation with the mask of the class
#         net = ipaddress.IPv4Network(IP1.get() + "/"+ maskFromClass[ipClass], False)

#         info = getInfoByClass(ipClass)
#         print(info)
#         # information display
#         numberOfNetworkResult.config(text= "Number of network: "+ str(info["nbNetwork"]))
#         numberOfHostResult.config(text= "Number of host: "+ str(info["nbHost"]))
#         networkAdressResult.config(text= "Network address: "+ str(str(net.network_address)))
#         broadcastAdressResult.config(text= "Broadcast address: "+ str(str(net.broadcast_address)))


#         # if it's a subnet
#         if(Mask1.get() != maskFromClass[ipClass]):
#             # Subnet definition
#             net = ipaddress.IPv4Network(IP1.get() + "/"+ Mask1.get(), False)
#             subnetworkAdressResult.config(text= "Subnetwork adress: " + str(net.network_address))
#         else:
#             subnetworkAdressResult.config(text= "")

#     if(len(IP2.get()) >0 and len(Mask2.get()) > 0):
#         exercice4Tab = crossNetworkCheck(IP1.get(), Mask1.get(), IP2.get(), Mask2.get())
#         exercice4Result1.config( text=exercice4Tab[0])
#         exercice4Result2.config( text=exercice4Tab[1])
def resultExo1():
    #### INTERFACE RESET
    classResult.config(text= "Class: ")
    numberOfNetworkResult.config( text="Number of network: ")
    numberOfHostResult.config( text="Number of host: ")
    
    ip = strIpAndMaskToTab(IP1.get())
    
    # class determination
    ipClass = findClassOfIp(ip)
    classResult.config(text= "Class: "+ ipClass)
    

    # Network creation with the mask of the class
    net = ipaddress.IPv4Network(IP1.get() + "/"+ maskFromClass[ipClass], False)

    info = getInfoByClass(ipClass)
   
    # information display
    numberOfNetworkResult.config(text= "Number of network: "+ str(info["nbNetwork"]))
    numberOfHostResult.config(text= "Number of host: "+ str(info["nbHost"]))

def resultExo2():
        #Initialisation 
        networkAdressResult.config( text="Network adress: ")
        broadcastAdressResult.config( text="Broadcast adress: ")
        subnetworkAdressResult.config( text="")

        ip = strIpAndMaskToTab(IP2.get())

        # class determination
        ipClass = findClassOfIp(ip)
        # Network creation with user mask
        net = ipaddress.IPv4Network(IP2.get() + "/"+ maskFromClass[ipClass], False)

        #Network and Broadcast adress display
        networkAdressResult.config(text= "Network address: "+ str(str(net.network_address)))
        broadcastAdressResult.config(text= "Broadcast address: "+ str(str(net.broadcast_address)))

        # if it's a subnet
        if(Mask2.get() != maskFromClass[ipClass]):
            # Subnet definition
            net = ipaddress.IPv4Network(IP2.get() + "/"+ Mask2.get(), False)
            subnetworkAdressResult.config(text= "You are in a subnet !\nSubnetwork adress: " + str(net.network_address))

def resultExo3():
    #initialisation
    isSecondIpInFirstNetwork.config( text="")
    #network creation
    net = ipaddress.IPv4Network(IP3.get() + "/"+ Mask3.get(), False)
    # Tell user if the ip/mask combination is in the network he entered
    if(networkAdressCheck(net, Network3.get())): isSecondIpInFirstNetwork.config(text="l'ip " + IP3.get() + " appartient au reseau " + Network3.get())
    else: isSecondIpInFirstNetwork.config(text="l'ip " + IP3.get() + " n'appartient pas au reseau " + Network3.get())

def resultExo4():
    #display result of exo 4
    exercice4Tab = crossNetworkCheck(IP4.get(), Mask4.get(), secondIP4.get(), secondMask4.get())
    exercice4Result1.config( text=exercice4Tab[0])
    exercice4Result2.config( text=exercice4Tab[1])

def resultExo5():
    totalHost = getNbHostByIpAndMask(IP5.get(), Mask5.get())
    nbHostbySR = subnetingByNbSR(totalHost, int(nbSR5.get()))
    nbSRbyHost = subnetingByNbHostPerSR(totalHost, list(map(lambda e: int(e.get()), hostEntries)))
    totalNumberOfHost5.config( text="Nombre total d'hote : " + str(totalHost))
    numberOfHostBySub5.config( text="Nombre d'hote par SR: " + str(nbHostbySR))
    numberOfSubnet5.config( text="Nombre total de SR: " + str(nbSRbyHost))
    


def callbackIPV4(event):
    try:
        net = ipaddress.IPv4Network(IP1.get())
        IP1.config({"background": "White"})
    except ValueError:
        IP1.config({"background": "Gray"})

def callbackMask(event):
   print("Mask")

def callbacknbSR5(event):
    if(len(nbSR5.get()) == 0): nbSR5.insert(0, '0')
    if(not re.fullmatch(r'\d', nbSR5.get()[-1])): nbSR5.delete(len(nbSR5.get())-1)
    for entry in hostEntries:
        entry.destroy()
    hostEntries.clear()
    
    for i in range(int(nbSR5.get())):
        e = Entry(exercice5, background="Gray")
        e.grid(row=3+i,column=1, padx=10, pady=10)
        hostEntries.append(e)


def display(frame):
    frame.tkraise()

#####################################################
# END FUNCTION
#####################################################

#ToDO pas nécessaire ?
windll.shcore.SetProcessDpiAwareness(1)

#creating main window
root = Tk()
root.title("Système et réseau")
s = ttk.Style()
print(s.theme_names())
print(s.theme_use())
root.geometry("1280x720")


#GlobalFrame
globalFrame = Frame(root, background="purple")
globalFrame.grid_rowconfigure(0, weight=1)
globalFrame.grid_columnconfigure(0, weight=1)
globalFrame.pack(side="top", fill="both", expand=True)



####### Exercice1 #######
exercice1 = Frame(globalFrame, background="yellow")
exercice1.grid(row=0, column=0, sticky=N+S+W+E)
#back button
Button(exercice1, text="Back", command=lambda: display(menuFrame)).grid(column=0,row=0)
#ip Entry
Label(exercice1, text="IPV4").grid(row=1,column=0, padx=10, pady=10)
IP1 = Entry(exercice1, background="Gray")
IP1.bind("<KeyRelease>", callbackIPV4) 
IP1.grid(row=1, column=1, padx=10, pady=10)

#Obtain result
Button(exercice1, text="Display result", command=resultExo1).grid(row=4,columnspan=2, padx=10, pady=10)

# Class
classResult = Label(exercice1, text="Class: ")
classResult.grid(row=5,column=0, pady=10, padx=10, sticky="w")
# Number of network
numberOfNetworkResult = Label(exercice1, text="Number of network: ")
numberOfNetworkResult.grid(row=6,column=0, pady=10, padx=10, sticky="w")
# Number of Host
numberOfHostResult = Label(exercice1, text="Number of host: ")
numberOfHostResult.grid(row=7,column=0, pady=10, padx=10, sticky="w")



####### Exercice2 #######
exercice2 = Frame(globalFrame, background="red")
exercice2.grid(row=0, column=0, sticky=N+S+W+E)
Button(exercice2, text="Back", command=lambda: display(menuFrame)).grid(column=0,row=0)

#Ip2 entry
Label(exercice2, text="IPV4").grid(row=1,column=0, padx=10, pady=10)
IP2 = Entry(exercice2, background="Gray")
IP2.bind("<KeyRelease>", callbackIPV4) 
IP2.grid(row=1, column=1, padx=10, pady=10)

#Mask2 entry
Label(exercice2, text="Masque").grid(row=2,column=0, padx=10, pady=10)
Mask2 = Entry(exercice2, background="Gray")
Mask2.bind("<KeyRelease>", callbackMask) 
Mask2.grid(row=2,column=1, padx=10, pady=10)

Button(exercice2, text="Back", command=resultExo2).grid(column=0,row=3)

# Network adress
networkAdressResult = Label(exercice2, text="Network adress: ")
networkAdressResult.grid(row=4,column=0, pady=10, padx=10, sticky="w")

# Broadcast adress
broadcastAdressResult = Label(exercice2, text="Broadcast adress: ")
broadcastAdressResult.grid(row=5,column=0, pady=10, padx=10, sticky="w")

# Subnetwork adress
subnetworkAdressResult = Label(exercice2, text="")
subnetworkAdressResult.grid(row=6,column=0, pady=10, padx=10, sticky="w")



####### Exercice3 #######
exercice3 = Frame(globalFrame, background="purple")
exercice3.grid(row=0, column=0, sticky=N+S+W+E)
Button(exercice3, text="Back", command=lambda: display(menuFrame)).grid(column=0,row=0)

#Ip3 entry
Label(exercice3, text="IPV4").grid(row=1,column=0, padx=10, pady=10)
IP3 = Entry(exercice3, background="Gray")
IP3.bind("<KeyRelease>", callbackIPV4) 
IP3.grid(row=1, column=1, padx=10, pady=10)

#Mask3 entry
Label(exercice3, text="Masque").grid(row=2,column=0, padx=10, pady=10)
Mask3 = Entry(exercice3, background="Gray")
Mask3.bind("<KeyRelease>", callbackMask) 
Mask3.grid(row=2,column=1, padx=10, pady=10)

# Network3 Entry
Label(exercice3, text="IP Reseau").grid(row=3,column=0, padx=10, pady=10)
Network3 = Entry(exercice3, background="Gray")
Network3.grid(row=3,column=1, padx=10, pady=10)

Button(exercice3, text="Display result", command=resultExo3).grid(column=0,row=4)

# isSecondIpInFirstNetwork
isSecondIpInFirstNetwork = Label(exercice3, text="")
isSecondIpInFirstNetwork.grid(row=5,column=0, pady=10, padx=10, sticky="w")



####### Exercice4 #######
exercice4 = Frame(globalFrame, background="blue")
exercice4.grid(row=0, column=0, sticky=N+S+W+E)
Button(exercice4, text="Back", command=lambda: display(menuFrame)).grid(column=0,row=0)

#Ip4 entry
Label(exercice4, text="IPV4 1").grid(row=1,column=0, padx=10, pady=10)
IP4 = Entry(exercice4, background="Gray")
IP4.bind("<KeyRelease>", callbackIPV4) 
IP4.grid(row=1, column=1, padx=10, pady=10)

#Mask4 entry
Label(exercice4, text="Masque 1").grid(row=2,column=0, padx=10, pady=10)
Mask4 = Entry(exercice4, background="Gray")
Mask4.bind("<KeyRelease>", callbackMask) 
Mask4.grid(row=2,column=1, padx=10, pady=10)

#Ip4 entry
Label(exercice4, text="IPV4 2").grid(row=1,column=3, padx=10, pady=10)
secondIP4 = Entry(exercice4, background="Gray")
secondIP4.bind("<KeyRelease>", callbackIPV4) 
secondIP4.grid(row=1, column=4, padx=10, pady=10)

#Mask4 entry
Label(exercice4, text="Masque 2").grid(row=2,column=3, padx=10, pady=10)
secondMask4 = Entry(exercice4, background="Gray")
secondMask4.bind("<KeyRelease>", callbackMask) 
secondMask4.grid(row=2,column=4, padx=10, pady=10)

Button(exercice4, text="Display result", command=resultExo4).grid(column=0,row=3)

# result Exercice 4
exercice4Result1 = Label(exercice4, text="")
exercice4Result1.grid(row=4,column=0, pady=10, padx=10, sticky="w")
exercice4Result2 = Label(exercice4, text="")
exercice4Result2.grid(row=5,column=0, pady=10, padx=10, sticky="w")



####### Exercice5 #######
exercice5 = Frame(globalFrame, background="green")
exercice5.grid(row=0, column=0, sticky=N+S+W+E)
Button(exercice5, text="Back", command=lambda: display(menuFrame)).grid(column=0,row=0)

Button(exercice5, text="Display result", command=resultExo5).grid(column=3,row=0)
#Ip5 entry
Label(exercice5, text="IPV4").grid(row=1,column=0, padx=10, pady=10)
IP5 = Entry(exercice5, background="Gray")
IP5.bind("<KeyRelease>", callbackIPV4) 
IP5.grid(row=1, column=1, padx=10, pady=10)

#Mask5 entry
Label(exercice5, text="Masque").grid(row=2,column=0, padx=10, pady=10)
Mask5 = Entry(exercice5, background="Gray")
Mask5.bind("<KeyRelease>", callbackMask) 
Mask5.grid(row=2,column=1, padx=10, pady=10)


hostEntries = []
# number of subnet entry
Label(exercice5, text="Nombre de sous-réseau").grid(row=3,column=0, padx=10, pady=10)
nbSR5 = Entry(exercice5, background="Gray")
nbSR5.bind("<KeyRelease>", callbacknbSR5) 
nbSR5.grid(row=3,column=0, padx=10, pady=10)
nbSR5.insert(0, '0')

# total number of host5
totalNumberOfHost5 = Label(exercice5, text="")
totalNumberOfHost5.grid(row=1, column=3, padx=10, pady=10)

#number of host by subnet5
numberOfHostBySub5 = Label(exercice5, text="")
numberOfHostBySub5.grid(row=2, column=3, padx=10, pady=10)

# number of subnet5
numberOfSubnet5 = Label(exercice5, text="")
numberOfSubnet5.grid(row=3, column=3, padx=10, pady=10)





####### MenuFrame #######
menuFrame = Frame(globalFrame, background="black")
menuFrame.grid(row=0, column=0, sticky=N+S+W+E)
Button(menuFrame, text="1 - Network from IP", command=lambda: display(exercice1)).grid(column=0,row=0)
Button(menuFrame, text="2 - Network Or SubNetwork from IP And Mask ", command= lambda: display(exercice2)).grid(column=0,row=1)
Button(menuFrame, text="3", command= lambda: display(exercice3)).grid(column=0,row=2)
Button(menuFrame, text="4", command= lambda: display(exercice4)).grid(column=0,row=4)
Button(menuFrame, text="5", command= lambda: display(exercice5)).grid(column=0,row=5)



# # Creating side by side frames
# frameLeft = Frame(exercice1, highlightbackground="grey", highlightthickness=1.5)
# frameCenter = Frame(exercice1, highlightbackground="grey", highlightthickness=1.5)
# frameRight = Frame(exercice1, highlightbackground="grey", highlightthickness=1.5)


# #----------------------------------------------
# #-----------------LeftFrame--------------------
# #----------------------------------------------
# #SubFrame
# frameLeftCenter = Frame(frameLeft)

# # First IP




# # Network IP
# Label(frameLeftCenter, text="IP Reseau").grid(row=2,column=0, padx=10, pady=10)
# Network1 = Entry(frameLeftCenter, background="Gray")
# Network1.grid(row=2,column=1, padx=10, pady=10)



# #Obtain result
# button = Button(frameLeftCenter, text="Display IP", command=ObtainResult).grid(row=4,columnspan=2, padx=10, pady=10)


# # Exercise 1


# # Exercice 2


# # Exercice 3




# frameLeftCenter.pack()
# #----------------------------------------------
# #----------------CenterFrame-------------------
# #----------------------------------------------
# #Subframe
# frameCenterCenter = Frame(frameCenter)

# # Exercice 4
# # Second IP
# Label(frameCenterCenter, text="Second IPV4").grid(row=0,column=0, padx=10, pady=10)
# IP2 = Entry(frameCenterCenter)
# IP2.grid(row=0, column=1, padx=10, pady=10)

# # Second Mask
# Label(frameCenterCenter, text="Second Mask").grid(row=1,column=0, padx=10, pady=10)
# Mask2 = Entry(frameCenterCenter)
# Mask2.grid(row=1,column=1, padx=10, pady=10)

# # result Exercice 4
# exercice4Result1 = Label(frameCenterCenter, text="")
# exercice4Result1.grid(row=3,column=0, pady=10, padx=10, sticky="w")
# exercice4Result2 = Label(frameCenterCenter, text="")
# exercice4Result2.grid(row=4,column=0, pady=10, padx=10, sticky="w")

# frameCenterCenter.pack()
#----------------------------------------------
#-----------------RightFrame--------------------
#----------------------------------------------


# #Packing frames
# frameLeft.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
# frameRight.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)
# frameCenter.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)



menuFrame.tkraise()


#launching the things
root.mainloop()



listValidateIp = [ "235.67.51.50","150.135.191.53","162.81.229.96","99.185.181.53","120.221.37.133","47.78.22.221","107.197.244.23","190.198.186.206","51.185.12.132","75.175.51.251","87.18.199.129","101.158.10.42","206.174.60.30","140.137.165.101","52.89.92.254","114.56.192.2","134.134.237.41","117.129.59.117","128.139.224.223","73.248.184.133","33.155.73.107","235.214.223.123","208.95.16.190","143.236.219.13","15.142.82.138","44.35.90.1","157.68.208.117","96.71.176.126","51.41.87.178","22.237.167.71","178.10.174.217","138.238.179.164","87.144.171.129","222.37.37.65","167.237.179.247","14.138.156.141","150.87.212.98","156.41.192.74","224.171.69.21","27.152.59.142","151.228.38.164","166.253.70.179","253.226.52.178","172.113.236.157","217.123.13.74","15.2.7.151","114.118.98.72","53.154.128.166","51.176.102.231","56.138.239.22","3.91.74.212","68.181.118.206","46.124.60.60","79.133.236.136","31.138.35.145","134.9.43.252","46.196.218.247","208.65.151.228","198.105.204.31","134.74.68.125","11.207.232.6","134.153.191.20","163.155.145.99","103.86.92.162","35.17.201.125","34.243.175.19","91.149.218.143","42.224.2.8","103.28.105.136","49.134.251.61","66.71.16.179","22.239.51.3","38.231.253.2","92.112.90.127","91.159.55.52","100.233.20.158","136.49.210.137","229.183.89.3","15.16.142.85","120.213.201.206","205.85.96.47","153.21.188.151","180.149.94.4","51.251.88.247","234.202.225.133","31.238.122.43","178.49.214.238","104.77.34.43","85.162.196.241","59.132.11.140","17.41.255.69","93.130.173.153","70.166.226.147","177.193.215.244","36.222.24.78","4.184.246.154","241.75.185.156","56.171.234.52","241.135.132.114","252.199.153.86"]


    

    
    