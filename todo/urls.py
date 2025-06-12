from django.urls import path
from .views import TodoListView, TodoDetailView

app_name = "todo"

#list_view 목록보기
urlpatterns =[
    path("", TodoListView.as_view(), name="list"), # 127.0.0.1:8000/todo/
    path("<int:pk>", TodoDetailView.as_view(), name="detail"), #상세보기 id가 필요합니다.
]