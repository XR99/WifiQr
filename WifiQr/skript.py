import qrcode
from PIL import Image
import getpass

SSID = input("Enter SSID: ")
security = input("Enter Security: ")
hidden = input("SSID hidden true or false?:")
pw = input("Enter password: ")
string = "WIFI:T:{};S:{};H:{};P:{};;".format(security, SSID, hidden, pw)


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(string)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")


user = getpass.getuser()
name = input("name qr code: ")
save = "C:/Users/{}/Desktop/{}.png".format(user, name)
img.save(save)
im = Image.open(r""+save)
im.show()