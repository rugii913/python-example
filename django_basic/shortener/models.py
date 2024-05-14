from django.db import models
from django.contrib.auth.models import AbstractUser # 방법 1 관련
# from django.contrib.auth.models import User # → 방법 2 관련, Django가 갖고 있는 기본 User 모델

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


# user 테이블 커스터마이징 하기 - 이번에는 방법 1 사용
## 방법 1 - AbstractUser 이용, 한 테이블만 사용함
## - ** user 모델을 바꿔줘야 하므로 settings.py에서 AUTH_USER_MODEL = "shortener.User"을 명시해줘야 함 **
class User(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING) # Django 기본 User 모델에는 이런 게 없기에 넣기 위해 새로운 User 모델 작업을 한 것

## 방법 2 - Django 기본 제공 user 모델 이용 + 여기에 필드를 추가한 모델을 함께 이용 → 데이터가 두 테이블에 쌓임
# class UserDetail(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)

## ** 방법 1, 2 중 하나를 선택한 후 python manage.py makemigrations 입력, python manage.py migrate 입력 **

## cf. 전체 테이블들을 확인해보면
##     - auth_로 시작하는 테이블: 인증을 위해 사용하는 테이블들
##     - django_로 시작하는 테이블: Django가 직접 사용하는 테이블들
##     - 그 외(여기서는 shortener_로 시작하는) 테이블: 개발자가 models.py에서 정의한 테이블들

## cf. 이미 맨 처음에 python manage.py migrate로 auth_user 테이블을 생성한 상태에서 users 혹은 user 테이블로 바꾸려면 오류 발생할 수 있음
##     - 다음과 같은 메시지 The field admin.LogEntry.user was declared with a lazy reference to '...', but app '...' doesn't provide model 'user'.
##     - https://velog.io/@cjyooong/이슈-Django-User-모델-확장AbstractUser
##     - https://jheaon.tistory.com/49
##     - 기본 migration을 적용한 뒤 user 테이블을 수정할 수 있는 방법이 존재하는지 모르겠음
##     - 이번에는 DB 테이블 날리고, migrations 안에 있는 __init__.py 제외한 파일들, __pycache__ 안에 있는 모든 파일 날린 후 다시 migration 진행함

