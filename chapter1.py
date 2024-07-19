import math

### ex. 9 ###
def factorial(num):
    from math import factorial   
    print(factorial(num))

factorial(6)

### ex. 10 ###
def is_LeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def leapYear(year1, year2):
    counter = 0
    for year in range(year1, year2):
        if is_LeapYear(year):
            counter += 1
        
    print("number of leap years between the years 1500 - 2010:" , counter)

leapYear(1500, 2010)

### ex. 11 ###
def factorial(n):
    return math.factorial(n)  

def ramanujan_pi_approximation(N):
    sum = 0
    for k in range(N+1):
        num = factorial(4*k) * (1103 + 26390*k)
        denom = (factorial(k)**4) * (396**(4*k))
        sum += num / denom
    
    factor = (2 * math.sqrt(2)) / 9801
    pi_approx = 1 / (factor * sum)
    return pi_approx

pi_approx_N0 = ramanujan_pi_approximation(0)
print("Approximation of π for N=0:", pi_approx_N0)
pi_approx_N1 = ramanujan_pi_approximation(1)
print("Approximation of π for N=1:", pi_approx_N1)
print("Python's stored value of π:", math.pi)

### ex. 13 ###
def verify_trig_identity(x):
    sin_squared = math.sin(x) ** 2
    cos_squared = math.cos(x) ** 2
    return sin_squared + cos_squared

values_of_x = [math.pi, math.pi / 2, math.pi / 4, math.pi / 6]

for x in values_of_x:
    result = verify_trig_identity(x)
    print(f"sin^2({x}) + cos^2({x}) = {result}")

for x in values_of_x:
    result = verify_trig_identity(x)
    print(f"For x = {x}: sin^2(x) + cos^2(x) = {result} (should be 1)")

### ex. 14 ###
degrees = 87
radians = math.radians(degrees)
sin_87 = math.sin(radians)

print(f"sin(87°) = {sin_87}")

### ex. 19 ###
def evaluate_expression(P, Q):
    return (P and Q) or (P and (not Q))

def find_conditions():
    conditions = []
    for P in [True, False]:
        for Q in [True, False]:
            if not evaluate_expression(P, Q):
                conditions.append((P, Q))
    return conditions

false_conditions = find_conditions()
print("Conditions for which (P AND Q) OR (P AND (NOT Q)) is false:")
for P, Q in false_conditions:
    print(f"P = {P}, Q = {Q}")

### ex. 22 ###
result = math.exp(2 * math.sin(math.pi / 6)) + math.log(3) * math.cos(math.pi / 9) - 5**3
print("Result of the expression:", result)

