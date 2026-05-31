from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ask/', views.ask_view, name='ask'),
    path('history/', views.history_view, name='history'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
]