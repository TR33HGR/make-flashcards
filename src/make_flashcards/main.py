from pathlib import WindowsPath
import cv2
import pytesseract


class Main:
    def __init__(self):
        self._path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.image = None

    def configure_path_to_tesseract(self):
        path = WindowsPath(self._path_to_tesseract)
        if path.exists():
            pytesseract.pytesseract.tesseract_cmd = self._path_to_tesseract
        else:
            raise FileNotFoundError(f"Tesseract exe not found at {path}")

    def read_image(self, path_to_image):
        path = WindowsPath(path_to_image)
        if path.is_dir():
            raise TypeError(f"Path {path} is a folder, not a file")
        if not path.match('*.jpg'):
            raise TypeError(f"File {path} is not a .jpg")
        if not path.exists():
            raise FileNotFoundError(f"Image not found at {path}")

        self.image = cv2.imread(str(path))

    def display_image(self):
        if self.image is None:
            raise FileNotFoundError("No image to display")

        cv2.imshow("Image", self.image)
        cv2.waitKey(0)
