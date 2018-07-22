#!/usr/bin/env python2

import binascii
import fractions

from pwn import *
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import pubkey, RSA

HOST = "localhost"
PORT = 5000


def find_common_gcd(nums):
    """Try to find two numbers in the set that share a common gcd.

    :return: A tuple (i,j,gcd) of indices that share a common gcd.
    """
    for i in xrange(len(nums)):
        for j in xrange(1, len(nums)):
            if i == j:
                continue

            gcd = fractions.gcd(nums[i], nums[j])
            if gcd != 1:
                return (i, j, gcd)

    return None


def main():
    # collect a few public keys
    keys = []
    flags = []
    for i in range(20):
        conn = remote(HOST, PORT)
        conn.recvuntil("key:\n")
        keystr = conn.recvuntil("And here", drop=True)
        key = RSA.importKey(keystr)
        keys.append(key)

        conn.recvuntil(":)\n")
        flagstr = conn.recvline().strip()
        flag = binascii.unhexlify(flagstr)
        flags.append(flag)

        conn.close()

    # Try to find two n's with a common GCD
    nums = [k.n for k in keys]
    i, j, gcd = find_common_gcd(nums)
    log.info("Found GCD! gcd({:d}, {:d}) = {:d}".format(i, j, gcd))

    p = gcd
    q = keys[i].n / gcd
    d = pubkey.inverse(65537, (p-1)*(q-1))
    privkey = RSA.construct((keys[i].n, 65537L, d))
    cipher = PKCS1_OAEP.new(privkey)
    flag = cipher.decrypt(flags[i])
    log.success("Flag: {:s}".format(flag))


if __name__ == "__main__":
    main()
