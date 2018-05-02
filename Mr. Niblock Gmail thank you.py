
import pyautogui as pg
import webbrowser
import time
#make sure you log into gmail first
webbrowser.open("http://mail.gcds.net")
time.sleep(5)
#wait 5 seconds and then it pesses 'C'
pg.hotkey('c')
time.sleep(7)
pg.hotkey('tab')
time.sleep(1)
pg.typewrite("Thank You", 0.1)



time.sleep(1)
pg.hotkey('tab')
time.sleep(1)
pg.typewrite("Thank you so much for everything!",0.1)
