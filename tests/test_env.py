#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Doc."""

import os
# import pytest

from dotenv import load_dotenv

from utils.youtube import search_youtube


def test_env_abc():
    load_dotenv()
    abc_key = os.getenv('ABC_KEY')

    assert abc_key == "1234xyz"


def test_search_youtube():
    res = search_youtube("never gonna give you up", 1)[0]
    print(res)
    assert res['title'] == "Rick Astley - Never Gonna Give You Up (Video)"
    assert res['type'] == "video"
    assert res['id'] == "dQw4w9WgXcQ"
