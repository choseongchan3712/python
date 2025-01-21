#
# % 키워드: else구문, elif구문, False값, pass키워드

# ! (1) else 조건문
# ? else구문은 if 조건문 뒤에 사용하며, if 조건문의 조건이 거짓일 때 실행되는 부분임.

number_1 = int(3)

if number_1 % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
# 홀수입니다.


# ! (2) elif 구문
# ? elif구문은 if 세 개 이상의 조건을 연결해서 사용하는 방법임

import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("봄입니다.")
elif 6 <= month <= 8:
    print("여름입니다.")
elif 9 <= month <= 11:
    print("가을입니다.")
else:
    print("겨울입니다.")
# 겨울입니다.


# ! (3) False로 변환되는 값
# ? if조건문의 매개변수에 불이 아닌 다른 값이 올 때는 자동으로 이를 불로 변환해서 처리함.
# ? False로 변환되는 값은 None, 숫자0과 0.0, 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)임.


# ! (4) pass 키워드
# ? pass키워드를 사용하는것은 "진짜 아무것도 안함" 또는 "곧 개발하겠음"이라는 의미
number_2 = 3

if number_2 > 0:
    pass
else:
    pass
