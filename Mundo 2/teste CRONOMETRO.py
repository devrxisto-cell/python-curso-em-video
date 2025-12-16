import time

start = input("Quer começar? (S/N): ").strip().upper()

if start == "S":
    for minute in range(0, 1):  # só 1 minuto, nesse exemplo
        for second in range(0, 60):
            print(f"{minute}:{second:02d}")
            time.sleep(1)
    print("⏰ Um minuto completo!")
else:
    print("Tente de novo!")
