"""Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line."""

result =[]

for x in range(1000,3000):
    x = str(x)
    digit_even = True
    for i in range(len(x)):
       if int(x[i])%2 != 0:
           digit_even = False
    if digit_even:
        result.append(x)

print(','.join(result))
