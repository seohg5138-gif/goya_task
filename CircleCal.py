import math
print("안녕하세요.\n계산기입니다.\n반지름을 입력해주세요.")

radius_1, unit_1 = input("반지름과 단위를 입력하세요 (예: 5 cm): ").split()
radius_1 = float(radius_1)
circumference_1=radius_1*2*math.pi
area_1=radius_1**2*math.pi
print("-----------------------결과-----------------------")
print(f"""원의 반지름{radius_1}에 대하여
둘레:{round(circumference_1,3)}{unit_1},
넓이:{round(area_1,3)}{unit_1}^2 입니다. """)
