
#!/usr/bin/python3

import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. /70)
        
        
def main ():
   mengetik ('''\33[1;31m
   ─█▀▀█─█────▀█▀─█─▄▀─█▀▀▀─█▀▀█
   ─█────█─────█──█▀▄──█▀▀▀─█▄▄▀
   ─█▄▄█─█▄▄█─▄█▄─█──█─█▄▄▄─█──█
    ''')
   print ('\33[1;37m╔══════════════════════════════════╗')
   print ('\33[1;37m║\33[1;30m  NAMA : OM FARDI.               \33[1;37m ║')
   print ('\33[1;37m║\33[1;30m  GITHUB : SANGHITAM.            \33[1;37m ║')
   print ('\33[1;37m║\33[1;30m  SC   : PREMIUM.                \33[1;37m ║')
   print ('\33[1;37m╚══════════════════════════════════╝')
   time.sleep(2)
   print ('\33[1;37m╔══════════════════════════════════╗')
   print ('\33[1;37m║\33[1;32m[\33[1;37m01\33[1;32m] \33[1;34m ID GROUP \33[1;37m                   ║')
   print ('\33[1;37m║\33[1;32m[\33[1;37m02\33[1;32m] \33[1;34m LINK TARGET \33[1;37m                ║')
   print ('\33[1;37m║\33[1;32m[\33[1;37m03\33[1;32m] \33[1;34m EMAIL \33[1;37m                      ║')
   print ('\33[1;37m║\33[1;32m[\33[1;37m04\33[1;32m] \33[1;34m RANDOM \33[1;37m                     ║')
   print ('\33[1;37m║\33[1;32m[\33[1;37m05\33[1;32m] \33[1;34m NUMBER   \33[1;37m                   ║')
   print ('\33[1;37m╚══════════════════════════════════╝')
   def login ():
       group = '1'
       link = '2'
       email = '3'
       random ='4'
       
       
       cliker=str(input ('\33[1;32m[\33[35m+\33[1;32m]\33[1;33m enter clicker options\33[1;31m➡\33[1;37m'))
       print ('''\33[1;32m
            ┈┈┈╲┈┈┈┈╱
            ┈┈┈╱▔▔▔▔╲
            ┈┈┃┈▇┈┈▇┈┃
            ╭╮┣━━━━━━┫╭╮
            ┃┃┃┈┈┈┈┈┈┃┃┃
            ╰╯┃┈┈┈┈┈┈┃╰╯
            ┈┈╰┓┏━━┓┏╯
             ┈┈┈╰╯┈┈╰╯
       ''') 
   login()
   def pande ():
       
       user = str (input ('\33[1;37m[\33[1;32m+\33[1;37m]\33[1;33minput kode premium :\33[1;37m'))  
       time.sleep(2)  
       if user =='kasi':
           print ('\33[1;31m°\33[1;32m°\33[1;33m°\33[1;34m°\33[1;35m°\33[1;36m°\33[1;37m°\33[1;38m°')
           time.sleep(1)
       
       else :
           print ('kode premium sala')
   pande()        
   
   def grup ():
       
      grup = str(input ('\33[1;32m[\33[35m+\33[1;32m]\33[1;33m input group id \33[1;31m➡\33[1;37m'))
      
      mengetik ('                \33[1;31m©\33[1;32m®\33[1;33m©\33[1;34m®\33[1;35m©\33[1;36m®\33[1;37m©\33[1;38m®')
      time.sleep(1)
      print ('\33[1;37mhttps://www.facebook.com/profile.php?id=100039753498000 > : \33[1;32murifah0401')
      print ('\33[1;37mhttps://www.facebook.com/profile.php?id=100076367262730 > :\33[1;32mcinta bangsat2003')
      print ('\33[1;37mhttps://www.facebook.com/profile.php?id=100086654252490 > : \33[1;32myugipex endra')
      
     
   grup()
main()
