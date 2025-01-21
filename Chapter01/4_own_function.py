
# % 키워드: format(), upper(), lower(), strip(), find(), in연산자, split(), f-문자열

# ! (1) 문자열의 format() 함수
# ? format() 함수는 문자열이 가지고 있는 함수임, 중괄호 {}를 포함한 문자열 뒤에 마침표"."를 찍고 format() 함수를 사용하는데, 중괄호의 개수와 format 함수 괄호안 매개변수의 개수는 반드시 같아야 함.

string_a = "{}".format(10)
print(string_a)
# 10

string_b = "{} {}".format(10, 20)
print(string_b)
# 10 20

string_c = "{} {} {}".format(10, 20, 30)
print(string_c)
# 10 20 30

# ? format을 사용하면 값은 문자열로 반환됨

# ? format이라는 함수는 {} 기호를 format의 괄호 안에 있는 매개변수로 대체하는 것뿐이기 때문에 {} 기호 앞뒤 혹은 {} 기호와 {} 기호 사이에 다양한 문자열을 넣을 수 있음

format_a = "{}만 원".format(5000)
print(format_a)
# 5000만 원

format_b = "첫 연봉은{}만 원".format(5000)
print(format_b)
# 첫 연봉은5000만 원

# ? format()함수의 다양한 기능:
# ? (1) 출력할 정수에 기호를 넣어주거나, 숫자 형태를 다양하게 출력할 수 있음
output_d = "{:d}".format(52)
print(output_d)
# 52

output_e = "{:5d}".format(52)
print(output_e)
#    52

output_f = "{:10d}".format(52)
print(output_f)
#         52

output_g = "{:05d}".format(52)
print(output_g)
# 00052

output_h = "{:05d}".format(-52)
print(output_h)
# -0052

# ? {:d}를 사용하면 int자료형의 정수를 출력하겠다고 직접적으로 지정하는 방법. 따라서 {:d}를 사용하면 매개변수로 정수만 올 수 있음.
# ? {:5d}라고 입력을 하면 5칸을 빈칸으로 잡고 뒤에서부터 52라는 숫자를 채움
# ? {:05d}라고 지정하면 5칸중 빈곳을 0으로 채움, 부호가 있을 때는 맨앞자리는 부호로 채움.

output_1 = "{:+d}".format(52) # 양수
print(output_1)
# +52

output_2 = "{:+d}".format(-52) # 음수
print(output_2)
# -52

output_3 = "{: d}".format(52) # 양수: 기호 부분 공백
print(output_3)
#  52

output_4 = "{: d}".format(-52) # 음수: 기호 부분 공백
print(output_4)
# -52

# ? {:+d}처럼 d앞에 + 기호를 붙이면 양수와 음수 기호를 표현할 수 있음. 
# ? {: d}처럼 앞에 공백을 두어 기호 위치를 비워 주면 함수에 입력한 기호가 표현됨

output_5 = "{:+5d}".format(52) # 기호를 뒤로 밀기
print(output_5)
#   +52

output_6 = "{:+5d}".format(-52) # 기호를 뒤로 밀기
print(output_6)
#   -52

output_7 = "{:=+5d}".format(52) #기호를 앞으로 밀기
print(output_7)
# +  52

output_8 = "{:=+5d}".format(-52) #기호를 앞으로 밀기
print(output_8)
# -  52

output_9 = "{:+05d}".format(52) # 0으로 채우기
print(output_9)
# +0052

output_10 = "{:+05d}".format(-52) # 0으로 채우기
print(output_10)
# -0052

# ? {:f}를 사용하면 float 자료형을 강제로 출력할 수 있음

float_1 = "{:f}".format(52.273)
print(float_1)
# 52.273000

float_2 = "{:15f}".format(52.273) # 15칸 만들기
print(float_2)
#       52.273000

float_3 = "{:+15f}".format(52.273) # 15칸에 부호 추가하기
print(float_3)
#      +52.273000

float_4 = "{:+015f}".format(52.273) # 15칸에 부호 추가하고 0으로 채우기
print(float_4)
# +0000052.273000

# ? 소수점 아래 자릿수 지정하기

float_5 = "{:15.3f}".format(25.273)
print(float_5)
#          25.273

float_6 = "{:15.2f}".format(25.273)
print(float_6)
#           25.27

float_7 = "{:15.1f}".format(25.273)
print(float_7)
#            25.3

# ? 의미 없는 소수점 제거하기
# ? 의미없는 0을 제거한 후 출력하고 싶을때는 {:g}를 사용함

number_1 = 52.0
print(number_1)
# 52.0

number_2 = "{:g}".format(number_1)
print(number_2)
# 52





# ! (2) 대소문자 바꾸기: upper()와 lower()
# ? upper()함수는 문자열의 알파벳을 대문자로, lower()함수는 문자열의 알파벳을 소문자로 만듬

a = "hello python"
print(a.upper())
# HELLO PYTHON

b = "HELLO PYTHON"
print(b.lower())
# hello python





# ! (3) 문자열 양옆의 공백 제거하기
# ? strip(): 문자열 양옆의 공백을 제거
# ? lstrip(): 문자열 왼쪽 공백 제거
# ? rstrip(): 문자열 오른쪽 공백 제거

c = """
      안녕하세요
파이썬
"""
print(c)
#       안녕하세요
# 파이썬

print(c.strip())
# 안녕하세요
# 파이썬





# ! (4) 문자열 구성 파악하기
# ? isalnum(): 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인
# ? isalpha(): 문자열이 알파벳으로만 구성되어 있는지 확인
# ? isidentifier(): 문자열이 식별자로 사용할 수 있는지 확인
# ? isdecimal(): 문자열이 정수 형태인지 확인
# ? isdigit(): 문자열이 숫자로 인식될 수 있는지 확인
# ? isspace(): 문자열이 공백으로만 구성되어 있는지 확인
# ? islower(): 문자열이 소문자로 구성되어 있는지 확인
# ? isupper(): 문자열이 대문자로 구성되어 있는지 확인

print("number10".isalnum())
# True
print("10".isdigit())
# True





# ! (5) 문자열 찾기
# ? find(): 왼쪽부터 찾아서 처음 등장하는 위치를 찾음
# ? rfind(): 오른쪽부터 찾아서 처음 등장하는 위치를 찾음

hello_1 = "안녕안녕하세요".find("안녕")
print(hello_1)
# 0

hello_2 = "안녕안녕하세요".rfind("안녕")
print(hello_2)
# 2





# ! (6) 문자열과 in연산자
# ? 문자열 내부에 어떤 문자열이 있는지 확인 하려면 in 연산자를 사용함. 출력은 True/False로 나옴

print("안녕" in "안녕하세요")
# True

print("javascript" in "python")
# False





# ! (7) 문자열 자르기: split()

split_a = "10 20 30 40 50".split(" ")
print(split_a)
# ['10', '20', '30', '40', '50']





# ! (8) f-문자열
# ? 파이썬 3.6버전부터는 format()함수를 더 간단히 사용할 수 있는 방법을 제공함. 바로 f-문자열임
# ? 사용방법: f"문자열{표현식}문자열"

print(f"3 + 4 = {3 + 4}")
# 3 + 4 = 7

print(f"""1 + 2 = {1 + 2}
2 + 3 = {2 + 3}
3 + 4 = {3 + 4}
""")
# 1 + 2 = 3
# 2 + 3 = 5
# 3 + 4 = 7