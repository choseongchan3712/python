#
# % 키워드: 리스트, 요소, 인덱스, for반복문

# ! (1) 라스트 선언 및 접근
# ? 파이썬에서 리스트를 생성하는 방법은 []에 자료를 쉼포로 구분해서 입력함.

list_a = [273, 32, 103, "문자열", True, False]

print(list_a)
# [273, 32, 103, '문자열', True, False]

print(list_a[0])
# 273

print(list_a[1])
# 32

print(list_a[2])
# 103

print(list_a[3])
# 문자열

print(list_a[4])
# True

print(list_a[5])
# False

print(list_a[0:3])
# [273, 32, 103]

# ? 리스트의 특정 요소는 변경할 수도 있음.
list_a[0] = "변경"
print(list_a)
# ['변경', 32, 103, '문자열', True, False]

# ? 대괄호 안에 음수를 넣어 뒤에서부터 요소를 선택할 수 있음.
list_b = [1, 2, 3, 4]
print(list_b[-1])
# 4

# ? 리스트 접근 연산자는 이중으로 사용할 수 있음
list_c = ["파이썬", "문자열", "리스트"]
print(list_c[0][0])
# 파

# ? 리스트 안에 리스트를 사용할 수도 있음
list_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list_d[1])
# [4, 5, 6]
print(list_d[1][1])
# 5

# ? 리스트 슬라이싱: [:]연산자로 마지막 위치에 '단계'를 추가하여 지정한 숫자만큼 인덱스를 건너뛰며 요소를 가져올 수 있음
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:5:2])
# [1, 3, 5]
print(numbers[::-1])  # 반대로 출력
# [8, 7, 6, 5, 4, 3, 2, 1]


# ! (2) 리스트 연산하기: 연결(+), 반복(*), len()
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print("list_1 =", list_1)
# list_1 = [1, 2, 3]
print("list_2 =", list_2)
# list_2 = [4, 5, 6]

print("list_1 + list_2 =", list_1 + list_2)  # 비파괴적 처리리
# list_1 + list_2 = [1, 2, 3, 4, 5, 6]
print("list_1 * 3 =", list_1 * 3)
# list_1 * 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print("len(list_1) =", len(list_1))
# len(list_1) = 3


# ! (3) 리스트에 요소 추가하기: append(), insert()
# ? 리스트에 요소를 추가하는 방법은 append()와 insert()가 있습니다.
# ? 1) append(요소): 리스트 뒤에 요소를 추가.
# ? 2) insert(위치, 요소): 리스트 중간에 요소를 추가함.

list_3 = [1, 3, 5]
list_3.append(7)
list_3.append(9)
print(list_3)
# [1, 3, 5, 7, 9]

list_3.insert(1, 2)
list_3.insert(3, 4)
list_3.insert(5, 6)
list_3.insert(7, 8)
list_3.insert(9, 10)
print(list_3)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ? expend()함수를 사용하면 append()함수를 여러번 사용하는 효과를 만들 수 있음
list_4 = [1, 2, 3]
list_4.extend([4, 5, 6])  # 파괴적 처리
print(list_4)
# [1, 2, 3, 4, 5, 6]


# ! (4) 리스트 요소 제거하기
# ? 인덱스로 제거하기: del 키워드, pop()
# ? 1) del 리스트명[인덱스]
# ? 2) 리스트명.pop(인덱스)

list_del = [0, 1, 2]
del list_del[1]
print(list_del)
# [0, 2]

list_pop = [4, 5, 6]
list_pop.pop(2)
print(list_pop)
# [4, 5]

# ? del 키워드는 리스트의 요소를 한꺼번에 제거할 수도 있음.
list_5 = [0, 1, 2, 3, 4, 5, 6]
del list_5[3:6]  # 마지막 요소는 포함하지 않음
print(list_5)
# [0, 1, 2, 6]

list_6 = [0, 1, 2, 3, 4, 5, 6]
del list_6[:3]  # 마지막 요소는 포함하지 않음
print(list_6)
# [3, 4, 5, 6]

list_7 = [0, 1, 2, 3, 4, 5, 6]
del list_7[3:]
print(list_7)
# [0, 1, 2]

# ? 3) 값으로 제거하기: remove()
# ? 리스트.remove(값)

list_8 = [1, 2, 1, 2]
list_8.remove(2)
print(list_8)
# [1, 1, 2]
# ? remove()함수로 지정한 값이 리스트 내부에 여러개 있어도 가장 먼저 발견되는 하나만 제거함

# ? 4) 모두 제거하는 clear()
# ? 리스트.clear()

list_9 = [0, 1, 2, 3, 4, 5]
list_9.clear()
print(list_9)
# []


# ! (5) 리스트 정렬하는 sort()
# ? 리스트 요소를 정렬할때 sort() 함수를 사용함. 기본은 오름차순 정렬.
# ? 리스트.sort()

list_10 = [57, 273, 103, 32, 275, 1, 7]

list_10.sort()
print(list_10)
# [1, 7, 32, 57, 103, 273, 275]

list_10.sort(reverse=True)
print(list_10)
# [275, 273, 103, 57, 32, 7, 1]


# ! (6) 리스트 내부에 있는지 확인하는 in / not in 연산자
# ? 파이썬은 특정 값이 리스트 내부에 있는지를 확인하는 방법을 제공함. 바로 in연산자를 활용하는 방법임.
# ? 값 in 리스트

list_11 = [273, 32, 103, 57, 52]

print(273 in list_11)
# True
print(99 in list_11)
# False

print(32 not in list_11)
# False
print(33 not in list_11)
# True


# ! (7) for 반복문
for i in range(5):
    print("반복문")
# 반복문
# 반복문
# 반복문
# 반복문
# 반복문

# ? for 반복문을 리스트와 사용하기
array = [1, 2, 3, 4, 5]
for element in array:
    print(element)
# 1
# 2
# 3
# 4
# 5
# ? for 반복문은 리스트에 있는 요소 하나하나가 element라는 변수에 들어가고 차례차례 반복하게 됨.

# ? for 반복문을 문자열과 사용하기
for character in "안녕하세요":
    print("-", character)
# - 안
# - 녕
# - 하
# - 세
# - 요


# ! (8) 중첩 리스트와 중첩 반복문
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for items in list_of_list:
    for item in items:
        print(item)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

item = 0
array = []
for i in range(10):
    item += 1
    array.append(item)

print(array)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
