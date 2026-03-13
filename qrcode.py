import qrcode

# Your website URL
website_link = "https://example.com"


qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,  
    border=4,  
)

qr.add_data(website_link)
qr.make(fit=True)

# 
img = qr.make_image(fill_color="black", back_color="white")

# choose the file path
img.save("website_qrcode.png")

print("QR Code generated and saved as 'website_qrcode.png'")