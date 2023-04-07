"""
사용자로부터 세 자리수 이하의 10진 정수 하나를 입력받아 다음과 같이 각 자릿수를 한글로 읽어주는 프로그램
202310977 정지원
Fri Apr 7
"""

def get_user_input(prompt_msg):
    """
    Gets user's input by prompt.
    
    Args:
        prompt_msg (str) : string to show in prompt when gets user's message.
    Returns:
        user's input : Str
    """
    return input(prompt_msg)

def print_single_digit(num_string):
    """
    Prints single digit of number in korean pronounciation.

    Args:
        num_string (str) : a number to print pronounciation.
    Returns:
        None
    """
    num = int(num_string)
    if num == 0:
        ans_str = '공'
    elif num == 1:
        ans_str = '일'
    elif num == 2:
        ans_str = '이'
    elif num == 3:
        ans_str = '삼'
    elif num == 4:
        ans_str = '사'
    elif num == 5:
        ans_str = '오'
    elif num == 6:
        ans_str = '육'
    elif num == 7:
        ans_str = '칠'
    elif num == 8:
        ans_str = '팔'
    elif num == 9:
        ans_str = '구'
    
    print(ans_str, end=' ')

def read_number(list_of_input):
    """
    Use function 'print_single_digit' with for statement.

    Args:
        list_of_input (list) : list of numbers to use function 'print_single_digit'.
    Returns:
        None
    """
    for single_digit in list_of_input:
        print_single_digit(single_digit)

# main program sector

nums_string = get_user_input('세 자리 정수 입력: ')
num_list = list(nums_string)
read_number(num_list)