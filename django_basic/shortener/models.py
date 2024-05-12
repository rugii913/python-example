from django.db import models

# 시작하기 전에 명령어 입력: python manage.py migrate → Django에서 필요로 하는 database를 만들어둠(admin, auth, contenttypes, sessions)

# 커스텀 모델 만들기
class PayPlan(models.Model):
    # Django는 PK를 명시적으로 지정하지 않으면, BigAutoField(auto increment인 BigIntegerField)인 id를 자동으로 갖게 함
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
# 위처럼 모델 코드를 작성한 후 명령어 입력 python manage.py makemigrations
# - 이 때 [프로젝트 루트]\[프로젝트명]\settings.py 파일 INSTALLED_APPS = [..] 리스트에 해당 app 이름이 추가되어있어야 함
#   - 여기서 No changes detected가 계속 출력되면 구글링해서 나오는 다른 방법 사용해보기
# - 그러면 [프로젝트 루트]\[앱명]\migrations 디렉토리에 0001_initial.py 같은 이름으로 생성된 파일 확인
# - 확인 됐으면 명령어 입력 python manage.py migrate
# - 그러면 [프로젝트 루트]\[앱명]\migrations\__pycache__ 디렉토리에 파일 생성된 것 확인, DB에도 반영되게 됨

# user 테이블에 슈퍼 사용자 만들기: python manage.py createsuperuser
# - Django에서 user 테이블은 알아서 생성해둠
## auth_user 테이블 확인 - 아래의 방법으로 확인 가능
## - 서버 실행 후 localhost:8000/admin으로 접속 후 users 확인
## - DBeaver 같은 툴을 이용해서 auth_user 테이블 등 여러 테이블 확인
