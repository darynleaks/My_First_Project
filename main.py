income = 202, 118, 2250, 1680, 1075, 80
print (
    """
Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80"""
)
print()
balance = sum(income)
print(f"Income: ${balance}")
staff = input('Staff expenses:\n')
staff1 = int(staff)
other = input('Other expenses:\n')
other1 = int(other)
balance -= (staff1 + other1)
print(f'Net income: ${balance}')