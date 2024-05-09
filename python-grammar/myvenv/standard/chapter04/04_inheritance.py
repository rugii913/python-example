# 상속

class Item:
    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다.")

    def discard(self):
        print(f"[{self.name}]을(를) 버렸습니다.")

class Weapon(Item):
    def __init__(self, name, demage):
        super().__init__(name)
        self.demage = demage
    
    def attack(self):
        print(f"[{self.name}]을(를) 이용해 {self.demage}로 공격합니다.")

class HealingItem(Item):
    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount
    
    def use(self):
        print(f"[{self.name}]을(를) 이용해 {self.recovery_amount}만큼 회복합니다.")

weapon1 = Weapon("weapon1", 110)
healing_item1 = HealingItem("healing_item1", 20)

weapon1.pick()
weapon1.attack()
healing_item1.use()
healing_item1.discard()

# ---------------------------- #

# 추상 클래스

from abc import *

class NewItem(metaclass=ABCMeta): # 추상 메서드를 이용하기 위해 필수
    def __init__(self, name):
        self.name = name

    def pick(self):
        print(f"[{self.name}]을(를) 주웠습니다.")

    def discard(self):
        print(f"[{self.name}]을(를) 버렸습니다.")

    @abstractmethod
    def use(self):
        pass

class NewWeapon(NewItem):
    def __init__(self, name, demage):
        super().__init__(name)
        self.demage = demage
    
    # def attack(self): use를 구현하지 않으면 오류 발생
    def use(self):
        print(f"[{self.name}]을(를) 이용해 {self.demage}로 공격합니다.")

class NewHealingItem(NewItem):
    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount
    
    def use(self):
        print(f"[{self.name}]을(를) 이용해 {self.recovery_amount}만큼 회복합니다.")

new_weapon1 = NewWeapon("new_weapon1", 110)
new_healing_item1 = NewHealingItem("new_healing_item1", 20)

new_weapon1.pick()
new_weapon1.use()
new_healing_item1.use()
new_healing_item1.discard()
