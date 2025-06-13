from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path("todo/", include("todo.urls")),
    path("", lambda request: redirect("todo:list") ),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")) #accounts는 회원가입을 위한 앱인데 프로젝트 urls에 이줄 윗줄 두줄을 줘야 된다. 이건 그냥 문법임
]
