def average (a, b, c, d, e):
    avg = (a + b + c + d + e) / 5
    return avg

a = float(input("Enter Score Math: "))
b = float(input("Enter Score Chinese: "))
c = float(input("Enter Score Science: "))
d = float(input("Enter Score History: "))
e = float(input("Enter Score English: "))

print("Average Score is= ",average(a, b, c, d, e))
