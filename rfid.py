from educator import *
import time

allowed_uid = bytearray(b'\x96\xfd\xe1\xbd')

def tit_tut():
    beep.time(150)  
    time.sleep(0.1)

    beep.time(400)  
    time.sleep(0.1)

    beep.time(150)  
    time.sleep(0.1)

    beep.time(400)  

while True:

    uid = Port1.read_RFID()

    if uid:

        print("UID =", uid)

        if uid == allowed_uid:

            oled.print(1, 1, "Akses Diterima", clear_row=1)
            beep.time(200)

            Port3.output_IO(pin=1, value=0)

            # BUKA PINTU
            Port2.servo_angle(2, 90)
            time.sleep(5)

            # TUTUP PINTU
            Port2.servo_angle(2, 0)

        else:

            oled.print(1, 1, "Akses Ditolak", clear_row=1)
            
            tit_tut()
            Port3.output_IO(pin=1, value=1)
            
            time.sleep(2)
            Port3.output_IO(pin=1, value=0)
            
            time.sleep(2)
            Port3.output_IO(pin=1, value=1)
            
            time.sleep(2)
            Port3.output_IO(pin=1, value=0)
            
        time.sleep(1)

    time.sleep(0.1)
