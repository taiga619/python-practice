#include <stdio.h>
#include <stdint.h>

typedef struct {
    volatile uint32_t ctrl;
    volatile uint32_t count;
    volatile uint32_t load;
    volatile uint32_t status;
} TimerRegs;

#define CTRL_EN (1u << 0)
#define CTRL_MODE (1u << 1)
#define CTRL_IRQ_EN (1u << 2)
#define STATUS_EXPIRED (1u << 0)

#define Timer ((TimerRegs *)0x50000000)

void timer_start(uint32_t load_value){
    Timer -> load = load_value;
    Timer -> ctrl |= (CTRL_EN | CTRL_IRQ_EN);
}
void timer_stop(void){
    Timer -> ctrl &= ~CTRL_EN;
}