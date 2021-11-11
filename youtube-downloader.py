#All Reseved By Matheesha 
import os 
import time 
import sys 
os.system("termux-setup-storage") 
os.system("clear")
logotext1 = """\033[93m\033[40m
█▀▄▀█ ▄▀█ ▀█▀ █░█ █▀▀ █▀▀ █▀ █░█ ▄▀█
█░▀░█ █▀█ ░█░ █▀█ ██▄ ██▄ ▄█ █▀█ █▀█\033[0m"""
print(logotext1)
time.sleep(3.0)
os.system("clear")
logotext2 = """\033[94m
          █▄█ ▀█▀ ▄▄ █▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ ▄▀█ █▀▄ █▀▀ █▀█
          ░█░ ░█░ ░░ █▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄\033[0m"""
print(logotext2)
logotext3 = """
              █▀▄▀█ ▄▀█ █ █▄░█   █▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀
              █░▀░█ █▀█ █ █░▀█   █▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░"""
print(logotext3)
print("\033[01m\033[93m                                                        \033[40mV1.0\033[0m")
for char in "\033[01m\033[93m                       \033[40m[+] Tool By Matheesha\033[0m\n\033[01m\033[93m                       \033[40m[+] Sl Cyber Warrior\033[0m\n\033[01m\033[93m                       \033[40m[+] Tool Main Menu\033[0m":
    print(char, end='')
    sys.stdout.flush()
    time.sleep(0.03)
print()
print()
for char in "\033[01m\033[93m                  \033[40m[1] Pytube Video Downloader\033[0m\n\033[01m\033[93m                  \033[40m[2] Youtube-Dl Video Downloader\033[0m\n\033[01m\033[93m                  \033[40m[3] Update All Tools\033[0m\n\033[01m\033[93m                  \033[40m[4] Contact Me\033[0m\n\033[01m\033[93m                  \033[40m[5] Exit\033[0m":
    print(char, end='')
    sys.stdout.flush()
    time.sleep(0.01)
print()
print()
cho = int(input("\033[01m\033[93m     \033[40m[+] Enter Your Choice :: \033[0m"))
if cho == 1 :
	print("\033[01m\033[93m     \033[40m[+] Your Input Is [1] Please Wait...\033[0m")
	time.sleep(5.0)
	os.system("pip install pytube")
	os.system("clear")
	os.system("python pytube-yt.py")
elif cho == 2 :
	print("\033[01m\033[93m     \033[40m[+] Your Input Is [2] Please Wait...\033[0m")
	time.sleep(5.0)
	os.system("pip install youtube_dl")
	os.system("clear")
	os.system("python youtube-dl.py")
elif cho == 3 :
	print("\033[01m\033[93m     \033[40m[+] Updating All Tool...\033[0m")
	time.sleep(3.0)
	os.system("clear")
	os.system("python youtube-downloader.py")
elif cho == 4 :
	os.system("xdg-open http://wa.me/+94766628462")
	time.sleep(0.3)
	os.system("clear")
	os.system("python youtube-downloader.py")
elif cho == 5 :
	print("\033[01m\033[93m     \033[40m[+] Thank For Using...")
	time.sleep(3.0)
	os.system("clear")
	exit()
else :
	print("\033[01m\033[93m     \033[40m[+] You Input Is Wrong...\033[0m")
	time.sleep(3.0)
	os.system("clear")
	os.system("python youtube-downloader.py")
