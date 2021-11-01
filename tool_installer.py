import time as t
import sys
import os
t.sleep(3)
os.system("clear")
print("""\x1b[1;92m            
        +-+-+-+-+-+-+-+-+-+-+-+-+-+  
        |T|O|O|L|I|N|S|T|A|L|L|E|R|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+
""")
print("================================================")
print("""\033[1;96m]
Tool name:Tool-installer
Version:V1.0
creator:Spider Anongreyhat
Team:TermuxHackz Society
Github:github.com/spider863644
WhatsApp:09052863644 or 08023687626
Description:This tool-installer in the python version of \"tools-installer\" by anonyminhack5

WhatsApp Group:https://chat.whatsapp.com/GpFvNXQDSWfGEh8FvTXJ0W
""")
print("'\x1b[1;92m=================================================")
print("          ======[TOOLS TO INSTALL]======")
print("""\n\033[1;92m[\033[1;94m
1. Install anonphisher   21. Install  termshark
2. Install Botel      22. Install NMap
3. install W-HACK     23. Install Malicious
4. Install Metasploit-framework    24. Install Camphish
5. Install admin-finder  25. Install Skiptracer
6. Install zip-btute   26. Install osint-framework
7. Install CamOver   27. Install  WhatsAppMonitor 
8. Install FBTOOL    
9. Install Trackip
10. Install QRGen
11. Install PhoneInfoga
12. Install GalleryHack
13. Install Crack-rar
14. Install RouterSploit
15. Install Passmaker
16. Install CCTV-HACKING
17. Install SocialBox-Termux
18. Install  Get-instagram-users-info---Any-instagram-account
19. Install sqlmap-dev
20. Install HashCode
""")
print("\033[1;91m======================================================")
print("""\x1b[1;95m
00. Update Tool  E. Exit  J. Join WhatsApp Group
""")
print("\033[1;91m======================================================")
print("\x1b[1;92mChoose a tool to install")
t = input("\x1b[1;92m~#: ")
os.system("clear")
if t == "1":
  os.system("""cd
  git clone https://github.com/TermuxHackz/anonphisher""")
elif t == "2":
  os.system("""cd
  git clone https://github.com/spider863644/Botel""")
elif t == "3":
  os.system("""cd
  git clone https://github.com/spider863644/W-HACK""")
elif t == "4":
  os.system("""cd
  git clone https://github.com/TermuxHackz/Metasploit-framework""")
elif t == "5":
  os.system("""cd
  git clone https://github.com/TermuxHackz/admin-finder""")
elif t == "6":
  os.system("""cd
  git clone https://github.com/TermuxHackz/zip-brute""")
elif t == "7":
  os.system("""cd
  git clone https://github.com/EntySec/CamOver""")
elif t == "8":
  os.system("""cd
  git clone https://github.com/mkdirlove/FBTOOL""")
elif t == "9":
  os.system("""cd
  git clone https://github.com/TermuxHackz/Trackip""")
elif t == "10":
  os.system("""cd
  git clone https://github.com/h0nus/QRGen""")
elif t == "11":
  os.system("""cd
  git clone https://github.com/sundowndev/PhoneInfoga""")
elif t == "12":
  os.system("""cd
  git clone https://github.com/RazorKenway/GalleryHack.git""")
elif t == "13":
  os.system("""cd
  git clone https://github.com/TermuxHackz/Crack-rar""")
elif t == "14":
  os.system("""cd
  git clone https://github.com/reverse-shell/routersploit""")
elif t == "15":
  os.system("""cd
  git clone https://github.com/Anontemitayo/Passmaker""")
elif t == "16":
  os.system("""cd
  git clone https://github.com/U-danbaiwa/CCTV-HACKING.git""")
elif t == "17":
  os.system("""cd
  git clone https://github.com/samsesh/SocialBox-Termux.git""")
elif t == "18":
  os.system("""cd
  git clone https://github.com/zxllkada/Get-instagram-users-info---Any-instagram-account.git""")
elif t == "19":
  os.system("""cd
  git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev""")
elif t == "20":
  os.system("""cd
  git clone https://github.com/Sup3r-Us3r/HashCode.git""")
elif t == "21":
  os.system("""cd
  git clone https://github.com/gcla/termshark""")
elif t == "22":
  os.system("apt install nmap")
elif t == "23":
  os.system("""cd
  git clone https://github.com/Hider5/Malicious""")
elif t == "24":
  os.system("""cd
  git clone https://github.com/techchipnet/CamPhish""")
elif t == "25":
  os.system("""cd
  git clone https://github.com/xiwill/Skip tracer""")
elif t == "26":
  os.system("""cd
  git clone https://github.com/lockfale/osint-framework""")
elif t == "27":
  os.system("""cd
  git clone https://github.com/ErikTschierschke/WhatsappMonitor.git""")
  
elif t == "E": 
  exit()
elif t == "00":
  print("Updating tool")
  os.system("""
  cd $HOME
  rm -f -r Tool-installer
  git clone https://github.com/spider863644/Tool-installer
  cd $HOME
  cd Tool-installer""")
elif t == "J":
  os.system("xdg-open https://chat.whatsapp.com/GpFvNXQDSWfGEh8FvTXJ0W")
else:
  print("\033[1;91mChoose a valid tool to install!"),os.system("python3 tool_installer.py")
t2 = input("Do you wanna install another tools? Y/N: ")
if t2 == "Y":
  os.system("python3 tool_installer.py")
elif t2 == "y":
  os.system("python3 tool_installer.py")
