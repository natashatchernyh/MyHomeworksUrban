numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_primes = []
not_primes = []

for i in numbers:
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            not_primes.append(i)
            break
    if flag == True and i != 1:
        is_primes.append(i)

#          continue                        мой вариант
#   if (is_prime):
#       if (i != 1):
#            is_primes.append(i)
#    else:
#        not_primes.append(i)

print('Primes: ', is_primes)
print('Not-Primes: ', not_primes)







