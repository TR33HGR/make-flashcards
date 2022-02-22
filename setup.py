import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="make-flashcards-tr33hgr", # Replace with your own username
    version="0.0.1",
    author="TR33HGR",
    author_email="",
    description="Automates creation of flashcards from Konkuk Language Institute's Korean textbook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TR33HGR/make-flashcards",
    project_urls={
        "Bug Tracker": "https://github.com/TR33HGR/make-flashcards/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
          'opencv-python',
          'pathlib',
          'pytesseract',
    ],
    python_requires=">=3.6",
)