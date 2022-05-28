from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .riot_api import getSummonerInfo


DEVELOPMENTAPIKEY = "RGAPI-7a114fe7-dd1d-425b-b9d4-53445b3cac1a"
# summonerName = "ㅂㄷㄱ"

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        summoner_name = request.POST["summoner_name"]
        summoner_data = getSummonerInfo(DEVELOPMENTAPIKEY, summoner_name)
        if "status" in summoner_data:
            context = {"summoner_error_msg": "유효하지 않는 소환사명입니다."}
            return render(request, "signup.html", context)
        found_user = User.objects.filter(username=username)
        if password != password2:
            password_error_msg = "두 비밀번호가 일치하지 않습니다."
            return render(
                request,
                "signup.html",
                {"password_error_msg": password_error_msg, "username": username},
            )
        if len(found_user):
            error = "이미 아이디가 존재합니다"
            return render(request, "signup.html", {"error": error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        User.objects.create_user(username=username, password=password)
        return redirect("home")
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        error = "아이디 또는 비밀번호가 틀립니다."
        return render(request, "registration/login.html")
    return render(request, "registration/login.html")


def logout(request):
    auth.logout(request)

    return redirect("home")


def validation(request):