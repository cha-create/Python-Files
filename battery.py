import psutil

battery = psutil.sensors_battery()
percent = int(battery.percent)
print("Battery: "+str(percent)+'%')