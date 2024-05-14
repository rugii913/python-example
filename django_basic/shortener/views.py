from shortener.models import User
from django.shortcuts import render, redirect

# Create your views here.

# cf . templates 폴더에 있는 html을 렌더링하도록 연결해주려면,
#       settings.py 파일 중 TEMPLATES 부분 중에 'DIRS': [os.path.join(BASE_DIR, "templates")], 로 수정해줘야 함
def index(request):
    user = User.objects.filter(username="admin").first() # Django ORM 사용 예시
    # user = User.objects.get(username="admin") # Django ORM에서 get()은 반드시 한 개이며, 존재하는 것이어야 하므로 없을 경우 에러 발생함, 보통 validation 필요 시 사용
    email = user.email if user else "Anonymous User" # user가 있는 경우와 없는 경우(None) 구분해서 할당

    print(request.user.is_authenticated)
    if request.user.is_authenticated is False:
        email = "Anonymous User"
    return render(request, "base.html", {"welcome_msg": f"Hello {email}"}) # 어떤 템플릿을 렌더링하는지 명시, JSON 형태의 데이터를 넘겨줄 수 있음

def redirect_test(request): # 직접 사용하지 않더라도 request를 받도록 명시함 - 이 requeset에 많은 정보를 담고 있음
    print("Do Redirect")
    return redirect("index") # 여기서 "index"는 위 함수 식별자 index가 아니라 urls.py에 path() 중 name에 지정된 값
