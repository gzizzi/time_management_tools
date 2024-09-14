#! /usr/bin/env python3

# nota: si può variare la durata degli intervalli in runtime
# python3
# >>> import sys
# >>> sys.path.append('/Users/administrator/time_management_tools')
# >>> from pomodoro_timer import pomodoro_timer
# >>> pomodoro_timer(25, 5, 15, 10)
# >>> pomodoro_timer(work_duration=30, short_break=10, long_break=20, cycles=4)

# to do
# facilitare il cambio degli intervalli con delle opzioni (ne vale la pena?)
# aggiungere un segnale luminoso e visivo allo scadere del tempo
# includere in timer.py
# 
# per come è fatto ora si ferma dopo cycles
#

import time

def pomodoro_timer(work_duration=25, short_break=5, long_break=15, cycles=4):
    try:
        for cycle in range(1, cycles + 1):
            print(f"Pomodoro {cycle} - Lavora per {work_duration} minuti.")
            countdown(work_duration * 60)  # Converte i minuti in secondi
            if cycle < cycles:
                print(f"Pausa breve - Riposa per {short_break} minuti.")
                countdown(short_break * 60)
            else:
                print(f"Pausa lunga - Riposa per {long_break} minuti.")
                countdown(long_break * 60)

    except KeyboardInterrupt:
        print(f"\nok, pausa lunga...")

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Tempo scaduto!")

if __name__ == "__main__":
    pomodoro_timer()
