import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
bit = platform.architecture()[0]
 
if bit == "64bit":
        os.system('xdg-open https://github.com/KhushalVala/khushal')
 
        from khushal import khushal
 
        khushal()
 
 
 
elif bit == "32bit":
 
        os.system('python khushal.py')
