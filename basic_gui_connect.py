# standard libraries
import glob
import time
import tkinter as tk

# installed libraries
import serial


class usb_comm():
    def __init__(self):
        # ports = glob.glob('/dev/tty.usb*')  # mac ports
        ports = ['COM%s' % (i + 1) for i in range(32)]  # windows ports
        # ports = glob.glob('dev/tty[A-Za-z]*')  # linux ports
        # print(ports)
        # devices = []
        # for port in ports:
        #     try:
        #         device = serial.Serial(port=port, write_timeout=0.1,
        #                                inter_byte_timeout=1, baudrate=115200,
        #                                parity=serial.PARITY_EVEN, stopbits=1)
        #         devices.append(device)
        #     except (OSError, serial.SerialException) as error:
        #         pass
        #
        # print(devices)
        self.device = serial.Serial(port='COM4', write_timeout=0.1, timeout=1.0,
                                    inter_byte_timeout=1, baudrate=114286, bytesize=8,
                                    parity=serial.PARITY_EVEN, stopbits=1)

    def write_I(self):
        self.device.write(b'ID')
        message = self.device.read_all()
        # message = self.device.readline()
        # while not message:
        #     message = self.device.readline()
        print(message)


class HelloGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # tk.Button(self, text="Hello", command=hello).pack()
        device = usb_comm()
        tk.Button(self, text="PSoC Hello", command=device.write_I).pack()


if __name__ == "__main__":
    root = HelloGUI()
    root.title("Basic GUI")
    root.geometry("300x300")
    root.mainloop()