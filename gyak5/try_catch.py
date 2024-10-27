try:
    print(5 / 0)
except ZeroDivisionError:
    print("Zéróosztó")
finally:
    print("(VÉGE)")