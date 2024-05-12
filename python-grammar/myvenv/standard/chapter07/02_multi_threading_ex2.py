# multi threading 예제 2
import threading
import time

def buyer():
    for i in range(3):
        print("[매수] 데이터 요청 중...")
        time.sleep(0.2)
        print("[매수] 데이터 분석 중...")
        time.sleep(0.2)
        print("[매수] 매수 적합 시점 판단 중...")
        time.sleep(0.2)
        print("[매수] 매수 진행...")
        time.sleep(0.2)

def seller():
    for i in range(3):
        print("[매도] 데이터 요청 중...")
        time.sleep(0.2)
        print("[매도] 데이터 분석 중...")
        time.sleep(0.2)
        print("[매도] 매도 적합 시점 판단 중...")
        time.sleep(0.2)
        print("[매도] 매도 진행...")
        time.sleep(0.2)

## 메인 스레드
print("[메인] start")

buyer_thread = threading.Thread(target=buyer)
seller_thread = threading.Thread(target=seller)

buyer_thread.start()
seller_thread.start()

buyer_thread.join() # join()한 서브 스레드가 종료될 때까지 메인 스레드가 종료되지 않고 기다림
seller_thread.join() # join()한 서브 스레드가 종료될 때까지 메인 스레드가 종료되지 않고 기다림

print("[메인] end")
