import qrcode

qr = qrcode.make("https://claude.ai/chat/c412f5bb-f2aa-498d-829e-cf7ef392d77d")
qr.save("qrcode.png")
qr.show()

