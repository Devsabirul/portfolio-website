from django.shortcuts import redirect, render
from login.forms import HandelLoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = HandelLoginForm(request.POST, data=request.POST)
            if fm.is_valid():
                user_name = fm.cleaned_data['username']
                user_password = fm.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    return redirect('/dashboard/')
        else:
            fm = HandelLoginForm()
        return render(request, 'login/login.html', {'form': fm})
    else:
        return redirect("/dashboard")

# logout


def user_logout(request):
    logout(request)
    return redirect('/SS-admin')
