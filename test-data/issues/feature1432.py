# Author: Carter Rows
# Date November 25th 2024
# Tests for feature 1432
# Config options in glances.conf

import unittest
from unittest.mock import patch, MagicMock
from glances.config import Config
from glances.main import parse_args

# test class for short name configuration option
class TestProcessShortName(unittest.TestCase):
    @patch('glances.config.Config.read')
    def test_short_name_config(self, mock_read):
        # create the mock config file
        mock_read.return_value = None
        config = Config()
        config.parser.add_section('processlist')
        # set short_name to true for testing
        config.parser.set('processlist', 'short_name', 'true')

        # check if it was parsed correctly
        self.assertTrue(config.get_bool_value('processlist', 'short_name', default=False))

# test class for irq (sensors) plugin configuration option
class TestIRQPlugin(unittest.TestCase):
    @patch('glances.config.Config.read')
    def test_irq_config(self, mock_read):
        # create mock config file
        mock_read.return_value = None
        config = Config()
        config.parser.add_section('irq')
        # set disable to false for testing
        config.parser.set('irq', 'disable', 'false')

        # check if it was parsed correctly
        self.assertFalse(config.get_bool_value('irq', 'disable', default=True))

# test class for update interval configuration option
class TestUpdateInterval(unittest.TestCase):
    @patch('glances.config.Config.read')
    def test_update_interval_config(self, mock_read):
        # create mock config file
        mock_read.return_value = None
        config = Config()
        config.parser.add_section('irq')
        # set refresh rate to 10 seconds for testing
        config.parser.set('global', 'refresh', '10')

        # check if it was parsed correctly
        self.assertEqual(config.get_int_value('global', 'refresh', default=2), 10)