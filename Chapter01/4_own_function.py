
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

