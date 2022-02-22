from hamcrest import assert_that, calling, raises
from make_flashcards.main import Main


class TheMain(Main):
    def set_path_to_tesseract(self, path_to_tesseract):
        self._path_to_tesseract = path_to_tesseract


def test_configure_path_to_tesseract_raises_FileNotFoundError_if_tesserect_exe_is_not_in_assumed_location():
    the_main = TheMain()
    the_main.set_path_to_tesseract("c:/assumed/path")

    assert_that(calling(the_main.configure_path_to_tesseract), raises(FileNotFoundError))


def test_read_image_raises_TypeError_if_provided_a_folder_instead_of_a_file():
    the_main = Main()

    assert_that(calling(the_main.read_image).with_args("c:/"), raises(TypeError))


def test_read_image_raises_TypeError_if_not_provided_a_jpg():
    the_main = Main()

    assert_that(calling(the_main.read_image).with_args("c:/incorrect/path.not_jpg"), raises(TypeError))


def test_read_image_raises_FileNotFoundError_if_provided_image_path_is_incorrect():
    the_main = Main()

    assert_that(calling(the_main.read_image).with_args("c:/incorrect/path.jpg"), raises(FileNotFoundError))


def test_display_image_raises_FileNotFoundError_if_read_image_not_called():
    the_main = Main()

    assert_that(calling(the_main.display_image), raises(FileNotFoundError))


def test_write_image_raises_FileNotFoundError_if_read_image_not_called():
    the_main = Main()

    assert_that(calling(the_main.write_image).with_args("_"), raises(FileNotFoundError))


def test_read_text_from_image_raises_FileNotFoundError_if_read_image_not_called():
    the_main = Main()

    assert_that(calling(the_main.read_text_from_image), raises(FileNotFoundError))


def test_write_text_to_file_raises_FileNotFoundError_if_read_text_from_image_not_called():
    the_main = Main()

    assert_that(calling(the_main.write_text_to_file).with_args("_"), raises(FileNotFoundError))


def test():
    the_main = Main()
    image = "tests/res/level1_1.jpg"

    the_main.configure_path_to_tesseract()
    the_main.read_image(image)
    # the_main.display_image()
    the_main.read_text_from_image()
    the_main.write_text_to_file("tests/res/output.txt")
    the_main.write_image("tests/res/image.jpg")
