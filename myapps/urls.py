from django.urls import path
from .views import login_view, logout_view, user_details ,SignUpView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_details/', user_details, name='user_details'),
    path('signup/', SignUpView.as_view(), name='signup'),
]