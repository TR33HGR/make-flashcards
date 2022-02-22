from pathlib import WindowsPath
import pytesseract


class Main:
    def __init__(self):
        self._path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def configure_path_to_tesseract(self):
        path = WindowsPath(self._path_to_tesseract)
        if path.exists():
            pytesseract.pytesseract.tesseract_cmd = self._path_to_tesseract
        else:
            raise FileNotFoundError(f"Tesseract exe not found at {path}")
