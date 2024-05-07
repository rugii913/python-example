# 모듈

## 왜 사용하는가: 프로그램 기능별로 파일을 나눠 유지보수 등 관리를 편하게

## 모듈이란: 한 개의 완성된 프로그램 파일 - [파일명].py 하나 하나가 모듈이라고 생각하면 됨

## 파이썬 기본(내장) 모듈 사용 방법
## - import [모듈명] - ex. import math
## - [모듈명].[변수명] - ex. print(math.pi)
## - [모듈명].[함수명]() - ex. print(math.ceil(5.7))
from math import pi, ceil as ce # 이렇게 from [모듈명] import [변수명] 혹은 [함수명] 이렇게 지정할 경우 아래처럼 간편하게 사용 가능

print(pi)
print(ce(2.7))

## 파이썬 외부 모듈 사용 방법
## - pip install [모듈명] - ex. pip install pyautogui
## - cf. PyAutoGUI - https://pyautogui.readthedocs.io/en/latest/
import pyautogui as pg

pg.moveTo(500, 500, duration = 0.5)

## 커스텀 모듈 사용해보기
### cf. Pylance에서 내장 모듈이 아닌 모듈 import 시 밑줄 보이는 문제 관련 - 아래처럼 수정하지 않아도 실행은 가능함
### - VS Code settings.json(파일 > 기본 설정 > 설정(단축키 Ctrl + ,))에 다음 추가
### - "python.analysis.extraPaths": ["{현재 디렉토리 경로}"],

### 실행 후 __pycache__ 파일이 생성되는데, 무시해도 됨
import pay_module

### 변수 사용
print(pay_module.version)

### 함수 사용
pay_module.printAuthor()

### 클래스 사용
pay_info = pay_module.Pay("A102030", 13_000, "2024-01-01")
pay_info.get_pay_info()

### cf. __name__ 변수 관련 - 해당 파일을 직접 실행했을 때와 import 했을 때 __name__이 다름
### - 직접 실행할 경우 __name__ == "__main__"
print(pay_module.__name__)
