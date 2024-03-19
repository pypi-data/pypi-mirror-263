from setuptools import setup, find_packages

VERSION = '0.0.11'
DESCRIPTION = 'Least Significant Bit (LSB) Steganography'
LONG_DESCRIPTION = 'A package that allows to hide clear text messages inside the least significant bits of a PNG or WAV file.'

# Setting up
setup(
    name="lsbs",
    version=VERSION,
    author="N3XU5_666",
    author_email="<n3xu5.evil.666@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'Pillow', 'pydub'],
    keywords=['python', 'image', 'audio', 'steganography'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
