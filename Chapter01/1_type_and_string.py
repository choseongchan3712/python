
#% 키워드: 자료형, 문자열, 이스케이프 문자, 문자열 연산자, type(), len()

#? 파이썬에서 자료형을 확인할 때는 type() 함수를 사용함. 함수의 괄호 내부에 자료를 넣으면 그 자료가 어떤 자료형을 가지고 있는지 확인할 수 있습니다.

# 예시
print(type("안녕하세요"))
# <class 'str'>

print(type(123))
# <class 'int'>

#! 첫번째 타입: 문자열 (string)
# 따옴표로 감싸 입력한 모든 것이 문자열

#? 하나만 출력
print("---하나만 출력---")
print("Hello Python")
# Hello Python

#? 여러 개를 출력
print("---여러 개를 출력---")
print(10, 20, 30, 40, 50)
# 10 20 30 40 50
print("안녕하세요", "저의", "이름은", "파이썬 입니다.")
# 안녕하세요 저의 이름은 파이썬 입니다.

#? 문자열 내부에 큰따옴표 넣기
print('"파이썬"입니다.')
# "파이썬"입니다.

#? 문자열 내부에 작은따옴표 넣기
print("'파이썬'공부중입니다.")
# "파이썬"입니다.

#? 이스케이프 문자: \ 기호와 함께 큰따옴표, 작은 따옴표를 사용하면 이를 문자열을 만드는 기호가가 아니라 '단순한 따옴표'로 인식함.
# \": 큰따옴표
# \': 작은따옴표
print("\"파이썬\"입니다.")
# "파이썬"입니다.

print('\'파이썬\'공부중입니다.')
# '파이썬'공부중입니다.

# \n: 줄바꿈을 의미함
# \t: 탭을 의미함
print("파이썬\n파이썬")
# 파이썬
# 파이썬

print("파이썬\t파이썬")
# 파이썬  파이썬


# ! 문자열 연산자

# ? (1) 문자열 연결 연산자: +
print("파이"+"썬")
# 파이썬

print("파이썬"+"!")
# 파이썬!

# ? 타입이 다른 요소 둘 사이에 + 를 사용하면 타입에러가 발생함.

# ? (2) 문자열 반복 연산자: *
print("python" * 3)
# pythonpythonpython

print(3 * "python")
# pythonpythonpython

# ? (3) 문자 선택 연산자(인덱싱): []
print("python"[0])
# p

print("python"[1])
# y

print("python"[2])
# t

print("python"[3])
# h

print("python"[4])
# o

print("python"[5])
# n

# ? 대괄호 안의 숫자를 음수로 입력하면 뒤에서부터 선택할 수 있음
print("python"[-1])
# n

print("python"[-2])
# o

print("python"[-3])
# h

print("python"[-4])
# t

print("python"[-5])
# y

print("python"[-6])
# p

# ? (4) 문자열 범위 선택 연산자(슬라이싱): [:]
print("python"[0:2])
# py
# 0~1까지를 반환함, 즉 마지막 숫자는 포함하지 않음

# ? 문자열 범위 선택 연산자는 대괄호 안에 넣는 숫자 둘 중 하나를 생략하여, 뒤의 값을 생략할 때는 자동으로 가장 최대 위치(마지막 글자)까지, 앞의 값을 생략할 때는 가장 앞쪽의 위치(첫 번째 글자)까지 지정함.
print("python"[1:])
# ython

print("python"[:4])
# pyth

# ? (5) 문자열의 길이 구하기: len()
print(len("python"))
# 6
