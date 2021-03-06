#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from distutils.core import setup


__author__ = "Patrick Hohenecker"
__copyright__ = (
        "Copyright (c) 2018, Patrick Hohenecker\n"
        "All rights reserved.\n"
        "\n"
        "Redistribution and use in source and binary forms, with or without\n"
        "modification, are permitted provided that the following conditions are met:\n"
        "\n"
        "1. Redistributions of source code must retain the above copyright notice, this\n"
        "   list of conditions and the following disclaimer.\n"
        "2. Redistributions in binary form must reproduce the above copyright notice,\n"
        "   this list of conditions and the following disclaimer in the documentation\n"
        "   and/or other materials provided with the distribution.\n"
        "\n"
        "THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS \"AS IS\" AND\n"
        "ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED\n"
        "WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\n"
        "DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR\n"
        "ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n"
        "(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n"
        "LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND\n"
        "ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n"
        "(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS\n"
        "SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
)
__license__ = "BSD-2-Clause"
__version__ = "2018.1"
__date__ = "Aug 21, 2018"
__maintainer__ = "Patrick Hohenecker"
__email__ = "mail@paho.at"
__status__ = "Development"


# read the long description from the read me file
long_description = open("README.md").read()


setup(
        author="Patrick Hohenecker",
        author_email="mail@paho.at",
        classifiers=[
                "Programming Language :: Python :: 3.6",
                "Programming Language :: Python :: 3.7"
        ],
        copyright="Copyright (c) 2018 Patrick Hohenecker",
        data_files=[
                (".", ["LICENSE", "README.md"])
        ],
        description="A PyTorch implementation of the Transformer model from \"Attention Is All You Need\".",
        install_requires=[
                "insanity>=2017.1",
                "numpy>=1.15.0",
                "torch>=0.4.1"
        ],
        license="BSD-2-Clause",
        long_description=long_description,
        name="transformer",
        package_dir={"": "src/main/python"},
        packages=[
                "transformer",
                "transformer.bert"
        ],
        python_requires=">=3.6",
        url="https://github.com/phohenecker/pytorch-transformer",
        version="2018.1"
)
