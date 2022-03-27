# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import pickle
import struct

import numpy
import cv2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    alist = []
    print_hi('welcome to the Cloud Server!')
    # print(socket.gethostbyaddr('127.0.0.1'))
    # first of all import the socket library

    # next create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 12345

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))
    print("socket binded to %s" % (port))

    # put the socket into listening mode
    s.listen(10)
    print("socket is listening")

    # a forever loop until we interrupt it or
    # an error occurs
    c, addr = s.accept()
    print('Got connection from', addr)
    data = b""
    payload_size = struct.calcsize("L")
    count = 0

    while True:
        while len(data) < payload_size:
            data += c.recv(4096)
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]
        while len(data) < msg_size:
            data += c.recv(4096)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        ###

        frame=pickle.loads(frame_data)
        print(frame.Cam_IP)
        print(frame.Number_Faces)
        print(frame.Timestamp)
        alist = frame.Images
        # print(type(alist))
        cv2.imwrite(str(count)+'_faces.jpg', alist)
        count += 1
    # while True:
    #
    #
    #     # send a thank you message to the client. encoding to send byte type.
    #     # c.send('Thank you for connecting'.encode())
    #
    #     data = b''
    #     count = 0
    #     while True:
    #         packet = c.recv(8192)
    #         # print(len(packet))
    #         if not packet: break
    #         data += packet
    #
    #     # data = c.recv(4096)
    #     data_variable = pickle.loads(data)
    #     # Close the connection with the client
    #     print(data_variable.Cam_IP)
    #     print(data_variable.Number_Faces)
    #     print(data_variable.Timestamp)
    #     alist = data_variable.Images
    #     cv2.imwrite('faces.jpg' + count, alist)
    #     count += 1
    #     c.close()
    #
    #     # Breaking once connection closed
    #     break

    


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
