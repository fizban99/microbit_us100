from microbit import uart, pin14, pin15, sleep
from sys import print_exception


class US100:

    def __init__(self, tpin=pin15, rpin=pin14):
        self.tx_pin = tpin
        self.rx_pin = rpin

    def distance_mm(self):
        try:
            uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=self.tx_pin, rx=self.rx_pin)
            sleep(1)
            uart.write(b'\x55')
            t = 0
            buf = bytearray(2)
            while not uart.any() and t < 1000:
                t = t + 1
                sleep(5)
            if t < 1000:
                uart.readinto(buf, 2)
            uart.init(115200)
            dist = buf[0] * 256 + buf[1]
            if dist > 1100:
                dist = -1
            return dist
        except Exception as exc:
            uart.init(115200)
            print_exception(exc)

    def temperature(self):
            try:
                uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=self.tx_pin, rx=self.rx_pin)
                sleep(1)
                uart.write(b'\x50')
                t = 0
                buf = bytearray(1)
                while not uart.any() and t < 1000:
                    t = t + 1
                    sleep(5)
                if t < 1000:
                    uart.readinto(buf, 1)
                uart.init(115200)
                return(buf[0] - 45)
            except Exception as exc:
                uart.init(115200)
                print_exception(exc)