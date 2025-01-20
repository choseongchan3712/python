
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