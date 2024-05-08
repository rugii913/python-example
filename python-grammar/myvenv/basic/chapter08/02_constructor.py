# 생성자
## 생성자를 이용해 속성 추가하기
class Monster:
    def __init__(self, health, attack, speed): # 속성 추가하기
        self.health = health
        self.attack = attack
        self.speed = speed

    def decrease_health(self, num): # 메서드 추가하기
        self.health -= num

    def get_health(self): # 메서드 추가하기
        return self.health

goblin = Monster(800, 120, 300)
goblin.decrease_health(300)
print(goblin.get_health())

wolf = Monster(1500, 200, 350)
wolf.decrease_health(500)
print(wolf.get_health())
