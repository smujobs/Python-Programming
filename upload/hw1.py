'''
사용자로부터 원의 반지름을 정수로 입력받아 그 원의 넓이를 구하는 프로그램을 (Chap 3 연습문제 3, 5)
Fri Mar 10, 2023
by Jiwon Jeong (202310977)
'''

# 매개변수 prompt로 전달받은 메시지를 화면에 출력한 후 입력된 값을 정수로 변환, 반환하는 함수
def get_radius(prompt):
    r = int(input(prompt))
    return r

# 넓이를 구하고자 하는 원의 반지름을 전달받아, 구한 원의 넓이를 반환하는 함수
def get_circle_area(radius):
    width_of_circle = (radius ** 2) * 3.14
    return width_of_circle
    

radius = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
width = get_circle_area(radius)
print('반지름 {}인 원의 넓이 = 3.14 x {} x {} = {}'.format(radius, radius, radius, width))