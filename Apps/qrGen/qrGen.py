

import pyqrcode
from pyqrcode import QRCode

s = input("Please enter a site URL ")

qrName = input("What would you like to save the QR code as? (Just type the file name, we will add the .svg extension) ")

url = pyqrcode.create(s)

url.svg((qrName + ".svg"), scale = 8)


