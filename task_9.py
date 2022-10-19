salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
extra_money = 0 # количество трат каждый месяц

for month in range(months + 1):
    extra_money = spend + (spend * (1 + increase) ** month) - salary
    while month < 11:
        need_money += extra_money

print(round(need_money))
