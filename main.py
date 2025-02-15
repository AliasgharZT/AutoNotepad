
import pyautogui as p 
import time as t

p.hotkey('win')
t.sleep(0.4)
q1='notepad'
for q in q1:
    p.hotkey(q) 
t.sleep(0.4)  
p.hotkey('enter')
t.sleep(0.4) 
p.hotkey('shift','alt') 
t.sleep(0.32)  
p.click(700,300) 
q2='hdk d; jsj hsj'
for q in q2:
    p.hotkey(q) 

t.sleep(0.12) 
p.hotkey('ctrl','s')
t.sleep(0.21) 
p.hotkey('shift','alt')
t.sleep(0.17) 
p.hotkey('~')    
q3='test' 
for q in q3:
    p.hotkey(q) 
t.sleep(0.13) 
p.hotkey('enter') 
