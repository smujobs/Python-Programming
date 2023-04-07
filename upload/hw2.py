'''
사용자로부터 입력된 금액을 동전으로 교환하고자 할 때, 각 동전별 교환 개수를 출력하는 프로그램
202310977 정지원
Fri Mar 17
'''

def get_integer(prompt_message : int):
    '''
    Shows message in prompt and gets user's input, returns in int.

    Args:
        prompt_message: String, to print message in prompt.
    Returns:
        returns Integer that user entered.
    '''
    integer = int(input(prompt_message))
    return integer

def exchange(price : int):
    '''
    Calculates changes and prints changes.

    Args:
        price: Int, to be exchanged in changes.
    '''
    numOf500 = price // 500
    price %= 500
    numOf100 = price // 100
    price %= 100
    numOf50 = price // 50
    price %= 50
    numOf10 = price // 10
    price %= 10

    print(f'500원 동전의 개수: {numOf500}')
    print(f'100원 동전의 개수: {numOf100}')
    print(f'50원 동전의 개수: {numOf50}')
    print(f'10원 동전의 개수: {numOf10}')


price_to_exchange = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(price_to_exchange)
