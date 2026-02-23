#!/bin/python
import struct
with open("example.cimg", "wb") as f:
    f.write(b"cIMG")      
    f.write((1).to_bytes(4,"little"))
    f.write((25).to_bytes(2,"little"))
    f.write((11).to_bytes(4,"little"))

    f.write(b"A" * (25*11))        
