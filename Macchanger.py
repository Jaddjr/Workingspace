import subprocess

def change_mac(iFace,newMac):
    print(f"[+] Changing Mac Address to {newMac}")
    subprocess.call({"sudo ifconfig{iFace} down" })
    subprocess.call({"sudo ifconfig{iFace} hw ether {newMac} "})
    subprocess.call({"sudo ifconfig{iFace} up"}) 

ok= "00:11:22:33:44:55"