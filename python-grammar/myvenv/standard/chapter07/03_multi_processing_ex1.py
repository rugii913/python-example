# multi processing 예제 1
import multiprocessing as mp

## 프로세스에서 실행할 함수
def sub_process(name):
    print("[sub] start")
    print(name)

    current_process_1 = mp.current_process()
    print(f"[sub] pid: {current_process_1.pid}")

    print("[sub] end")

## 메인 프로세스
if __name__ == "__main__": # Windows 운영체제에서는 이 부분이 반드시 필요함 - https://docs.python.org/2/library/multiprocessing.html#multiprocessing-programming
    print("[main] start")

    process1 = mp.Process(target=sub_process, args=("startcoding",))
    process1.start()

    current_process_1 = mp.current_process()
    print(f"[main] pid: {current_process_1.pid}")

    print("[main] end")
