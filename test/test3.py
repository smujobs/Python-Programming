def disp_multi_table(num):
    for sub in range(1, 10):
        print(f'{num} x {sub} = {num * sub:2d}')
        

def input_pos_num():
    n = 0
    while n <= 0:
        n = int(input('구구단에 들어갈 양의 정수를 입력하세요: '))
    return n

disp_multi_table(input_pos_num())