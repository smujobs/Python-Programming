# 2차원 화면에 있는 직사각형의 둘레와 넓이 구하기 프로그램 작성, 202310977 정지원, Say May 20

class Rectangle:
    def __init__(self, left_top_x, left_top_y, right_botom_x, right_bottom_y):
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.right_botom_x = right_botom_x
        self.right_bottom_y = right_bottom_y

    def show(self):
        print(f'좌상단꼭짓점이 ({self.left_top_x}, {self.left_top_y})이고 우하단꼭짓점이 ({self.right_botom_x}, {self.right_bottom_y})인 사각형입니다.')

    def getWidth(self):
        return abs(self.right_botom_x - self.left_top_x)
    
    def getHeight(self):
        return abs(self.right_bottom_y - self.left_top_y)
    
    def getArea(self):
        return self.getWidth() * self.getHeight()
    
    def getPerimeter(self):
        return self.getWidth() * 2 + self.getHeight() * 2
    
# test - complete

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show() # => 좌상단꼭짓점이 (5, 5)이고 우하단꼭짓점이 (20, 10)인 사각형입니다.
print(f'넓이는 {a}, 둘레는 {p}') # => 넓이는 75, 둘레는 40