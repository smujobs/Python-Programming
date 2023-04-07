exchg_rate = 0

def set_rate(rate):
    global exchg_rate
    exchg_rate = rate

def get_rate(rate):
    return exchg_rate

def to_dollar(won):
    return won / exchg_rate

def to_won(dollar):
    return dollar * exchg_rate

def main():
    print('### 환율 변환 모듈 테스트 ###')
    set_rate(1010)
    print('오늘의 환율', get_rate())
    print('2020원 =', to_dollar(2020),'달러')
    print('2달러 =', to_won(2),'원')

if __name__ == '__main__':
    main()