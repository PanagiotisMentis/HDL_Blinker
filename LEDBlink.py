from myhdl import block, always, now

@block
def LEDBlink(clk):
    @always(clk.posedge)
    def blink():
        print("%s BLINK" % now())

    return blink
