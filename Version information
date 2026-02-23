#!/bin/python

def zapis_cimg_subor(nazov_suboru="example.cimg"):
    magic_hlavicka = b"(m6E"
    verzia_cislo = 225
    with open(nazov_suboru, "wb") as subor:
        subor.write(magic_hlavicka)
        subor.write(verzia_cislo.to_bytes(1, "little"))

if __name__ == "__main__":
    zapis_cimg_subor()
