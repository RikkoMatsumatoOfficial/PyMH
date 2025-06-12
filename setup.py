from setuptools import setup
import setuptools

setup(
    name="PyMH",
    version="0.1",
    author="RikkoMatsumatoOfficial",
    packages=setuptools.find_packages(),
    package_data={
        '': ['x64\\*.dll'],
        '': ['x32\\*.dll'],
    }
    description="This is My First Python Library For MinHook(Created by TsudaKageyo)... So Enjoy to use this my Python Library!!!"
)