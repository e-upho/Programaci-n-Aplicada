import csv
import time

t = 0.0
step = 0.01

with open("infinito.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["t", "x"]) 

    try:
        while True:
            x = 1 - (1 / (1 + t))
            writer.writerow([x])
            print(f"x = {x:.10f}")
            time.sleep(0.05)
            t += step
    except KeyboardInterrupt:
        print("\nProceso interrumpido. Datos guardados en 'infinito.csv'.")