
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import update_session_auth_hash,logout
from django.views.decorators.http import require_http_methods
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomCsUserChangeForm


# Create your views here.
def information(request):
    return render(request,'user_inform/information.html',{})


    
def profile_update_view(request):
    if request.method == 'POST':
        user_change_form = CustomCsUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return redirect('user_inform:information')
    else:
        user_change_form = CustomCsUserChangeForm(instance = request.user)

        return render(request, 'user_inform/modifyinform.html', {'user_change_form':user_change_form})
    

@login_required
def password_edit_view(request):
    if request.method == 'POST':
        password_change_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            storage = messages.get_messages(request)
            storage.used = True  # 이전 메시지를 모두 소비하여 삭제합니다.
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다. 다시 로그인 해주세요")
            logout(request)
            return redirect('accounts:login')
            # return redirect('user_inform:information')
    else:
        password_change_form = CustomPasswordChangeForm(request.user)
    
    # messages.get_messages(request)
    return render(request, 'user_inform/modifypw.html', {'password_change_form':password_change_form})