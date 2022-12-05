#ProjectEuler 2 => Even Fibonacci Numbers

fib = [1,2]
i = 2
sum = 0
while True:
    if fib[i-2] + fib[i-1] < 4000000:
        fib.append(fib[i-2] + fib[i-1])
        i+=1
    else:
        break
for j in fib:
    if j%2==0:
        sum+=j

print(fib)
print(sum)