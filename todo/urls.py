from django.urls import path
from .views import TodoListView

app_name = "todo"

#list_view 목록보기
urlpatterns =[
    path("", TodoListView.as_view(), name="list"),
]