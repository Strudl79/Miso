Najskôr som si pozrel /challenge/cimg.

Všimol som si, že hlavička má mať veľkosť 4 bajty.

Skúsil som teda pomocou echo zapísať do súboru example.cimg reťazec „abcd“,
ale program mi vypísal chybu, že magic number nie je správny.

Potom som si /challenge/cimg prešiel ešte raz a zistil som,
že magic number musí byť zapísaný vo forme b"".

Keď som to takto upravil, program už fungoval bez problémov
(/challenge/cimg example.cimg).
