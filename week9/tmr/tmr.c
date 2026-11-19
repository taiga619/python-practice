#include "tmr.h"

void tmr_init(TmrRegs *r, uint32_t load, int periodic){
    r -> load = load;
    if(periodic){
        r -> ctrl |= CTRL_MODE;
    }
    else{
        r -> ctrl &= ~CTRL_MODE;
    }
}

void tmr_start(TmrRegs *r){
    r -> ctrl |= CTRL_EN;
}

void tmr_stop(TmrRegs *r){
    r -> ctrl &= ~CTRL_EN;
}
int tmr_expired(TmrRegs *r){
    return (r -> status & STATUS_EXPIRED) != 0;
}

void tmr_clear_expired(TmrRegs *r){
    r -> status = STATUS_EXPIRED;
}