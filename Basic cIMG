#include <stdio.h>
#include <stdint.h>

int main() {
    FILE *f = fopen("example.cimg", "wb");
    if (!f) return 1;

    fwrite("cIMG", 1, 4, f);

    uint32_t val32 = 2;
    fwrite(&val32, 4, 1, f);

    uint64_t val64_1 = 75;
    fwrite(&val64_1, 8, 1, f);

    uint64_t val64_2 = 22;
    fwrite(&val64_2, 8, 1, f);

    unsigned char pixel[4] = {0x8C, 0x1D, 0x40, 'A'};

    int count = 75 * 22;
    for (int i = 0; i < count; i++) {
        fwrite(pixel, 1, 4, f);
    }

    fclose(f);
    return 0;
}
