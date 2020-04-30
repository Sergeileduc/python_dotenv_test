#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Doc."""

import os

from dotenv import load_dotenv


def use_dotenv():
    load_dotenv()
    return os.getenv('ABC_KEY')


abc = use_dotenv()
print(abc)
