#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Doc."""

import os
# import pytest

from dotenv import load_dotenv


def test_env_abc():
    load_dotenv()
    abc_key = os.getenv('ABC_KEY')

    assert abc_key == "1234xyz"
