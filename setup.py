from setuptools import setup, find_packages

VERSION = '1.0.1'
DESCRIPTION = 'Test websites for slow loris'
LONG_DESCRIPTION = 'A package that allows you to test websites for the slow loris vulnerability'

# Setting up
setup(
    name="PyLorisPyPITest",
    version=VERSION,
    author="YoloFTW",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'slow loris', 'test', 'loris', 'slow lorris'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)