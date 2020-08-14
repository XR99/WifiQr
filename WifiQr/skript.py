import qrcode
from PIL import Image 

name = input("Enter name of Wifi: ")
security = input("Enter Security: ")
pw = input("Enter password: ")
string = "WIFI:T:"+security+";S:"+name+";P:"+pw+";;"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(string)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save("qr.png")
