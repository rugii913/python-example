# multi processing 예제 3
from multiprocessing import Process
import time

class Subprocess(Process):

    def __init__(self, name):
        Process.__init__(self)
        self.name = name
    
    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(2)
        print(f"[sub] {self.name} end")

if __name__ == "__main__":
    print("[main] start")
    p = Subprocess(name="startcoding")
    p.start()
    time.sleep(1)
    # 자식 프로세스가 살아있는지 검사 후 살아있다면 강제 종료
    print(p.is_alive())
    if (p.is_alive()):
        p.terminate()

    print("[main] end")

## 추가 학습해볼만 한 내용
## 1. 스레드 간 데이터 처리(lock)
## 2. 프로세스 간 데이터 전공(Queue, Pipe)
## 3. 속도 비교
## 4. 운영체제와 메모리
