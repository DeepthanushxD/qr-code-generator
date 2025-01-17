import os
os.system("pip install qrcode")
os.system("pip install pillow") # The qrcode library uses this module
import random
import string
import qrcode

from ui import Logger

logger = Logger()

def generate_random_name(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def save_qr_code(data, output_folder="output"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_name = generate_random_name() + ".png"
    file_path = os.path.join(output_folder, file_name)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    logger.debug(f"QR code saved to: {file_path}") 
def main():
    os.system("cls" if os.name == "nt" else "clear")

    user_input = logger.inp("Enter the URL or text for the QR code:").strip()
    if user_input:
        save_qr_code(user_input)
    else:
        logger.error("No input provided.")  # Cambié "warning" a "warn" según el método definido en ui.py

if __name__ == "__main__":
    main()