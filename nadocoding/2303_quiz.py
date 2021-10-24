#1
station="사당"
print(station+"행 열차가 들어오고 있습니다")

#2
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월"+str(date)+"일로 선정되었습니다")
#3
url = "http://naver.com"
my_str = url.replace("http://","")
#print(my_str)
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))
#4
'''
from random import *
lst =[1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))
'''
from random import *
users = range(1, 21)
print(type(users))
users = list(users)
print(users)
shuffle(users)
winners = sample(users, 4)#4명중 1명은 치킨 3명은 커피
print("--당첨자 발표")
print("치킨 당첨자:{0}".format(winners[0]))
print("커피 당첨자:{0}".format(winners[1:]))

#5
from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5<= time <=15:
        print("[o] {0}번재 손님(소요시간:{1}분)".format(i, time))
        cnt +=1
    else: #매칭 실패한 경우
        print("[ ] {0}번재 손님(소요시간:{1}분)".format(i, time))
print("총 탑승 승객:{0}분".format(cnt))
#6
def std_weight(height, gender):
    if gender =="남자":
        return height * height *22
    else:
        return height * height * 21
height = 175
gender ="남자"
weight = round(std_weight(height /100, gender),2)
print("키 {0}cm {1}의 표중 체중은 {2}kg입니다".format(height, gender, weight))
#전화번호 입력시 -가 있든 없는 찰떡같이 알아먹기
phone_number="010-1234-5678"
phone_number2="01098765432"
phone_number3="010 1111 2222"

phone_number=phone_number3
result=phone_number.replace('-','').replace(' ','')
print(result)
#구구단 7단 출력하기
for i in range(1,10):
    print(f'7 X {i} ={7 *i}')
#구구단 2~9단 출력하기중 7까지만
for dan in range(2,10):
    for i in range(1,10):
        print(f'{dan} X {i} ={dan *i}')
    print('-'*10)
    if dan ==7:
        break
#구구단 2~7단을 출력하되 1,3,5,7,9인것만을 출력하기
for dan in range(2,10):
    for i in range(1,10):
        if i%2==0:#if i ==2 or i==4 or i==6 or i==8:
            continue
        print(f'{dan} X {i} ={dan *i}')
    print('-'*10)
    if dan ==7:
        break
#퀴즈 8
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type=house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
              ,self.price, self.completion_year)
houses = []
house1 = House("강남","아파트","메메","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2008년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

for house in houses:
    house.show_detail()

'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''
def is_prime(num):
    if num <2:
        return "소수아님"
    elif num ==2:
        return"소수"
    else:
        for i in range(2, num):
            if num%i ==0:
                return "소수아님"
            return"소수"

result = is_prime(2)
print(result)  # 소수
result = is_prime(13)
print(result)  # 소수
result = is_prime(36)
print(result)  # 소수 아님
'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
'''
def get_compliment(str):
    if str[:3] =="고구마":
        return"왓쇼이"
    elif str[:3] =="맛있는":
            return "우마이"
    elif str == "놀랄 만한 상황" or "굉장한" or "황당한":
        return "요모야"
    else:
        return "으무"

result = get_compliment('고구마 된장국')
print(result) # 왓쇼이!
result = get_compliment('맛있는 크레이프')
print(result) # 우마이!
result = get_compliment('놀랄 만한 상황')
print(result) # 요모야..!
result = get_compliment('좋은 마음가짐이다!')
print(result) # 으무!
'''
Quiz5-1. 모듈이란?

필요한것끼리 자동으로 묶어놓은 파일
Quiz5-2. 패키지란?

모듈들을 모아놓은 집합

Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요

import theater_module as p


Quiz5-4. __all__의 역할은?

모듈의 일부만 저장되게 한다


Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?

from theater_module import price, price_morning

Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
import travel.vietnam
 trip_to.detail()


from travel import vietnam
trup_to=ThailandPackage()
trip_to.detail()


from travel.vietnam import ThailandPackage

trip_to=vietnam.CietnamPackge()
trip_to.detail()
'''
