from hamcrest import assert_that, is_
from make_flashcards.template import is_true


def test():
    assert_that(is_true(), is_(True))
