from myhdl import block, Signal

from ClkDriver import ClkDriver
from LEDBlink import LEDBlink

@block
def LED_Blinker():
    clk = Signal(0)
    clkdriver = ClkDriver(clk)
    blink = LEDBlink(clk)

    return clkdriver, blink

inst = LED_Blinker()
inst.run_sim(50)
