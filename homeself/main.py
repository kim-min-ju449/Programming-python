from receipebook import Receipebook

def print_menu():
    print('1. 레시피 검색')
    print('2. 레시피 추가')
    print('3. 재료 검색')
    print('4. 레시피 모음')
    print('5. 종료')
    menu = input('>>메뉴를 선택하세요:')
    return menu
def main():
    receipebook_203 = Receipebook()
    while True:
        menu = print_menu()
        if menu == '1':
            receipebook_203.search_receipe()
            #레시피검색
        elif menu =='2':
            receipebook_203.add_receipe()
        elif menu =='3':
            receipebook_203.search_whatin()
        elif menu =='4':
            receipebook_203.show_all_receipe()
        elif menu =='5':
            break
        else:
            print('잘못입력했습니다.')
if __name__ == '__main__':
    main()

