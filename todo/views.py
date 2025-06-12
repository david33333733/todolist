from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm
from django.urls import reverse_lazy


# 전체목록보기 API
# 모델불러오기
# 탬플릿으로 이동하기
# 이름표= todo
# 후입선출 방식으로 불러오기
class TodoListView(ListView):
    model = Todo # 무조건
    template_name = "todo/todo_list.html" # 두번째 무조건
    # todo/templates/todo/todo_list.html
    context_object_name = "todos" # todos.name 옵션
    ordering = ["-created_at"] #옵션

class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo/todo_detail.html"
    context_object_name = "todos"

class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo/todo_detail.html"
    context_object_name = "todos"

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todo/todo_detail.html"
    context_object_name = "todos"

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo/todo_detail.html"
    context_object_name = "todos"