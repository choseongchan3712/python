
# % 키워드: 변수 선언, 변수 할당, 변수 참조, input(), int(), float(), str()

# ! (1) 변수 만들기 
pi = 3.14159265
print(pi)
# 3.14159265

print(pi + 2)
# 5.14159265

print(pi - 2)
# 1.1415926500000002

print(pi * 2)
# 6.2831853

print(pi / 2)
# 1.570796325

print(pi % 2)
# 1.1415926500000002

print(pi * pi)
# 9.869604378534024

# ? 원의 둘레와 넓이 구하기
pi = 3.14159265
r = 10

print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", pi * 2 * r)
print("원의 넓이 =", pi * (r ** 2))
# 원주율 = 3.14159265
# 반지름 = 10
# 원의 둘레 = 62.831853
# 원의 넓이 = 314.159265






# ! (2) 복합 대입 연산자
a = 10
a += 10
print(a)
# 20

b = 20
b -= 10
print(b)
# 10

c = 10
c *= 2
print(c)
# 20

d = 10
d /= 2
print(d)
# 5.0

e = 7
e %=2
print(e)
# 1

f = 2
f **= 2
print(f)
# 4


# ? 문자열 복합 대입 연산자
string1 = "py"
string1 += "thon"
print(string1)
# python

string2 = "python"
string2 *= 2
print(string2)
# pythonpython





# ! (2) 사용자 입력 input()
# ? 파이썬은 명령 프롬프트에서 사용자로부터 데이터를 입력받을 때 input() 함수를 사용함
# ? input 함수 괄호 안에 입력한 내용을 프롬프트 문자열이라고 한다.

string = input("인사말을 입력하세요>")
print(string)

# ? 여기서 주의 할 점은 input()함수는 사용자가 무엇을 입력해도 결과는 무조건 문자열 자료형임





# ! (3) 문자열을 숫자로 바꾸기
# ? input() 함수의 입력 자료형은 항상 문자열이기 때문에 입력받은 문자열을 숫자로 변환해야 숫자 연산에 활용할 수 있는데, 이것을 캐스트(cast)라고 한다.
# ? int(): 문자열을 정수형으로 변환.
# ? float(): 문자열을 실수형으로 변환.

number_a = input("숫자 입력a>") # 123
int_a = int(number_a) 

number_b = input("숫자입력b>") # 456
int_b = int(number_b)

print("문자열 자료:", number_a + number_b)
# 123456
print("숫자 자료", int_a + int_b)
# 325





# ! 숫자를 문자열로 바꾸기
# ? 숫자를 문자열로 바꾸는 방법은 다양하지만, 그중에 하나가 str()함수임
output_a = str(123)
output_b = str(123.456)

print(type(output_a), output_a)
# <class 'str'> 123
print(type(output_b), output_b)
# <class 'str'> 123.456