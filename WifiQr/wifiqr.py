########
#imports
########
import qrcode
from PIL import Image
import getpass
import sys

########
#script
########

########################################################################################
def main():
    """
    """
    if len(sys.argv) == 1:
        string = getInput()
        img = createQR(string)
        save(img)
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("help")
    elif len(sys.argv) == 5:
        SSID = sys.argv[1]
        security = sys.argv[2]
        hidden = sys.argv[3]
        pw = sys.argv[4]
        string = "WIFI:T:{};S:{};H:{};P:{};;".format(security, SSID, hidden, pw)
        img = createQR(string)
        save(img)
    else:
        print("ERROR")
        sys.exit()

########################################################################################
def getInput():
    """
    """
    SSID = input("Enter SSID: ")
    security = input("Enter Security: ")
    hidden = input("SSID hidden true or false?:")
    pw = input("Enter password: ")
    return "WIFI:T:{};S:{};H:{};P:{};;".format(security, SSID, hidden, pw)

########################################################################################
def createQR(string):
    """
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(string)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")

########################################################################################
def save(img):
    """
    """
    user = getpass.getuser()
    name = input("name qr code: ")
    save = "C:/Users/{}/Desktop/{}.png".format(user, name)
    img.save(save)
    im = Image.open(r""+save)
    im.show()

if __name__ == "__main__":
    main()