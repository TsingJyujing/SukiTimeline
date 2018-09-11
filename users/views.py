from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        # 请求为 POST，利用用户提交的数据构造一个绑定了数据的表单
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            print("User {} has login.".format(form.get_user()))
            return redirect("/")
        else:
            print("User {} login failed.".format(form.get_user()))
    else:
        # 请求不是 POST，构造一个空表单
        form = AuthenticationForm()
    return render(request, 'login.html', context={'form': form})
