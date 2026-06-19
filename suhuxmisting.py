from educator import *
import time

BATAS_KELEMBAPAN = 20

while True:
    try:
        #SENSOR SUHU
        suhu, hum = Port1.DHT11(pin=1)

        print("Suhu:", suhu)
        print("Kelembapan:", hum)

        oled.print(1, 1, f"Temp:{suhu}C", clear_row=1)
        oled.print(2, 1, f"Hum :{hum}%", clear_row=1)

        if hum < BATAS_KELEMBAPAN:
            oled.print(3, 1, "Pompa ON", clear_row=1)

            # Nyalakan pompa
            Port2.output_IO(pin=1, value=1)

            beep.time(200)

            time.sleep(10)

            # Matikan pompa
            Port2.output_IO(pin=1, value=0)

        else:
            oled.print(3, 1, "Pompa OFF", clear_row=1)
            Port2.output_IO(pin=1, value=0)

        time.sleep(30)

    except Exception as e:
        print(e)
        time.sleep(1)
