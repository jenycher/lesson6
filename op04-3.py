def bank(a, years):
  interest_rate = 0.10  # Годовая процентная ставка (10%)
  total = a
  for _ in range(years):
      total += total * interest_rate
  return total

# Пример использования функции
initial_deposit = float(input("Введите размер вклада: "))
deposit_years = int(input("Введите срок вклада в годах: "))
result = bank(initial_deposit, deposit_years)
print(f"Сумма на счету пользователя через {deposit_years} лет составит {result:.2f} рублей")
#В этой функции происходит итерация по каждому году в течение заданного срока вклада years, и к сумме вклада добавляется процентная ставка за каждый год. Функция возвращает итоговую сумму на счету пользователя после указанного количества лет.