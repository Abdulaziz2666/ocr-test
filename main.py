import pytesseract

print("OCR MODUL ISHLAYAPTI ✅")

try:
    version = pytesseract.get_tesseract_version()
    print("Tesseract versiyasi:", version)
except Exception as e:
    print("Tesseract topilmadi:", e)
