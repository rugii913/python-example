## Python 설치 관련
- Python 설치 후 최신 버전 Python 이용하려면 환경 변수 변경 필요
  - 설치 중 옵션으로 환경 변수 설정까지 하도록 했다면 상관 없음
  - 만약 다른 Python 버전으로 변경하고 싶다면 해당 버전의 폴더를 환경 변수로 사용하도록 변경 필요
- python --version: 현재 Python 버전 확인

## pip 관련
- pip란?
  - Python 패키지 관리자
  - 다른 사람이 만들어놓은 파이썬 소스 파일을 다운로드 받아서 pc 환경 혹은 가상 환경에 설치해주는 것 
- pip 업그레이드 명령어 - 아래 둘 중 하나
  - python -m pip install --upgrade pip
  - pip install --upgrade pip
- pip list: 현재 설치된 패키지 확인
  - pip도 패키지 중 하나임을 확인 가능

## 가상 환경 관련
### 가상 환경 생성 명령어
- python -m venv [생성할 가상 환경 이름]

### 가상 환경 활성화(activate) 명령어
- [가상 환경 경로]\Scripts\activate
- cf. 비활성화하려면 활성화된 상태에서 deactivate 입력

### 가상 환경 내 패키지 리스트 보기 명령어
- 해당 가상 환경을 activate 한 뒤 pip list 입력

### 가상 환경에 새로운 패키지 설치
- pip install [설치할 패키지 이름]
  - ex. pip install requests
    - 설치 후 pip list 해보면 requests 패키지 및 transitive dependency가 있는 다른 패키지까지 설치되어있음을 확인 가능

## Django 설치 및 Django 프로젝트 시작
### 전역 pip를 이용하여 Django 설치 및 프로젝트 시작
- pip install django → 전역 Django 설치
- django-admin startproject [프로젝트명] → 전역 Django를 이용해 프로젝트 시작
  - [프로젝트명] 디렉토리가 생성되며 그 하위로 [프로젝트명] 디렉토리와 manage.py 파일이 있음
  - cf. [프로젝트명]에 "-" 가 포함될 수 없음

### 가상 환경 설치 및 가상 환경용 Django 설치, 서버 동작 확인
- python -m venv [가상 환경 이름] → 가상 환경 설치
  - .\[가상 환경 이름]\Scripts\activate → 터미널에서 해당 가상 환경 활성화
  - pip install django → 가상 환경의 Django 설치
- 가상 환경 Django까지 설치됐다면 이제 모두 manage.py를 통해 Django 프로젝트를 관리함
  - python manage.py runserver → 서버 띄우기
  - 브라우저에서 localhost:8000 요청하여 서버 잘 떠있는지 확인
  - (python manage.py migrate) → 터미널에서 경고 문구 있어서 실행해줬음
    - 참고 [장고(Django) - 마이그레이션(Migration)](https://tibetsandfox.tistory.com/24)

### Django 프로젝트에 새로운 app 만들어보기
- Django 프로젝트 안에 사용자가 들어오는 app과 백오피스 app을 분리해보기
  - python manage.py startapp [앱 이름] → 여기서는 사용자가 들어오는 앱을 만들어줬음
  - 그러면 [프로젝트명] 디렉토리에 이제 [앱 디렉토리], [프로젝트명 디렉토리], ... 등이 존재
  - python manage.py runserver → 서버 잘 뜨는지 다시 확인해보기
