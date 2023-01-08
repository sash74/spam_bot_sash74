import pyautogui
import keyboard
a = 0
creenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
currentMouseX, currentMouseY

msg = input('quel sera le meaasge?')
if msg == 'menu secret':
  print (pyautogui.position())

repet = input('combien y aura t-il de messages?')
pyautogui.click(1850, 50)

while a < 2:
  if keyboard.is_pressed('enter'):
      a == a + 3
      break

for i in range(int(repet)):
  pyautogui.write(msg, interval=0.01)
  pyautogui.press('enter')
