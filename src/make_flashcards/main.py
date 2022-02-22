from pathlib import WindowsPath
import cv2
import pytesseract


class Main:
    def __init__(self):
        self._path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.image = None
        self.text = None

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

        image = cv2.imread(str(path))
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def display_image(self):
        if self.image is None:
            raise FileNotFoundError("No image to display")

        cv2.imshow("Image", self.image)
        cv2.waitKey(0)

    def read_text_from_image(self):
        if self.image is None:
            raise FileNotFoundError("No image to read")

        self.text = pytesseract.image_to_string(self.image)

    def write_text_to_file(self, path_to_output_file):
        if self.text is None:
            raise FileNotFoundError("No text to output")

        output_file = WindowsPath(path_to_output_file)
        if not output_file.exists():
            output_file.touch()
        with output_file.open(mode="w", encoding="utf-8") as output:
            output.write(self.text)

    def write_image(self, path_to_output_file):
        if self.image is None:
            raise FileNotFoundError("No image to output")

        output_file = WindowsPath(path_to_output_file)
        cv2.imwrite(str(output_file), self.image)
