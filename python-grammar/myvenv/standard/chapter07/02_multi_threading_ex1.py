# multi threading 예제 1
import threading

## 서브 스레드에서 실행할 함수 정의
def work():
    print("[sub] start")
    keyword = input("[sub] 검색어를 입력하세요 >>> ")
    print(f"[sub] {keyword}로 검색을 시작합니다.")
    print("[sub] end")

## 메인 스레드 실행되는 부분
print("[main] start")

worker = threading.Thread(target=work)
worker.daemon = True # 서브 스레드의 daemon 속성을 True로 줘서 daemon thread로 만들 경우 메인 스레드가 종료될 때 서브 스레드도 함께 종료
worker.start()

print("[main] 메인 스레드는 메인 스레드의 일을 수행 후 종료")
print("[main] end")
