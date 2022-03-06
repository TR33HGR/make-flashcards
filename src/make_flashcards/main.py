from pathlib import WindowsPath
from tkinter import W
import numpy as np
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

        kernel = np.ones((2,2), np.uint8)
        image = cv2.imread(str(path))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #self.image = cv2.Canny(image, 100, 200)
        #ret, self.image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
        #self.image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)
        #ret, image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY) 
        #image = cv2.dilate(image, kernel, iterations=1)
        #image = cv2.erode(image, kernel, iterations=1)
        #image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        rgb_planes = cv2.split(image)
        result_planes = []
        for plane in rgb_planes:
            dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
            bg_img = cv2.medianBlur(dilated_img, 21)
            diff_img = 255 - cv2.absdiff(plane, bg_img)
            result_planes.append(diff_img)

        image = cv2.merge(result_planes)
        #image = cv2.erode(image, kernel, iterations=1)
        image = cv2.dilate(image, kernel, iterations=1)
        ret, image = cv2.threshold(image, 215, 255, cv2.THRESH_BINARY) 
        self.image = image

    def display_image(self):
        if self.image is None:
            raise FileNotFoundError("No image to display")

        cv2.imshow("Image", self.image)
        cv2.waitKey(0)

    def read_text_from_image(self):
        if self.image is None:
            raise FileNotFoundError("No image to read")

        self.text = pytesseract.image_to_string(self.image, lang='kor+eng')

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

    def get_bound_boxes(self):
        if self.text is None:
            raise FileNotFoundError("No text to find boundries")

        boxes = pytesseract.image_to_boxes(self.image)

        output_file = WindowsPath("tests/res/bound_boxes.txt")
        if not output_file.exists():
            output_file.touch()
        with output_file.open(mode="w", encoding="utf-8") as output:
            output.write(boxes)

    def draw_boxes_on_image(self):
        img_width = self.image.shape[1]
        img_height = self.image.shape[0]
        boxes = pytesseract.image_to_boxes(self.image, lang='kor+eng')
        for box in boxes.splitlines():
            box = box.split(" ")
            character = box[0]
            x = int(box[1])
            y = int(box[2])
            x2 = int(box[3])
            y2 = int(box[4])
            cv2.rectangle(self.image, (x, img_height - y), (x2, img_height - y2), (0, 255, 0), 1)
 
            cv2.putText(self.image, character, (x, img_height -y2), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
