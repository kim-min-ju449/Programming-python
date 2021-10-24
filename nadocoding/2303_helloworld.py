#1
id_number ="040905"
print(id_number[0:2])
print(id_number[2:])
print(int(id_number[0:2])+int(id_number[2:]))
#2
phone_number=["02","1234","5678"]
print(phone_number[0])
print(phone_number[2])
#2-1

student_number ="2100"
number=int(student_number[1])

'''
if student_number[1] ==1 or 2:
    print("뉴미디어소프트웨어과")
elif student_number[1] ==3 or 4:
    print("뉴미디어웹솔루션과")
elif student_number[1] == 5 or 6:
        print("뉴미디어디자인과")
else:
    print("잘못입력했습니다.")
    '''
majors=['뉴미디어소프트웨어과','뉴미디어웹솔루션과','뉴미디어디자인과']
if 1 <=number <=6:
    print(f'{number}반{majors[(number-1)//2]}')
else:
    print("잘못입력했습니다. ")

#2-2
def get_major(grade):
    if grade[1] == 1 or 2:
        return grade[0],"뉴미디어소프트웨어과"
    elif grade[1] == 3 or 4:
        print("뉴미디어웹솔루션과")
        return grade[0], "뉴미디어웹솔루션과"
    elif grade[1] == 5 or 6:
        return grade[0], "뉴미디어디자인과"
    

grade, major =get_major("2100")
print(major, grade)
#2-3
a=0
def average(a,b,c=0):
   if c ==0:
       return (a + b + c) / 2
   return (a + b + c) / 3

print(average(10, 20, 30)) #20.0
print(average(4, 23)) #13.5
#2-4
def get_bmi(cm, kg):
    m=cm/100
    bmi= kg/(m*m)
    if bmi > 25:
        print("비만")
    elif bmi>=23:
        print("과체중")
    elif bmi>=18.5:
        print("정상")
    else:
        print("마름")
    return round(bmi,1)
bmi = get_bmi(176, 69)
print(bmi) #22.3
#3-1
def n_sum(a):
    num=str(a)
    if len(num) >=10:
        return -1
    elif len(num) == 2:
        return int(num[0])+int(num[1])
    elif len(num) ==3:
        return int(num[0]) + int(num[1])+int(num[2])
result = n_sum(10)
print(result)        #1
result = n_sum(331)
print(result)         #7
result = n_sum(408)
print(result)         #12
result = n_sum(1000000000)
print(result)         #-1
#3-2
def  get_subway_fare(km):
    if km <=10:
        return 720
    elif km<=50:
        a =km/5
        return a*100+720
    else:
        a= 50/5
        b = (km-50)/8
        return (a*100)+(b*100)+720
fare = get_subway_fare(5)
print(fare)        #720
fare = get_subway_fare(26)
fare = get_subway_fare(61)
print(fare)        #1720
print(fare)        #1120
#3-3
def get_three_six_nine(num):
    if num>=10:
        strnum =str(num)

        if strnum[0] == 3 or 6 or 9:

            if strnum[1]==3 or 6 or 9:
                return "짝짝"
            else:
                return "짝"
        else:
            return strnum
    else:
        if num == 3 and 6 and 9:
            return "짝"
        else:
            return num
result = get_three_six_nine(1)
print(result)        #1
result = get_three_six_nine(3)
print(result)        #짝
result = get_three_six_nine(16)
print(result)        #짝
result = get_three_six_nine(36)
print(result)        #짝짝
#3-4


'''
도형과 길이 밑변을 넣으면 넓이 구해주는 프로그램

1. get_area
2. string int 
3. 넓이
4. result=get_area(8,4,"삼각형")
print(result)

'''

def get_area(height, width, name):
    if name =="삼각형":
        return height*width/2
    elif name =="사각형":
        return height*width
    elif name =="원":
        return height*width*3.14
    elif name=="마름모":
        return height*width*0.5
    else:
        return "용량 초과입니다. 이런 도형은 없거나 시스템이 없습니다"

result=get_area(8,4,"삼각형")
print(result)
result=get_area(6,6,"원")
print(result)
result=get_area(9,5,"사각형")
print(result)
result=get_area(9,5,"다각형")
print(result)


