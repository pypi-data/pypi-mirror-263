from setuptools import setup, find_packages

setup(
    name="kurumii_nokeyboard",
    version="1.3.2",
    packages=find_packages(),
    install_requires=[
        "pytube",
        "moviepy",
        "requests"
    ],
    author="Kurumii",
    description="A handy litle tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)