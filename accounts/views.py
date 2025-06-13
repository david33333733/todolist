from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')  # todo 앱의 리스트 페이지로 리다이렉트
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form}) # 여기에서 사용됨{{ form.as_p }}