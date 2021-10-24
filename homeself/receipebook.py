from receipe import Receipe
class Receipebook:
    def __init__(self):
        self.receipe_list =[]
        self.food_court()

    def add_receipe(self):
        #추가할 레시피 이름을 입력받자
        receipe_name = input('>>레시피 이름을 입력하세요:')
        #중복을 체크하자
        for receipe in self.receipe_list:
        #중복되는 레시피가 있으면
            if receipe_name == receipe.name:
        #이미 있다고 알려주자
                print('이미 존재하는 레시피입니다.')
                return
        #중복되는 레시피가 없으면 새 레시피 생성하자
        new_receipe = Receipe(receipe_name)
        new_receipe.set_receipe()
        #레시피 리스트에 추가하자
        self.receipe_list.append(new_receipe)

    def show_all_receipe(self):
        for index, receipe in enumerate(self.receipe_list):
            print(f'\n{index+1}번')
            print(receipe)
    def search_receipe(self):
        # 칮을 레시피 이름을 입력받자
        receipe_name=input('>>원하는 레시피를 검색하세요:')
        searched_receipe = []
        # (반복문시작) 레시피 리스트를 돌면서 레시피 있는지 확인하자
        for receipe in self.receipe_list:
            #찾는 레시피 이름이 있따면
            if receipe_name in receipe.name: #if '부대' in '부대찌개'
                #그 레시피 보여주자
                print(receipe)
                searched_receipe.append(receipe)
        #(반복문종료)
        #찾는 레시피가 없다면
        if len(searched_receipe) ==0: #못 찾았다
                
            #추가할지 물어보자
            choice = input('>>원하는 레시피가 없습니다. 추가하시겠습니까?(1: 예, 0: 아니요')
            #추가한다고 하면
            if choice == '1':
                #레시피 추가하자
                self.add_receipe()
            # 추가 안 한다고 하면
            else:
                return
                #끝
    def search_whatin(self):
        # 재료 다 보여주자
        whatin_set =set()
        for receipe in self.receipe_list:
            for whatin in receipe.whatin:
                whatin_set.add(whatin) #{'김지'.'두부','감자}.add(두부) ->{'두부',감자','김치'}
        print('다음 재료를 사용해보세요!')
        for index, whatin in enumerate(whatin_set):
            print(f'{index+1}.{whatin}')

        print(receipe)

    def food_court(self):
        지원이 = Receipe('케이크')
        지원이.quantity =1
        지원이.url = 'youtube.com'
        지원이.ingredient = {'밀가루:','500','계란:','100','생크림:','200'}
        지원이.info='맛있게 드세요'
        self.receipe_list.append(지원이)
        서연이=Receipe('삼겹살김치볶음밥')
        서연이.quantity =4
        서연이.link=''
        서연이.whatin ={'삼겹살':'500'}
        self.receipe_list.append(서연이)


    def __str__(self):
        pass