"""
할인율과 상품의 할인 가격을 전달받아 상품의 할인 전 가격을 계산하는 프로그램
Fri Mar 24, by Jiwon Jeong
"""

def get_fixed_price(discount_percentage, discounted_price):
    """
    gets percentage of discount and discounted price of something, calculates original price by arguments, and returns original price.
        Args:
            discount_percentage : percentage of discount.
            discounted_price : discounted price of something to be calculated.
        Returns:
            original_price : original price of something, calculated by arguments.
    """
    original_price = discounted_price * 100 / (100 - discount_percentage)
    return original_price

def get_int_input(prompt_message):
    """
    shows message and gets int by prompt.
        Args:
            prompt_message : string to show in prompt when gets input by user.
        Returns:
            None
    """
    int_input = int(input(prompt_message))
    return int_input

discount_percentage = get_int_input('할인율은? ')
discounted_price_A = get_int_input('A 상품의 할인된 가격은? ')
discounted_price_B = get_int_input('B 상품의 할인된 가격은? ')
print('A 상품의 정가는 {:g} 원'.format(get_fixed_price(discount_percentage, discounted_price_A)))
print('B 상품의 정가는 {:g} 원'.format(get_fixed_price(discount_percentage, discounted_price_B)))