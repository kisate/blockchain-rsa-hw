import argparse
from my_rsa import rsa_encrypt, rsa_decrypt, rsa_gen_keys
import math
import hashlib

def sign(msg, n, e):
    h = int(hashlib.sha1(msg.encode("utf-8")).hexdigest(), 16)
    print(h)
    return rsa_encrypt(n, e, h)

def verify(msg, signature, n, d):
    h = rsa_decrypt(n, d, signature)
    return int(hashlib.sha1(msg.encode("utf-8")).hexdigest(), 16) == h 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--command', choices=['generate', 'sign', 'verify'])
    parser.add_argument('-i', '--input', type=str)
    parser.add_argument('-o', '--output', type=str)
    parser.add_argument('-k', '--key', type=str)
    parser.add_argument('-s', '--sign', type=str)

    args = parser.parse_args()

    if args.command == 'generate':
        with open(args.output, 'w') as f:
            f.write(" ".join(str(x) for x in rsa_gen_keys()))

    elif args.command == 'sign':
        with open(args.key, 'r') as f:
            n, _, _, e, d = [int(x) for x in f.read().split()]

        with open(args.input, 'r') as f:
            message = f.read()

        with open(args.output, 'w') as f:
            f.write(str(sign(message, n, e)))

    elif args.command == "verify":
        with open(args.key, 'r') as f:
            n, _, _, e, d = [int(x) for x in f.read().split()]

        with open(args.input, 'r') as f:
            message = f.read()

        with open(args.sign, 'r') as f:
            signature = int(f.read())

        if verify(message, signature, n, d):
            print("Signature is correct")
        else:
            print("Wrong signature")