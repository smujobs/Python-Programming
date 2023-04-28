# 쇼핑몰 장바구니 시뮬레이션 프로그램 작성, 202310977 정지원, Fri Apr 28

shopping_bag : dict = {}

def get_user_input(message_to_show):
    return input(message_to_show)

def create_item(tgt_list : dict, product_name : str, product_quantity : int, list_name : str):
    tgt_list[product_name] = product_quantity
    print(f'{list_name}에 {product_name} {product_quantity}개가 담겼습니다.')

def read_item(tgt_list : dict):
    print('장바구니 보기:', tgt_list)

def search_item(tgt_list : dict, product_name : str):
    if product_name in tgt_list:
        print(f'{product_name}은(는) {tgt_list[product_name]}개 담겨 있습니다.')
    else:
        print(f'{product_name}은 {tgt_list}에 담겨있지 않습니다.')

# Main Unit

while True:
    product_name = str(get_user_input('추가할 상품의 상품명을 입력하세요: '))
    if product_name != '':
        product_quantity = int(get_user_input('추가할 상품의 수량을 입력하세요: '))
        create_item(shopping_bag, product_name, product_quantity, '장바구니')
    else: break

read_item(shopping_bag)

while True:
    product_name = str(get_user_input('검색할 상품의 상품명을 입력하세요: '))
    if product_name != '':
        search_item(shopping_bag, product_name)
    else: break

print('프로그램을 종료합니다.')