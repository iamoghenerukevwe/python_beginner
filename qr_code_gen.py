import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
print("This is a QR code generator")

p = input("Enter your information: ")

# Generate QR code
url = pyqrcode.create(p)

# Create and save the png file naming "myqr.png"
url.svg("myQR.svg", scale=8)

print("QR code generated check your root directory to locate")