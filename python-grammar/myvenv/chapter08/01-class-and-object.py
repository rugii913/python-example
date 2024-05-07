# 클래스
## 클래스 만들기
class Monster:
    def say(self): # 모든 메서드의 첫번째 파라미터는 self
        print("나는 몬스터다")

## 클래스 사용하기
### 인스턴스 만들고 호출하기
monster1 = Monster()
monster1.say()

# cf. 파이썬에서 자료형은 클래스이다.
a = 10
b = "문자열 객체"
c = True

print(type(a))
print(type(b))
print(type(c))
print(type(monster1))

print(b.__dir__()) # 해당 객체의 메서드들을 확인할 수 있음
print(monster1.__dir__())
