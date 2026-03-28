def average(a, b, c, d, e):
    avg = (a + b + c + d + e) / 5
    return avg

a = float(input("Enter Math: "))
b = float(input("Enter Science: "))
c = float(input("Enter English: "))
d = float(input("Enter History: "))
e = float(input("Enter Chinese: "))

print("Your Score is = ",average(a,b,c,d,e))