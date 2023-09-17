1
a = int(input())
b = int(input())
c = int(input())
s = a + b + c
print(s)

2
a = int(input())
b = int(input())
print(a * b / 2)
3 
n = int(input())
k = int(input())
print(k // n)
print(k % n)
4 
n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)
5
print('Hello, ' + input() + '!')
6
след и пред
n = int(input())
print('The next number for the number ' + str(n) + ' is ' + str(n + 1) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(n - 1) + '.')
7
a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)
8 
a = int(input())
b = int(input())
L = int(input())
N = int(input())
print(2 * L + (2 * N - 1) * a + 2 * (N - 1) * b)