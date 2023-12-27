import os

os.system("clear")

def main():
    print ("")                                                                                                                          
    print ("\033[1;31m██████        \033[1;32m █████  ███    ███  █████  ████████")
    print ("\033[1;31m██   ██       \033[1;32m██   ██ ████  ████ ██   ██    ██")                                                       
    print ("\033[1;31m██████ \033[1;37m █████ \033[1;32m██      ██ ████ ██ ███████    ██")                                             
    print ("\033[1;31m██   ██       \033[1;32m██   ██ ██  ██  ██ ██   ██    ██")
    print ("\033[1;31m██   ██        \033[1;32m█████  ██      ██ ██   ██    ██")
    print ("")
    print ("\033[1;31m[0]\033[1;32mUpdate")
    print ("\033[1;35mcolor")
    print ("\033[1;31m[1]\033[1;32m -C Red")
    print ("\033[1;31m[2]\033[1;32m -C Blue")
    print ("\033[1;31m[3]\033[1;32m -C Back")
    print ("\033[1;31m[4]\033[1;32m -C Green")
    print ("\033[1;31m[5]\033[1;32m -C pink")
    print ("\033[1;31m[6]\033[1;32mExit")
    print ("")
    x=int(input("\033[1;31m[●]\033[1;33mEnter Your Choice \033[1;31m》》\033[1;37m:"))
    if x==0:
       os.system("clear")
       os.system("apt update && apt upgrade -y")
       os.system(" apt install cmatrix -y")
       main()
    elif x==1:
         os.system("cmatrix -C red")
    elif x==2:
         os.system("cmatrix -C blue")
    elif x==3:
         os.system("cmatrix -C back")
    elif x==4:
         os.system("cmatrix -C green")
    elif x==5:
         os.system("cmatrix -C pink")
    elif x==6:
         os.system("clear")
    else:
         print ("not .../")
main()
