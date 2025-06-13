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
    form_class = TodoForm
    template_name = "todo/todo_create.html"
    success_url = reverse_lazy("todo:list") #저장버튼 이후 이동할 페이지 왜 context없고 lazy는 무엇인가 14~20

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_update.html"
    context_object_name = "todos"
    # success_url = reverse_lazy("todo:list")
    def get_success_url(self):
        return reverse_lazy("todo:detail", kwargs={"pk": self.object.pk}) 

class TodoDeleteView(DeleteView): #삭제뷰 문법이다.
    model = Todo
    template_name = "todo/todo_delete.html"
    success_url = reverse_lazy("todo:list")
    context_object_name = "todos"