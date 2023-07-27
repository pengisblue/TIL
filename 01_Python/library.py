class Pokemon:
    number_of_pokemon = 0
    discovered_species = []
    filst_child = None

    def __init__(self):
        self.skill_1 = '몸통박치기'
        Pokemon.increase_number

    # 모든 포켓몬은, 공격이라는 행위
    def attack(self):
        return self.skill_1

    @classmethod
    def increase_spcies(cls, spcies):
        # 내 클래스 변수 discovered_species
        # 아직 추가 된 적이 없던 종이라면, 추가
        print('종 추가 여부 확인')
        if spcies not in cls.discovered_species:
            cls.discovered_species.append(spcies)

    @classmethod
    def increase_number(cls):
        cls.number_of_pokemon += 1