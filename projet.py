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

def callbackIPV4(event):
    try:
        net = ipaddress.IPv4Network(IP1.get())
        IP1.config({"background": "White"})
    except ValueError:
        print("Incorrect Ip")
        IP1.config({"background": "Gray"})

def callbackMask(event):
   print("Mask")

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
#ip Entry
Label(exercice1, text="IPV4").grid(row=0,column=0, padx=10, pady=10)
IP1 = Entry(exercice1, background="Gray")
IP1.bind("<KeyRelease>", callbackIPV4) 
IP1.grid(row=0, column=1, padx=10, pady=10)

#Obtain result
button = Button(exercice1, text="Display result", command=resultExo1).grid(row=4,columnspan=2, padx=10, pady=10)

# Class
classResult = Label(exercice1, text="Class: ")
classResult.grid(row=5,column=0, pady=10, padx=10, sticky="w")
# Number of network
numberOfNetworkResult = Label(exercice1, text="Number of network: ")
numberOfNetworkResult.grid(row=6,column=0, pady=10, padx=10, sticky="w")
# Number of Host
numberOfHostResult = Label(exercice1, text="Number of host: ")
numberOfHostResult.grid(row=7,column=0, pady=10, padx=10, sticky="w")

# Exercice2
exercice2 = Frame(globalFrame)
exercice1.grid(row=0, column=0, sticky=N+S+W+E)
# Exercice

#MenuFrame
menuFrame = Frame(globalFrame, background="black")
menuFrame.grid(row=0, column=0, sticky=N+S+W+E)
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


# # First Mask
# Label(frameLeftCenter, text="Masque").grid(row=1,column=0, padx=10, pady=10)
# Mask1 = Entry(frameLeftCenter, background="Gray")
# Mask1.bind("<KeyRelease>", callbackMask) 
# Mask1.grid(row=1,column=1, padx=10, pady=10)

# # Network IP
# Label(frameLeftCenter, text="IP Reseau").grid(row=2,column=0, padx=10, pady=10)
# Network1 = Entry(frameLeftCenter, background="Gray")
# Network1.grid(row=2,column=1, padx=10, pady=10)



# #Obtain result
# button = Button(frameLeftCenter, text="Display IP", command=ObtainResult).grid(row=4,columnspan=2, padx=10, pady=10)


# # Exercise 1


# # Exercice 2
# # Network adress
# networkAdressResult = Label(frameLeftCenter, text="Network adress: ")
# networkAdressResult.grid(row=8,column=0, pady=10, padx=10, sticky="w")

# # Broadcast adress
# broadcastAdressResult = Label(frameLeftCenter, text="Broadcast adress: ")
# broadcastAdressResult.grid(row=9,column=0, pady=10, padx=10, sticky="w")

# # Subnetwork adress
# subnetworkAdressResult = Label(frameLeftCenter, text="")
# subnetworkAdressResult.grid(row=10,column=0, pady=10, padx=10, sticky="w")

# # Exercice 3
# isSecondIpInFirstNetwork = Label(frameLeftCenter, text="")
# isSecondIpInFirstNetwork.grid(row=11,column=0, pady=10, padx=10, sticky="w")



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



exercice1.tkraise()


#launching the things
root.mainloop()



listValidateIp = [ "235.67.51.50","150.135.191.53","162.81.229.96","99.185.181.53","120.221.37.133","47.78.22.221","107.197.244.23","190.198.186.206","51.185.12.132","75.175.51.251","87.18.199.129","101.158.10.42","206.174.60.30","140.137.165.101","52.89.92.254","114.56.192.2","134.134.237.41","117.129.59.117","128.139.224.223","73.248.184.133","33.155.73.107","235.214.223.123","208.95.16.190","143.236.219.13","15.142.82.138","44.35.90.1","157.68.208.117","96.71.176.126","51.41.87.178","22.237.167.71","178.10.174.217","138.238.179.164","87.144.171.129","222.37.37.65","167.237.179.247","14.138.156.141","150.87.212.98","156.41.192.74","224.171.69.21","27.152.59.142","151.228.38.164","166.253.70.179","253.226.52.178","172.113.236.157","217.123.13.74","15.2.7.151","114.118.98.72","53.154.128.166","51.176.102.231","56.138.239.22","3.91.74.212","68.181.118.206","46.124.60.60","79.133.236.136","31.138.35.145","134.9.43.252","46.196.218.247","208.65.151.228","198.105.204.31","134.74.68.125","11.207.232.6","134.153.191.20","163.155.145.99","103.86.92.162","35.17.201.125","34.243.175.19","91.149.218.143","42.224.2.8","103.28.105.136","49.134.251.61","66.71.16.179","22.239.51.3","38.231.253.2","92.112.90.127","91.159.55.52","100.233.20.158","136.49.210.137","229.183.89.3","15.16.142.85","120.213.201.206","205.85.96.47","153.21.188.151","180.149.94.4","51.251.88.247","234.202.225.133","31.238.122.43","178.49.214.238","104.77.34.43","85.162.196.241","59.132.11.140","17.41.255.69","93.130.173.153","70.166.226.147","177.193.215.244","36.222.24.78","4.184.246.154","241.75.185.156","56.171.234.52","241.135.132.114","252.199.153.86"]


    

    
    