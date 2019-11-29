#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Doc."""

import os

from dotenv import load_dotenv

load_dotenv()

abc_key = os.getenv('ABC_KEY')

print(abc_key)
