# this script is to establish tryhackme environment for you
import os
import sys
import time

def file(*args):
 try:
    os.system("mkdir thm && touch thm/config.txt")
    path = os.getcwd()
    with open('thm/config.txt','w') as config:
        config.write(args[0] + '\n')
        config.write(args[1] + '\n')
        config.write(path + '\n')
    print("\nConfiguring...")
    time.sleep(3)
    print("Configuration done.\n")
    time.sleep(1)
    return path
 except Exception as e:
    print(e)
   

while True:
 print("Enter the operation you want want to perform")
 print("--> 0.Customize the file according to you")
 print("--> 1.Setup the environment for tryhacme")
 print("--> 2.Setup the environment for hackthebox\n")
 choice = int(input("--> Enter Your Choice:- "))

 if(choice == 0):
    print("\n--> \"This customization will be saved for later , this is a one time process only\"")
    user_thm = input("--> Enter your tryhackme username: ")
    user_path = input("--> Enter your path to openvpn file: ")
    #exporting data into file
    path = file(user_thm,user_path)

    
    print("--> Enter 1 - Main Menu\n--> Enter 0 - EXIT\n")  
    choice = int(input("--> Enter Your Choice:- "))
    if(choice == 1):
        continue
    else:
	    exit()

 elif choice ==1:
     with open('thm/config.txt','+r') as file:
      for line in file:
         if '/' in line:
            line = path
     print("Connecting to the vpn...")
     time.sleep(2)
     os.system(f"sudo openvpn {path}/{user_thm}.ovpn")



     
    
    

    



# path = input("Enter the path to the tryhackme file: ")
# os.system("sudo openvpn {path}")

# print(fname)
