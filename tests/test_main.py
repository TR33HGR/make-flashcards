from hamcrest import assert_that, calling, raises
from make_flashcards.main import Main


class TheMain(Main):
    def set_path_to_tesseract(self, path_to_tesseract):
        self._path_to_tesseract = path_to_tesseract


def test_configure_path_to_tesseract_raises_FileNotFoundError_if_tesserect_exe_is_not_in_assumed_location():
    the_main = TheMain()
    the_main.set_path_to_tesseract("c:/assumed/path")

    assert_that(calling(the_main.configure_path_to_tesseract), raises(FileNotFoundError))
