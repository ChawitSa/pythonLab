import qrcode

inputLink = "https://open.spotify.com/artist/3pc0bOVB5whxmD50W79wwO?si=X9DEJZ2FQ6OVYX9U_ZYsCQ"
qr = qrcode.QRCode(version=1, box_size=10, border=2)
qr.add_data(inputLink)
qr.make(fit=True)
img = qr.make_image()

img.save("Keshi.jpg")
print(True)