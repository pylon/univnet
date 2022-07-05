#!/usr/bin/env python

from distutils.core import setup

setup(
    name="univnet",
    version="0.1.1",
    description=("Unofficial PyTorch Implementation of UnivNet Vocoder"),
    url="https://github.com/pylon/univnet/",
    author="azraelkuan",
    packages=["univnet"],
    data_files=[("univnet", ["pretrained/univ_c32_0288.pt"])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
