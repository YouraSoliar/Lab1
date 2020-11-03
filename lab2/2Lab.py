print("Перша константа", False)
print("Друга константа", True)
print("Третя константа", None)

numbers = [1,2,3]
sumOfNumbers = sum(numbers)
print("\nРезультат функції sum() - ", sumOfNumbers)

A = True
if A:
    print("\nЗначить А=True\n")
else:
    print("\nЗначить А=False\n")

try:
    print("Введіть число ")
    x = int (input())
except ValueError:
    print("Ви ввели не число")
    x = 0
finally:
    print("А вот воно що!")

with open("README.md", "r") as f:
    for line in f:
        print(line)

this_is_lambda = lambda first, second: f'Цей код написав суму: {first + second}'
print("Це просто функція - ", this_is_lambda)
print("Це її виклик - ", this_is_lambda(1, 3))
