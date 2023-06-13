from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from django.shortcuts import HttpResponse
from app01 import models


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", required=True)
    password = forms.CharField(label="密码", required=True, widget=forms.PasswordInput(render_value=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"
            field.widget.attrs['placeholder'] = "请输入{}".format(field.label)


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'login.html', {'form': form})

    # 错误用户名或密码
    user_object = models.UserInfo.objects.filter(**form.cleaned_data).first()
    if not user_object:
        return render(request, 'login.html', {'form': form, 'error': '用户名或密码错误'})



    # 登录成功
    request.session['user_info'] = {'id': user_object.id, 'username': user_object.username, 'role': user_object.role}
    return redirect('/home/')


def home(request):
    return render(request, 'home.html')


def logout(request):
    request.session.clear()
    return redirect('/login/')