#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Doc."""

import os
import unittest

from dotenv import load_dotenv

load_dotenv()

abc_key = os.getenv('ABC_KEY')

# print(abc_key)


class TestEnvVar(unittest.TestCase):
    """Run unit tests."""

    async def test_env_abs(self):
        """Test google_top_link."""
        print(abc_key)
        self.assertEqual(abc_key, "1234xyz")
