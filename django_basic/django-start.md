## Django 설치 및 프로젝트 시작
- pip install django - 전역 Django 설치
- django-admin startproject [프로젝트명] → 전역 Django를 이용해 프로젝트 시작
  - [프로젝트명] 디렉토리가 생성되며 그 하위로 [프로젝트명] 디렉토리와 manage.py 파일이 있음

## 가상 환경 설치 및 가상 환경용 Django 설치, 서버 동작 확인
- python -m venv [가상 환경 이름] → 가상 환경 설치
  - .\[가상 환경 이름]\Scripts\activate → 터미널에서 해당 가상 환경 활성화
  - cf. 가상 환경 활성화된 상태에서 비활성화하려면 그냥 deactivate 입력
  - pip install django → 가상 환경의 Django 설치
- 가상 환경 Django까지 설치됐다면 이제 모두 manage.py를 통해 Django 프로젝트를 관리함
  - python manage.py runserver → 서버 띄우기
  - 브라우저에서 localhost:8000 요청하여 서버 잘 떠있는지 확인
  - (python manage.py migrate) → 터미널에서 경고 문구 있어서 실행해줬음

## Django 프로젝트에 새로운 app 만들어보기
- Django 프로젝트 안에 사용자가 들어오는 app과 백오피스 app을 분리해보기
  - python manage.py startapp [앱 이름] → 여기서는 사용자가 들어오는 앱을 만들어줬음
  - 그러면 [프로젝트명] 디렉토리에 이제 [앱 디렉토리], [프로젝트명 디렉토리], ... 등이 존재
  - python manage.py runserver → 서버 잘 뜨는지 다시 확인해보기
