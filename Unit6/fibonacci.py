__author__ = 'dmitrijdackov'


dic = {0:0, 1:1}

def fibonacci(n):
    if n in dic:
        return dic[n]

    value = fibonacci(n - 1) + fibonacci(n-2)
    dic[n] = value
    return value

print (fibonacci(36))