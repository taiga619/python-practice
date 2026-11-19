#ifndef TMR_H
#define TMR_H

#include <stdint.h>

typedef struct{
    volatile uint32_t ctrl;
    volatile uint32_t load;
    volatile uint32_t count;        
    volatile uint32_t status;
} TmrRegs;

#define CTRL_EN         (1u << 0)
#define CTRL_MODE       (1u << 1)
#define CTRL_IRQ_EN     (1u << 2)
#define STATUS_EXPIRED  (1u << 0)

#define TMR_BASE    0x50000000u
#define TMR         ((TmrRegs *)TMR_BASE)  

void tmr_init(TmrRegs *r, uint32_t load, int periodic);
void tmr_start(TmrRegs *r);
void tmr_stop(TmrRegs *r);
int tmr_expired(TmrRegs *r);
void tmr_clear_expired(TmrRegs *r);

#endif