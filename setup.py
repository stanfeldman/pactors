from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "pactors",
    version = "0.0.1",
    author = "Stanislav Feldman",
    description = ("Python actors library"),
    url = "https://github.com/stanislavfeldman/pactors",
    keywords = "utils actors",
    packages=['pactors'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development"
    ],
)
