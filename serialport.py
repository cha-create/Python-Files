import serial

serialPort = serial.Serial("COM3", 9600)
while True:
    string = input()
    if string == "exit":
        break
    serialPort.write(bytes(string, "ascii"))
    print("written")
    if serialPort.in_waiting > 0:
        print(serialPort.read_all())
