from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'})
    )
    bio = forms.CharField(
        max_length=200, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short bio (optional)'})
    )
    location = forms.CharField(
        max_length=100, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Chennai, India'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap class to all fields automatically
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'e.g. How does a three-phase induction motor work?',
            })
        }