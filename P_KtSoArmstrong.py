def is_armstrong(num):
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))

num = int(input("Nhập số nguyên: "))
if is_armstrong(num):
    print(f"{num} là số Armstrong")
else:
    print(f"{num} không phải là số Armstrong")
    