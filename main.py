# 11
n = int(input())
for i in range(2, n):
    if n % i == 0:
        print("Tub emas")
        break
else:
    print("Tub")

# 12
lst = list(map(int, input().split()))
print(sum(lst))

# 13
lst = list(map(int, input().split()))
print(min(lst))

# 14
matn = input()
print(matn.count("a"))

# 15
n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
