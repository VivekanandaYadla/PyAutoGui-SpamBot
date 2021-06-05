import pyautogui
import time

l = input("Enter message:")


print("t minus")

count = 10
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1
while True:
	pyautogui.FAILSAFE = False
	pyautogui.typewrite(l + '\n')

