from unittest import TestCase, main as unittest_main

from pyturn.stun_client import StunClient


class TestStunClient(TestCase):
    def setUp(self):
        self.stun_client = StunClient("0.0.0.0", 12345, is_fingerprint=True)

    def test_stun_request(self):
        print(self.stun_client.stun_request("142.251.98.127", 19302))


if __name__ == '__main__':
    unittest_main()
