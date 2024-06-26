from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .forms import CsRegisterForm, LoginForm
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.http import JsonResponse

#회원가입
class CsRegisterView(CreateView):
    model = Users
    template_name = 'accounts/signup.html'
    form_class = CsRegisterForm
    success_url = reverse_lazy('accounts:login')
    #reverse(): 클래스 변부분으로 해당 소스 파일이 임포트 되면서 클래스정의가 이루워질떄 호출된다
    #이 시점이 프로젝트 포기화 이전이기 떄문에 reverse에 실패하게 됨

    #reverse_lazy: reverse를 수행하는 싯점이 실제로 reverse값을 참조하는 시점으로 지연되어 수행됨

    #**따라서 클래스형 뷰에서는 reverse_lazy를 사용하고 
    #def형 뷰 / model에서는 def를 따로 지정해주니까 reverse를 사용한다    
    def form_valid(self, form):
        storage = messages.get_messages(self.request)
        storage.used = True  # 이전 메시지를 모두 소비하여 삭제합니다.
        messages.success(self.request, "회원가입 성공하였습니다. 로그인 해주세요")
        return super().form_valid(form)

#회원가입 시 중복 체크
def duplicate_check(request):
    user_id = request.GET.get('label_user_id')
    try:
        user = Users.objects.get(user_id=user_id)
        duplicate = "fail"
    except Users.DoesNotExist:
        duplicate = "pass"
    
    return JsonResponse({'duplicate': duplicate})

def check_user_id_view(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id', '')  # GET 요청으로부터 아이디 가져오기
        print(user_id)
        if Users.objects.filter(user_id=user_id).exists():  # 아이디가 이미 존재하는지 확인
            data = {'is_taken': True}  # 이미 사용 중인 경우
         
        else:
            data = {'is_taken': False}  # 사용 가능한 경우
        print(data)
        return JsonResponse(data)  # JSON 형식으로 응답
    

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        user_id = form.cleaned_data.get("user_id")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=user_id, password=password)
        print(user)
        if user is not None:
            self.request.session['user_id'] = user_id
            print(self.request.session['user_id'])
            login(self.request, user)
            response=super().form_valid(form)
            #self.request.session['user_id'] = user_id
            response.set_cookie('user_id',user_id)
        return response


def logout_view(request):
    logout(request)
    return redirect('/index/')
