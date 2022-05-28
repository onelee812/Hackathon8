from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST['password2']
        fond_user = User.objects.filter(username=username)
        if password != password2:
            error_msg = '두 비밀번호가 일치하지 않습니다.'
            return render(request, 'registration/signup.html', {
                'error_msg': error_msg,
                'username': username
            })
        if len(found_user):
            error = "이미 아이디가 존재합니다"
            return render(request, "registration/signup.html", {"error": error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        User.objects.create_user(username=username, password=password)
        return redirect("home")
    return render(request, "registration/signup.html")

def login(requst):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password) 
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        error = "아이디 또는 비밀번호가 틀립니다."
        return render(requst, "registration/login.html")
    return render(requst, "registration/login.html")

def logout(request):
    auth.logout(request)

    return redirect("home")