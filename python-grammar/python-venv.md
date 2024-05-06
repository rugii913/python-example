## Python 가상 환경 관련 메모

### 가상 환경 생성 명령어
- python -m venv [생성할 가상 환경 이름]

### 가상 환경 실행 명령어
- [가상 환경 경로]/Scripts/activate

### 가상 환경 내 패키지 리스트 보기 명령어
- pip list
- cf. pip는 Python 패키지 관리자 - 다른 사람이 만들어놓은 파이썬 소스 파일을 다운로드 받아서 pc 환경 혹은 가상 환경에 설치해주는 것 

### 가상 환경에 새로운 패키지 설치
- pip install [설치할 패키지 이름]
  - ex. pip install requests
    - 설치 후 pip list 해보면 requests 패키지 및 transitive dependency가 있는 다른 패키지까지 설치되어있음을 확인 가능
