import argparse
import struct

parser = argparse.ArgumentParser(description="Decode a BIG-IP LTM cookie value")
parser.add_argument("-c", "--cookie", type=str, required=True, help="The cookie value to decode")
args = parser.parse_args()

ip, port = struct.unpack(">LH", struct.pack("<LH", *map(int, args.cookie.split(".")[:2])))
print(f"IP: {ip >> 24}.{ip >> 16 & 0xff}.{ip >> 8 & 0xff}.{ip & 0xff}")
print(f"Port: {port}")

#https://my.f5.com/manage/s/article/K6917
