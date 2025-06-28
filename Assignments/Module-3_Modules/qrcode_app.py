import qrcode

"""url="https://www.tops-int.com/"

qr=qrcode.make(url)
qr.save("tops.png")"""



msg="This is Python!"

qr=qrcode.make(msg)
qr.save("secret.png")