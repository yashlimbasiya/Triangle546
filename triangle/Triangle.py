def classifyTriangle(a,b,c):

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'       
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'   
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):  #checking if its an integer
        return 'InvalidInput'
    if a >= b + c or b >= a + c or c >= a + b:
        return 'NotATriangle'       
    if a == b and b == c:
        return 'Equilateral'
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return 'Right'
    elif a != b and b != c and a != b:
        return 'Scalene'
    else:
        return 'Isosceles'
