import math

try:
      n = input("Введите номер варианта: ")

      x = 2 * int(n)
      t = 3.5 * int(n)

      z = ((9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - abs(math.sin(t)))) * math.e ** x

      print(f'x: {x}\n'
            f't: {t}\n'
            f'z: {round(z, 3)}')
except Exception as error:
      print("Ошибка при выполнении скрипта:", error)
