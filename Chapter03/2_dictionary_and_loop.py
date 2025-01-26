#
# % 키워드: 딕셔너리, 키, 값

# ! (1) 딕셔너리 선언하기
# ? 딕셔너리는 중괄호{}로 선언하며, 키:값 형태를 쉼표(,)로 연결해서 만듬.
# ? 키는 문자열, 숫자, 불 등으로 선언할 수 있음.

dict_a = {"name": "어벤저스 엔드게임", "type": "히어로 무비"}


# ! (2) 딕셔너리의 요소에 접근하기
# ? 딕셔너리 요소에 접근할 때는 리스트처럼 딕셔너리 뒤에 대괄호[]를 입력하고 내부에 인덱스처럼 키를 입력함.
# ? 이때 주의할 점은 딕셔너리를 선언할 때는 중괄호{}를 사용하지만, 딕셔너리의 요소에 접근할 때는 리스트처럼 딕셔너리 뒤에 대괄호[]를 입력하고 내부에 인덱스처럼 키를 입력함.
print(dict_a["name"])
# 어벤저스 엔드게임
print(dict_a["type"])
# 히어로 무비

# ? 딕셔너리 내부의 값에 문자열, 숫자, 불 등의 다양한 자룔를 넣을 수도 있음. 리스트와 딕셔너리도 하나의 자료이므로, 리스트와 딕셔너리를 값으로 넣을 수도 있음.
dict_b = {
    "director": ["안소니 루소", "조 루소"],
    "cast": ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"],
}

print(dict_b["director"])
# ['안소니 루소', '조 루소']

dictionary = {
  "name": "7D 건조 망고",
  "type": "당절임",
  "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
  "origin": "필리핀"
}

print("name:", dictionary["name"])
# name: 7D 건조 망고
print("type:", dictionary["type"])
# type: 당절임
print("ingredient:", dictionary["ingredient"])
# ingredient: ['망고', '설탕', '메타중아황산나트륨', '치자황색소']
print("origin:", dictionary["origin"])
# origin: 필리핀

# ? 값 변경
dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])
# name: 8D 건조 망고

# ? 딕셔너리 안에있는 리스트도 인덱스를 지정하여 특정 값을 받아올 수 있음
print(dictionary["ingredient"][1])
# 설탕