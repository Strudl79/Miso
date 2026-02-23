#!/bin/python
import struct

def vytvor_subor():
    magic = b"{MAG"
    verzia = 1
    sirka = 79
    vyska = 24
    znak = b"q"
    
    with open("example.cimg", "wb") as subor:
        subor.write(magic)
        subor.write(verzia.to_bytes(8, "little"))
        subor.write(sirka.to_bytes(4, "little"))
        subor.write(vyska.to_bytes(4, "little"))
        subor.write((sirka * vyska) * znak)

if __name__ == "__main__":
    vytvor_subor()
