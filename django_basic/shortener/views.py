from django.http.response import JsonResponse
from shortener.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# cf . templates 폴더에 있는 html을 렌더링하도록 연결해주려면,
#       settings.py 파일 중 TEMPLATES 부분 중에 'DIRS': [os.path.join(BASE_DIR, "templates")], 로 수정해줘야 함
def index(request):
    user = User.objects.filter(username="admin").first() # Django ORM 사용 예시
    # user = User.objects.get(username="admin") # Django ORM에서 get()은 반드시 한 개이며, 존재하는 것이어야 하므로 없을 경우 에러 발생함, 보통 validation 필요 시 사용
    email = user.email if user else "Anonymous User" # user가 있는 경우와 없는 경우(None) 구분해서 할당
    return render(request, "base.html", {"welcome_msg": f"Hello {email}"}) # 어떤 템플릿을 렌더링하는지 명시, JSON 형태의 데이터를 넘겨줄 수 있음

@csrf_exempt # Django는 기본적으로 csrf 토큰을 발급, 요청 위변조 방지 - @csrf_exempt는 csrf 체크를 하지 말라는 것 - Postman으로 체크할 때는 이 데코레이터를 붙여줌
# 아예 csrf 토큰 발급, 체크를 꺼두려면 settings.py 중 MIDDLEWARE = [..]에서 "...CsrfViewMiddleware" 부분을 주석 처리
def get_user(request, user_id): # path variable을 받음 urls.py 참고
    print(user_id)
    if request.method == "GET":
        abc = request.GET.get("abc") # query string을 알아서 파싱함
        xyz = request.GET.get("xyz")
        user = User.objects.filter(pk=user_id).first()
        return render(request, "base.html", {"user": user, "params": [abc, xyz]})
    elif request.method == "POST":
        username = request.GET.get("username")
        if username:
            user = User.object.filter(pk=user_id).update(username=username)
        return JsonResponse(status =201, data=dict(msg="You just reached with Post Method!")) # 템플릿으로 보내는 게 아니라 JSON으로 응답
        # return JsonResponse(dict(msg="POST 메서드"), safe=False) # 한글이 포함된 경우 safe=False로 보내야 오류 방지
