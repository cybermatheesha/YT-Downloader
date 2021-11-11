#All Reseved By Matheesha
import os
import sys
import time
import pytube
from pytube import YouTube
os.system("termux-setup-storage")
os.system("clear")
logo = """\033[93m\033[40m
  █▀▄▀█ █▀▀█ ▀▀█▀▀ █  █ █▀▀ █▀▀ █▀▀ █  █ █▀▀█ 
  █ ▀ █ █▄▄█   ▀   █▀▀█ █▀▀ █▀▀ ▀▀█ █▀▀█ █▄▄█ 
  ▀   ▀ ▀  ▀   ▀   ▀  ▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀  ▀ ▀  ▀\033[0m"""
print(logo)
time.sleep(3.0)
os.system("clear")
logo1 = """\033[94m
             █  █ █▀▀█ █  █ ▀▀█▀▀ █  █ █▀▀▄ █▀▀
             █▄▄█ █  █ █  █   █   █  █ █▀▀▄ █▀▀
             ▄▄▄█ ▀▀▀▀  ▀▀▀   ▀    ▀▀▀ ▀▀▀  ▀▀▀
\033[0m
       █▀▀▄ █▀▀█ █   █ █▀▀▄ █   █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█
       █  █ █  █ █▄█▄█ █  █ █   █  █ █▄▄█ █  █ █▀▀ █▄▄▀
       ▀▀▀  ▀▀▀▀  ▀ ▀  ▀  ▀ ▀▀▀ ▀▀▀▀ ▀  ▀ ▀▀▀  ▀▀▀ ▀ ▀▀"""
print(logo1)
print("\033[01m\033[93m                                                   \033[40mV1.0\033[0m")
for char in "\033[01m\033[93m                  \033[40m[+] Tool By Matheesha\033[0m\n\033[01m\033[93m                  \033[40m[+] Sl Cyber Warrior\033[0m\n\033[01m\033[93m                  \033[40m[+] With Pytube-Yt\033[0m ":
    print(char, end='') 
    sys.stdout.flush() 
    time.sleep(0.03)
print()
print()
for char in "\033[93m\033[01m                      \033[40m[1] Download Video\033[0m\033[01m\033[93m\n                      \033[40m[2] Download Audio\033[0m\033[01m\033[93m\n                      \033[40m[3] Update Tool\033[0m\n\033[01m\033[93m                      \033[40m[4] Contact Me\033[0m\n\033[01m\033[93m\033[01m\033[93m                      \033[40m[5] Main Menu\033[0m\n\033[01m\033[93m                      \033[40m[6] Exit\033[0m":
    print(char, end='')
    sys.stdout.flush()
    time.sleep(0.01)
print()
print()
cho = (int(input("\033[01m\033[93m     \033[40m[+] Enter Your Choice :: \033[0m")))
if cho == 1 :
	video_url = input("\033[01m\033[93m     \033[40m[+] Enter Your Video [URL] ::\033[0m")
	print("\033[01m\033[93m     \033[40m[+] Downloading Your Video...\033[0m")
	youtube = pytube.YouTube(video_url)
	video = youtube.streams.first()
	video.download('YOU_TUBE_DOWNLOADER_VIDEOS')
	print("\033[01m\033[93m     \033[40m[+] Video Downloaded...\033[0m")
	time.sleep(0.3)
	print("\033[01m\033[93m     \033[40m[+] Please Chek Your [File Manager] App...\033[0m")
	time.sleep(0.5)
	os.system("clear")
	os.system("python pytube-yt.py")
elif cho == 2 :
	yt = YouTube(
		str(input("\033[01m\033[93m     \033[40m[+] Enter Youtube Video [URL] :: \033[0m")))
	video = yt.streams.filter(only_audio=True).first()
	print("\033[01m\033[93m     \033[40m[+] Downloading Your Audio...\033[0m")
	time.sleep(3.0)
	destination = ('YOU_TUBE_DOWNLOADER_AUDIOS') or '.'
	out_file = video.download(output_path=destination)
	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.rename(out_file, new_file)
	print("\033[01m\033[93m     \033[40m[+] Please Chek Your [File Manager] App...\033[0m")
	time.sleep(5.0)
	os.system("clear")
	os.system("python pytube-yt.py")
elif cho == 3 :
	print("\033[01m\033[93m     \033[40m[+] Updating...\033[0m")
	time.sleep(3.0)
	os.system("clear")
	os.system("python pytube-yt.py")
elif cho == 4 :
	os.system("xdg-open http://wa.me/+94766628462")
	time.sleep(0.3)
	os.system("clear")
	os.system("python pytube-yt.py")
elif cho == 5 :
	os.system("clear")
	os.system("python youtube-downloader.py")
elif cho == 6 :
	print("\033[01m\033[93m     \033[40m[+] Thank For Using...")
	time.sleep(3.0)
	os.system("clear")
else :
	print("\033[01m\033[93m     \033[40m[+] You Input Is Wrong...\033[0m")
	time.sleep(3.0)
	os.system("clear")
	os.system("python pytube-yt.py")
