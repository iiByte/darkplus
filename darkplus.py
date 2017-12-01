# Written by Stephane Gagnon, Nov 29th 2017

import math
from time import sleep
from subprocess import *
from PIL import Image, ImageStat

# get systems current wallpaper
result = run(["wallpaper"], stdout=PIPE)
output = result.stdout.decode("utf-8")[0:-1]

wallpaper = Image.open(str(output))
stats = ImageStat.Stat(wallpaper)
r,g,b = stats.mean
perceivedBrightness = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) # max birghtness is 255.0

if perceivedBrightness >= 127.5:
	status = run(["dark-mode", "status"], stdout=PIPE).stdout.decode("utf-8")[0:-1]
	if status == "off":
		print("perceived brightness is " + str(perceivedBrightness) + ", and dark-mode is already off\n")
	elif status == "on":
		print("perceived brightness is " + str(perceivedBrightness) + ", so dark-mode is set to off\n")
		sleep(1)
		call(["dark-mode", "off"])
elif perceivedBrightness < 127.5:
	status = run(["dark-mode", "status"], stdout=PIPE).stdout.decode("utf-8")[0:-1]
	if status == "on":
		print("perceived brightness is " + str(perceivedBrightness) + ", and dark-mode is already on\n")
	elif status == "off":
		print("perceived brightness is " + str(perceivedBrightness) + ", so dark-mode is set to on\n")
		sleep(1)
		call(["dark-mode", "on"])