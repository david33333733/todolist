from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'description', 'complete', 'exp']
    # 메타정보를 담는 클래스 참조하겠다는 뜻 폼을 참조하겠다.