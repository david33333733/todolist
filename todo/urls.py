from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TodoUpdateView, TodoDeleteView

app_name = "todo"

#list_view 목록보기
urlpatterns =[
    path("", TodoListView.as_view(), name="list"), # 127.0.0.1:8000/todo/
    path("<int:pk>", TodoDetailView.as_view(), name="detail"), #상세보기 id가 필요합니다.
    path("create/", TodoCreateView.as_view(), name="create"), # 127.0.0.1:8000/todo/create/
    path("<int:pk>/update/", TodoUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", TodoDeleteView.as_view(), name="delete"),
]