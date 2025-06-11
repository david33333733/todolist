from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo
# 전체목록보기
#모델불러오기
#템플릿으로 이동하기
#이름표= todo
#오늘 생성한 데이터만 후입선출 방식으로 불러오기
class TodoListView(ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "todos"
    ordering = ["-created_at"]