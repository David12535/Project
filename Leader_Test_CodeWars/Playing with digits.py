#Playing with digits
def dig_pow(n, p):
    sum = 2 
    for num in str(n):
        sum += int(num) ** p
        p += 1
    if sum // n == 0:
        return int(sum / n)
    else:
        return -1