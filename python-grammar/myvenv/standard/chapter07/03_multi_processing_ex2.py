# multi processing 예제 2
from multiprocessing import Process
import time

class Subprocess(Process): # 서브 프로세스를 클래스로 지정할 수도 있음

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
    p.join() # 서브 프로세스가 종료될 때까지 메인 프로세스가 종료되지 않고 기다리려면 join() 이용
    print("[main] end")
