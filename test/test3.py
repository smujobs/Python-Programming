# 쇼핑몰 장바구니 시뮬레이션 프로그램 작성, 202310977 정지원, Fri Apr 28

shopping_bag : list = []

def get_user_input(message_to_show):
    return input(message_to_show)

def create_item(tgt_list : list, product_name : str, list_name : str):
    tgt_list.append(product_name)
    print(f'{list_name}에 {product_name}가 담겼습니다.')

def read_item(tgt_list : list):
    print('장바구니 보기:', tgt_list)

# Main Unit

while True:
    product_name = str(get_user_input('추가할 상품의 상품명을 입력하세요: '))
    if product_name != '':
        create_item(shopping_bag, product_name, '장바구니')
    else: break

read_item(shopping_bag)