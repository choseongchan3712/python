# % 키워드: 불, 비교 연산자, 논리 연산자, if 조건문

# ! (1) 비교연산자
# ? ==: 같다
# ? >: 크다
# ? <: 작다
# ? !=: 다르다
# ? <=: 작거나 같다
# ? >=: 크거나 같다

print(10 == 100)
# False

print(10 != 100)
# True

print(10 < 100)
# True

print(10 > 100)
# False

print(10 <= 100)
# True

print(10 >= 100)
# False

# ? 파이썬은 문자열에도 비교 연ㅅ나자를 적용할 수 있음. 이때 한글은 사전 순서(가나다순)로 앞에 있는 것이 작은 값을 가짐.

print("가방" == "가방")
# True

print("가방" != "하마")
# True

print("가방" < "하마")
# True

print("가방" > "하마")
# False


# ! (2) 논리 연산자

# ? 1) not 연산자
print(not True)
# False
print(not False)
# True

# ? 2) and연산자와 or연산자
print(True and True)
# True
print(True and False)
# False
print(False and False)
# False
print(True or True)
# True
print(True or False)
# True
print(False or False)
# False


# ! (3) if 조건문
number = int(5)

if number > 0:
    print("양수입니다.")
if number < 0:
    print("음수입니다.")
if number == 0:
    print("0입니다.")

# ? 날짜/시간 출력하기
import datetime

# 날짜/시간과 관련된 기능을 가져옴

now = datetime.datetime.now()
# 현재 날짜/시간을 구합니다.

print(now.year, "년")
# 2025 년
print(now.month, "월")
# 1 월
print(now.day, "일")
# 22 일
print(now.hour, "시")
# 2 시
print(now.minute, "분")
# 19 분
print(now.second, "초")
# 51 초

print(
    "{}년 {}월 {}일 {}시 {}분 {}초".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )
)
# 2025년 1월 22일 3시 21분 35초

# 오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.".format(now.hour))
# 현재 시각은 3시로 오전입니다.

# 오후 구분
if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다.".format(now.hour))
