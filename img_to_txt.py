from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\yash\AppData\Local\Tesseract-OCR\tesseract.exe"
img = Image.open(r"C:\Users\yash\Desktop\test.png")
text = pytesseract.image_to_string(img)
print(text)
