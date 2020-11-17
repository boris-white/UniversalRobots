#Echo client program
import socket
import time
HOST = "10.88.0.110"    # The remote host
PORT = 30002              # The same port as used by the server
print ("Starting Program")
count = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

time.sleep(2)
print ("0.2 seconds are up already")
#s.send (str.encode("movej([-1.50, -1.50, -1.57, -1.57, 1.57, 1.57], a=1, v=0.8, t=0, r=0)" + "\n"))
#time.sleep(4)
s.send (str.encode("movej([-1.57, -1.8, -1.5, -1.4, 1.57, 1.57], a=2, v=0.8, t=0, r=0)" + "\n"))
time.sleep(3)
s.send (str.encode("movej([-1.53, -1.8, -1.9, -.9, 1.57, 1.57], a=2, v=0.8, t=0, r=0)" + "\n"))
time.sleep(3)
s.send (str.encode("movej([-2.5, -2.85, -.7, -.1, 1.9, 1.57], a=2, v=1, t=0, r=0)" + "\n"))
time.sleep(5)
s.close()
print ("Program finish")


//should be able to use port 29999 for starting and stopping of the program and port is 30002(not 3002) will allow operator to sends coordinates to move the robot
