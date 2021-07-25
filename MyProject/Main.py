class Player():
    def __init__(self, name, level, money):
        self.name = name
        self.level = level
        self.money = money
        print(f'{name}님 {level}레벨 {money}원')

        
p1 = Player('da', '0', '10000')
p2 = Player('na', '1', '10000')
