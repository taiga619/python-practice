#include "tmr.h"
#include <stdio.h>

int main(void){
    TmrRegs fake = {0, 0, 0, 3};
    tmr_init(&fake, 1000, 1);
    printf("load=%u ctrl=%u\n", (unsigned)fake.load, (unsigned)fake.ctrl);
    tmr_start(&fake);
    printf("ctrl=%u\n", (unsigned)fake.ctrl);
    printf("EXPIRED=%d\n", tmr_expired(&fake));
    tmr_clear_expired(&fake);
    printf("status=%u\n", (unsigned)fake.status);
    tmr_stop(&fake);
    printf("ctrl=%u\n", (unsigned)fake.ctrl);
    return 0;
}