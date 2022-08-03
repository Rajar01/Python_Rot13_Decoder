#!/usr/bin/python

import sys

def main():
    
    if(len(sys.argv) < 2):
        print("Error: Missing argument \"Encoded Rot13 String\"")
        return -1

    encoded_flag = sys.argv[1]
    decoded_flag = ""

    for i in encoded_flag:
        if ord("A") <= ord(i.upper()) <= ord("Z"):
            if (ord("A") <= ord(i) < ord("N")) or (ord("a") <= ord(i) < ord("n")):
                decoded_flag += chr(ord(i) + 13)

            if (ord("N") <= ord(i) <= ord("Z")) or (ord("n") <= ord(i) <= ord("z")):
                decoded_flag += chr(ord(i) - 13)
        else:
            decoded_flag += i

    print(decoded_flag)

if __name__ == "__main__":
   main()
