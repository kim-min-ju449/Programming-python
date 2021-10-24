# 핸드폰 요금이 62421원 나왔다. 100원 미만은 절사한다고 한다. 62400원 청구. 59827원일 경우, 실제 청구 금액은?
import math
print(math.floor(598.27)*100)

bill = 62421
print(bill//100*100)
print(bill-bill%100)
print(math.floor(bill/100)%100)
# 평가계획은 100점 만점에 10점 단위로 점수를 줄 수 있다. 채점한 결과 93점이 나왔다. 90점 부여. 56점은 몇 점 부여?
print(round(5.6)*10)

score=93
print(round(score/10)*10)
print(round(score,-1))
# 로또 복권 자동 생성기를 만든다면?
# (로또복권: 1~45 사이의 번호 중 랜덤으로 6개 뽑기)
import random
print(random.randrange(1,45,1))
print(random.randrange(1,45,1))
print(random.randrange(1,45,1))
print(random.randrange(1,45,1))
print(random.randrange(1,45,1))
print(random.randrange(1,45,1))

random.sample(range(1,46), 6)
# 1~9 숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?(185:O, 212:X)
num = list(range(1, 10))  # num = [1,2,3,4,5,6,7,8,9]

number = []
for i in range(3):
    number.append(num.pop(num.index(random.choice(num))))

print(str(number[0])+str(number[1])+str(number[2]))

#2
list_r = random.sample(range(1,10),3)
print("".join(str(n) for n in list_r))
print("".join(map(str, list_r)))
print(str(list_r))

# 내가 태어난 날로부터 며칠이 지났는지?
import datetime
now=datetime.datetime.now()
birthday = datetime.datetime(2004, 9, 5)
print(birthday)
print(now-birthday)
# 올해 크리스마스까지 며칠이 남았는지?
christ=datetime.datetime(2021, 12, 25)
print(christ-now)
# 내 생일이 며칠 남았는지?
birth=datetime.datetime(2021, 9, 5)
print(birth-now)
# 랜덤하게 번호로 자리를 배치하는 방법은?
# 제적(전출, 자퇴) 인원이 있다면?
last_number = input("마지막 번호는?")
list_class = list(range(1,int(last_number)+1))
while True:
    exclude_number = input("뺄 번호는?(엔터치면 끝내자)")
    if exclude_number =='':
        break
    list_class.remove(int(exclude_number))
random.shuffle(list_class)
#print(list_class)
print("자리\t학생번호")
for index, n in enumerate(list_class):
    print(f'{index+1}\t{n}')
