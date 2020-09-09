import pyshark
import unittest
from test2function import to_audio

class TestAudio (unittest.TestCase):
    def test_audio(self):
        res_audio = to_audio('input_file.pcap','rtp')
        with open ('out.raw','rb') as f:
            raw_data = f.read()

        self.assertAlmostEqual(res_audio,raw_data.hex())

if __name__ == '__main__':
    unittest.main()
