def cheak(score):
    if score >=100:
        return "A"
    elif score >= 90:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C+"
    elif score >= 80:
        return "C"
    elif score >= 80:
        return "D+"
    elif score >= 80:
        return "D"
    else :
        return "ມືງແມ່ງກາກສັສ"
    
    


s = float(input("Inter Your Score: "))

print("Your Score is ",cheak(s))