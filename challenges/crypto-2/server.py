#!/usr/bin/env python3

import binascii
import random
import socketserver
import time

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import pubkey, RSA
from Crypto.Util.number import getStrongPrime

HOST = "0.0.0.0"
PORT = 5000

print("[*] Generating primes")
PRIMES = [getStrongPrime(1024) for _ in range(20)]


class CryptoService(socketserver.BaseRequestHandler):

    def handle(self):
        print("[*] Connection from {:s}:{:d}".format(*self.client_address))

        e = 65537
        p, q = random.sample(PRIMES, 2)
        n = p * q
        d = pubkey.inverse(e, (p-1)*(q-1))
        public = RSA.construct((n, e))
        privkey = RSA.construct((n, e, d))
        cipher = PKCS1_OAEP.new(privkey)

        self.request.sendall(b"Here's your public key:\n")
        self.request.sendall(public.exportKey() + b"\n")

        self.request.sendall(b"And here's the flag! :)\n")
        with open("flag.txt", "rb") as f:
            flag = f.read()
        ct = cipher.encrypt(flag)
        self.request.sendall(binascii.hexlify(ct) + b"\n")


def main():
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer((HOST, PORT), CryptoService)
    server.daemon_threads = True

    print("[+] Server started")
    server.serve_forever()


if __name__ == "__main__":
    main()
