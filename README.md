# make-flashcards
Automates creation of flashcards from Konkuk Language Institute's Korean textbook

Created following the [Python Project – Text Detection and Extraction with OpenCV and OCR](https://projectgurukul.org/python-text-detection-extraction-opencv-ocr/) tutorial

## requirments
This project requires [Tesseract](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1.20220118.exe) be installed. I have also included all `Additioanl script data` and `Additioanl language data` when installing, but you should only require the Chinese options, Korean, and Japanese as additional languages

## tox
For tox, from the base directory, run the command:
```
tox
```

On the first run, this will set up virtual environments for pytest, pylint, & flake8.

### pytest
pytest will run all the test files defined in the `/tests` folder.

### pylint
pylint will check the codestyle of files defined in both the `/tests` & `/src` folders.

Warnings for ``missing-docstring`` have been excluded in the tox file. Any additional warning suppression can be added to the ``--disable`` line in the ``[testenv:pylint] ... commands = ...`` in the `tox.ini` file or disabled individually on the specific file giving the warning.

### flake8
flake8 with check the codestyle of files defined in both the `/test` & the `/src` folders.