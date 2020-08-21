from django.urls import path, include
from .views import SignUp
from . import views
from django.contrib.auth import views as av
from .forms import CustomAuthenticationForm

app_name = 'accounts'
urlpatterns = [
    path('top', views.top, name = 'top'),
    path('signup/', SignUp.as_view(), name = 'signup'),
    path('login/', av.LoginView.as_view(form_class=CustomAuthenticationForm), name='login'),
    path('logout/', av.LogoutView.as_view(template_name = 'regstration/logout.html',next_page = 'accounts:top'), name = 'logout'),

    # パスワード変更・完了画面
    path('password_change/', av.PasswordChangeView.as_view(template_name = 'registration/password_change.html'), name='password_change'),
    path('password_change/done/', av.PasswordChangeDoneView.as_view(template_name = 'registration/password_change_done.html'), name='password_change_done'),

    # ユーザー情報・変更画面
    path('profile/', views.UserProfileView.as_view(), name="profile"),
    path('change/', views.UserChangeView.as_view(), name="change"),
]