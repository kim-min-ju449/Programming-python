list1 = [1, 5, 7]
try:
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])
except IndexError as e:
    print(e)
else:
    print("성공!!")
finally:
    print("꼭 실행 해야되는 코드")