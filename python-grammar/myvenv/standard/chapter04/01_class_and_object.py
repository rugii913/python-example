# 절차적 vs. 객체 지향
## 절차적 프로그래밍: 기능들을 어떤 순서로 처리할 것인가에 초점
## 객체 지향 프로그래밍: 객체가 중심이 되고, 객체를 정의, 객체 간 상호작용에 초점
## - 프로그램 규모가 커지면 객체 지향 프로그래밍이 더 유용

# 클래스와 객체의 개념 - 생략
class EmptyClass:
    pass # 빈 클래스라면 pass라도 적어줘야함

class Post:
    # 생성자(constructor): 객체를 생성할 때 호출하는 메서드
    def __init__(self, title: str, content: str):
        # 객체 생성 시 __init__에서 받은 인자를 객체 자기 자신인 self의 속성으로 설정
        self.title = title
        self.content = content
        self.title_and_content = title + content # 받은 인자와 속성이 1:1로 일치할 필요는 없음

    def __str__(self): # __str__(): 객체를 출력할 때 호출되는 메서드
        return f"제목: {self.title}, 내용: {self.content}"

post1 = Post("제목1", "내용1")
print(post1) # __str__() 메서드가 정의되지 않은 경우 <__main__.Post object at 0x0000024A8F568710> 이런 식으로 출력됨
