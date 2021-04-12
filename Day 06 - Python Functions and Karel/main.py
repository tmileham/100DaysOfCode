total = 0

# Finding even numbers using modular sign
for nums in range(1,101):
    if nums % 2 == 0:
        total += nums

print(total)

total = 0
for nums in range (2,102,2):
    total += nums

print(total)