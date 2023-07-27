from library import Pokemon

# 상속 받는다.
class Pikachu(Pokemon):
    no = 25
    type = '전기'


    def __init__(self, name, lv=5):
        # super -> 부모 클래스의 메서드를 호출하고자 할 때 사용
        super().__init__()
        # 부모 클래스의 메서드를 직접 호출 -> self 인자로 넘겨야함
        # Pokemon.__init__(self)
        self.name = name
        self.lv = lv

        # 최초의 피카츄가 태어났을 때만, 종 정보를 기록한다
        # first_child
        if Pikachu.filst_child is None:
            Pikachu.filst_child = self
            super().increase_spcies('피카츄')


class Metamon(Pokemon):
    no = 132
    type = '노말'

    def __init__(self, name, lv=5):
        super().__init__()
        self.name = name
        self.lv = lv

        if Metamon.filst_child is None:
            Metamon.filst_child = self
            super().increase_spcies('메타몽')
        
        self.skill_1 = '변신'
    
    def attack(self, target):
        self.type = target.type
        return f'{self.name}이 {target.name}으로 변신했다.'
    

p1 = Pikachu('피카츄')
m1 = Metamon('메타몽')
print(Pokemon.discovered_species)
print(p1.attack(), m1.attack(p1))
print(m1.type)
print(Metamon.type)