def sum_range(start, end):
  
  total = 0
  for num in range(start, end + 1):
      total += num
  return total

# Пример использования функции
start = int(input("Введите начальное значение диапазона: "))
end = int(input("Введите конечное значение диапазона: "))
result = sum_range(start, end)
print(f"Сумма всех целых чисел в указанном диапазоне равна {result}")