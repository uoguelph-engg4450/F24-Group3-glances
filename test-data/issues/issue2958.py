# Test cases for hide_threshold_bytes implementation
# Author: Carter Rows
# Date October 20th 2024

import unittest
from unittest.mock import patch, MagicMock
from glances.plugins.diskio import PluginModel

class TestDiskIOPlugin(unittest.TestCase):

    @patch('psutil.disk_io_counters')
    def test_hide_small_writes(self, mock_disk_io_counters):
        # mimic the disk i/o counters with small arbitrary write size
        mock_disk_io_counters.return_value = {
            'sda': MagicMock(write_bytes = 14 * 1024)
        }

        plugin = PluginModel(args = None, config = None)
        # set threshold to 32 kb
        plugin.hide_threshold_bytes = 32 * 1024

        stats = plugin.update_local()

        # assert no stats are recorded since write is smaller than 32 kb
        self.assertEqual(len(stats), 0)

    @patch('psutil.disk_io_counters')
    def test_show_large_writes(self, mock_disk_io_counters):
        # mimic the disk i/o counters with larger than threshold size 40kb
        mock_disk_io_counters.return_value = {
            'sda': MagicMock(write_bytes = 40 * 1024)
        }

        plugin = PluginModel(args = None, config = None)
        # set threshold to 32 kb
        plugin.hide_threshold_bytes = 32 * 1024

        stats = plugin.update_local()

        # assert that the write is recorded since we are larger than threshold
        self.assertGreater(len(stats), 0)
        self.assertEqual(stats[0]['write_bytes'], 40 * 1024)

    @patch('psutil.disk_io_counters')
    def test_no_threshold(self, mock_disk_io_counters):
        # mimic the disk i/o counters with any size of write
        mock_disk_io_counters.return_value = {
            'sda': MagicMock(write_bytes = 14 * 1024)
        }

        plugin = PluginModel(args = None, config = None)
        # no threshold
        plugin.hide_threshold_bytes = None

        stats = plugin.update_local()

        # assert that the write is recorded even without a threshold
        self.assertGreater(len(stats), 0)

if __name__ == '__main__':
    unittest.main()