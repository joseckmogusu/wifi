import wifi_qrcode_generator as qr
import qrcode

# Generate a QR code for the WiFi network
qr_code = qr.wifi_qrcode('wifi_name', False, 'WPA', 'password')

# Create a QR code image from the generated code
qr_img = qrcode.make(qr_code)

# Save the QR code image to a file
qr_img.save('wifi_qr_code.png')
