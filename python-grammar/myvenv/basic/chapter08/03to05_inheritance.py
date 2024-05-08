# 상속, 오버라이딩, 클래스 변수
import random

class Monster:
    max_num = 1000 # 클래스 변수: 인스턴스들이 모두 공유하는 변수

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1

    def move(self):
        print(f"{self.name} 이동")

class Wolf(Monster): # 생성자 __init__()은 상속받은 그대로 사용
    pass # 특정 코드를 정의만 해두고 싶을 때 사용

class Shark(Monster):
    def move(self): # 메서드 오버라이딩
        print(f"{self.name} 헤엄치기")

class Dragon(Monster):
    def __init__(self, name, health, attack): # 생성자 오버라이딩
        super().__init__(name, health, attack) # 부모 클래스 생성자의 로직을 사용함 - name, health, attack 속성은 그대로 사용
        self.skills = ("불", "꼬리", "날개")

    def move(self):
        print(f"{self.name} 날기")

    def use_skills(self):
        print(f"{self.name} 스킬 사용: {self.skills[random.randint(0, 2)]}")

wolf1 = Wolf("늑대", 1500, 200)
wolf1.move()
print(f"Monster.max_num = {wolf1.max_num}")
print(f"Monster.max_num = {Monster.max_num}")

shark1 = Shark("상어", 3000, 400)
shark1.move()
print(f"Monster.max_num = {shark1.max_num}") # 공유됨을 확인할 수 있음

dragon1 = Dragon("용", 8000, 800)
dragon1.move()
dragon1.use_skills()
print(f"Monster.max_num = {dragon1.max_num}")
