
# % 키워드: 숫자 자료형, 숫자 연산자, 연산자, 우선순위

# ! (1) 숫자의 종류
# ? 숫자를 만들려면 그냥 단순히 숫자를 입력하면 됨.
print(123)
# 123

print(123.456)
# 123.456

# ? 숫자에는 두 가지의 종류가 있음. 바로 정수(int)와 실수(float)
print(type(123))
# <class 'int'>

print(type(123.456))
# <class 'float'>

# ? 주의 할 점은 0과 0.0은 다른 타입임
print(type(0))
# <class 'int'>

print(type(0.0))
# <class 'float'>





# ! (2) 숫자 연산자
# ? 사칙연산: =, -, *, /
print("5 + 7 =", 5 + 7)
# 5 + 7 = 12

print("5 - 7 =", 5 - 7)
# 5 - 7 = -2

print("5 * 7 =", 5 * 7)
# 5 * 7 = 35

print("5 / 7 =", 5 / 7)
# 5 / 7 = 0.7142857142857143


# ? 장수 나누기 연산자: //
# ? 정수 나누기 연ㅅ나자는 숫자를 나누고 소수점 이하의 자릿수를 생략시키는 연산자임
print("3 / 2 =", 3 / 2)
# 3 / 2 = 1.5

print("3 // 2 =", 3 // 2)
# 3 // 2 = 1


# ? 나머지 연산자: %
print("5 % 2 =", 5 % 2)
# 5 % 2 = 1


# ? 제곱 연산자: **
print("2 ** 1 =", 2 ** 1)
# 2 ** 1 = 2

print("2 ** 2 =", 2 ** 2)
# 2 ** 2 = 4

print("2 ** 3 =", 2 ** 3)
# 2 ** 3 = 8

print("2 ** 4 =", 2 ** 4)
# 2 ** 4 = 16





# ! (3) 연산자의 우선 순위
print(5 + 3 * 2)
# 11

print(2 + 2 - 2 * 2 / 2 * 2)
# 0.0

print(2 - 2 + 2 / 2 * 2 + 2)
# 4.0

# ? 만약 순서를 바꾸고 싶다면 ( )를 쓸 수 있음
print((5 + 3) * 2)
# 16

# ? 이 경우는 문자열 연산자 에서도 작동함
print("py" + "thon" * 3)
# pythonthonthon

print(("py" + "thon") * 3)
# pythonpythonpython