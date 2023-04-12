import argparse
from my_rsa import rsa_encrypt, rsa_decrypt, rsa_gen_keys
import math

def sign(msg, n, e):
    h = hash(msg)
    return rsa_encrypt(n, e, h)

def verify(msg, signature, n, d):
    h = rsa_decrypt(n, d, signature)
    return hash(msg) == h 

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
            message = r.read()

        with open(args.output, 'w') as f:
            f.write(sign(message, n, d))

    elif args.command == "verify":
        with open(args.key, 'r') as f:
            n, _, _, e, d = [int(x) for x in f.read().split()]

        with open(args.input, 'r') as f:
            message = r.read()

        with open(args.output, 'w') as f:
            f.write(sign(message, n, d))


    s = "hello world"
    m = int.from_bytes(s.encode(), byteorder='little')

    n, _, _, e, d = rsa_gen_keys()

    me = rsa_encrypt(n, e, m)
    md = rsa_decrypt(n, d, me)

    length = math.ceil(md.bit_length() / 8)
    sd = md.to_bytes(length, byteorder='little').decode()