import socket
import threading
from unittest import TestCase, main as unittest_main

from pyturn.turn_client import TurnClient


def remove_trailing_null_bytes(data: bytes) -> bytes:
    last_non_null_index = len(data)
    for i in range(len(data) - 1, -1, -1):
        if data[i] != 0:
            break
        last_non_null_index = i
    return data[:last_non_null_index]


def receive_data_from_udp_port(port: int, buffer_size: int = 1024) -> bytes:
    receiving_data = b""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        # Bind the socket to the specified port
        udp_socket.bind(('127.0.0.1', port))
        print(f"Listening for UDP packets on port {port}...")
        while True:
            data, address = udp_socket.recvfrom(buffer_size)
            receiving_data += TurnClient.parse_data(data)
            receiving_data = remove_trailing_null_bytes(receiving_data)
            if receiving_data[-3:] == b"end":
                print(f"receiving data {receiving_data[:-3]}")
                udp_socket.close()
                return receiving_data


class TestTurnClient(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.turn_client1 = TurnClient("127.0.0.1", 12345, password="MTIzNDU2Nzg5MA==", username="1709740831",
                                      is_fingerprint=True)
        cls.turn_client2 = TurnClient("127.0.0.1", 12346, password="MTIzNDU2Nzg5MA==", username="1709740831")
        cls.turn_client1.turn_allocate_request("0.0.0.0", 3478, lifetime=777, even_port=True, dont_fragment=True)
        cls.turn_client2.turn_allocate_request("0.0.0.0", 3478)
        cls.channel_number = 0x4004

    def test_turn_send(self):
        self.turn_client1.turn_create_permission("0.0.0.0", 3478, self.turn_client1.trans_id,
                                                 self.turn_client2.relayed_ip,
                                                 self.turn_client2.relayed_port)
        self.turn_client2.turn_create_permission("0.0.0.0", 3478, self.turn_client2.trans_id,
                                                 self.turn_client1.relayed_ip,
                                                 self.turn_client1.relayed_port)
        receive_thread = threading.Thread(target=receive_data_from_udp_port, args=(12346,))
        receive_thread.start()
        self.turn_client1.turn_send("0.0.0.0", 3478, self.turn_client1.trans_id, self.turn_client2.relayed_ip,
                                    self.turn_client2.relayed_port, b"data1 end")
        receive_thread.join()

    def test_turn_channel_send(self):
        self.turn_client1.turn_create_permission("0.0.0.0", 3478, self.turn_client1.trans_id,
                                                 self.turn_client2.relayed_ip,
                                                 self.turn_client2.relayed_port)
        self.turn_client2.turn_create_permission("0.0.0.0", 3478, self.turn_client2.trans_id,
                                                 self.turn_client1.relayed_ip,
                                                 self.turn_client1.relayed_port)
        self.turn_client1.turn_channel_bind("0.0.0.0", 3478, self.turn_client1.trans_id, self.turn_client2.relayed_ip,
                                            self.turn_client2.relayed_port, self.channel_number)
        receive_thread = threading.Thread(target=receive_data_from_udp_port, args=(12346,))
        receive_thread.start()
        self.turn_client1.turn_channel_send("0.0.0.0", 3478, self.channel_number, b"|hello from channel end")
        receive_thread.join()

    @classmethod
    def tearDownClass(cls):
        cls.turn_client1.turn_delete_allocation("0.0.0.0", 3478, cls.turn_client1.trans_id)
        cls.turn_client2.turn_delete_allocation("0.0.0.0", 3478, cls.turn_client2.trans_id)


if __name__ == '__main__':
    unittest_main()
