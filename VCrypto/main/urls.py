from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('search_results/', views.search_results, name='search_results'),
    path('friends/', views.friends, name='friends'),
    path('search_results/send_friend_request/<int:userID>', views.send_friend_request, name='send_friend_request'),
    path('search_results/cancel_friend_request/<int:userID>', views.cancel_friend_request, name='cancel_friend_request'),
    path('search_results/decline_friend_request/<int:userID>', views.decline_friend_request, name='decline_friend_request'),
    path('search_results/accept_friend_request/<int:userID>', views.accept_friend_request, name='accept_friend_request'),
    path('search_results/unfriend/<int:userID>', views.unfriend, name='unfriend'),
]