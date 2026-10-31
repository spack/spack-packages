/* Calls three of the functions crmvec.h declares, from the installed library */
#include <stdint.h>
#include <stdio.h>

#include <crmvec.h>

int main(void)
{
    uint16_t x[2] = {0x0000, 0x3c00}; /* binary16 0 and 1 */
    uint16_t y[2];

    crmvec_f16_exp(x, y, 2); /* 1, and e rounded to binary16 */
    printf("%s %04x %04x %g %g\n", CRMVEC_VERSION, (unsigned)y[0], (unsigned)y[1],
           crmvec_sinpi(0.5), crmvec_pown(2.0, 10));
    return 0;
}
