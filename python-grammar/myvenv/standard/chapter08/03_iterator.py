# iterator

## iterable object
## - 순서가 있는 자료형: 문자열, 리스트, 튜플, 딕셔너리, range 객체, ...
ex_iterable = [10, 20, 30]
for i in ex_iterable:
    print(i)

print(dir(ex_iterable)) # → dir()로 까보면 __iter__라는 멤버를 갖고 있음
print(type(ex_iterable.__iter__)) # __iter__의 type은 method-wrapper → __iter__() 실행하면 iterator 객체를 만들어줌
print(type(ex_iterable.__iter__())) # iterator를 만들어준 것을 확인할 수 있음

ex_iterator1 = ex_iterable.__iter__()
for i in ex_iterator1: # 위 ex_iterable에 대해 작업했을 때와 결과는 같음
    print(i)

print(dir(ex_iterator1)) # __next__()를 갖고 있음
# print(ex_iterator.__next__) # StopIteration 이미 위 for에서 iteration을 끝냈기 때문에 StopIteration 오류 발생

ex_iterator2 = ex_iterable.__iter__()
print(ex_iterator2.__next__())
print(ex_iterator2.__next__())
print(ex_iterator2.__next__())
# 즉 iterable의 동작 방식은 __iter__()로 얻는 iterator 객체에서 __next__()를 사용하는 방식

# ------------------------------------ #

## iterator 생성 방법
## - iterator 클래스를 정의
## - __iter__ 메서드를 정의
## - __next__ 메서드를 정의

class Seasons:
    def __init__(self):
        self.season_list = ["spring", "summer", "autumn", "winter"]
        self.idx = 0
        self.max_num = 4
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < self.max_num: # 현재 상태에서는 self.idx == 4이면 else로 넘어가게 될 것
            curr_idx = self.idx
            self.idx += 1
            return self.season_list[curr_idx]
        else:
            raise StopIteration
        
for i in Seasons(): # 이렇게 작성하게 되면 알아서 __iter__()와 __next__()를 호출해서 그 결과를 i에 담아줌
    print(i)

iterator_seasons = Seasons().__iter__()
print(iterator_seasons.__next__())
print(iterator_seasons.__next__())
print(iterator_seasons.__next__())
print(iterator_seasons.__next__())
# print(iterator_seasons.__next__()) # 한 번 더 호출하면 StopIteration 오류
