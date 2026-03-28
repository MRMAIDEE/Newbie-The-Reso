def deposit(d, rate, months):
    r = rate / 100
    total = d * (1 + r) ** months
    return total
d = float(input("Enter Your Deposit: "))

r = float(input("Enter interest: "))

months = int(input("Enter Months: "))

print("Total is= ",deposit(d, r, months))
