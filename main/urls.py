from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('news/', views.news, name='news'),
    path('index1/', views.addpage, name='index1'),
    path('reg/', views.reg, name='reg'),
    # path('labka/', views.send_message, name='labka'),
    path('index/', views.index),
   
    # path('login/', views.loginPage, name='login'),
    # path('logout/', views.logoutUser, name='logout'),
    path('test/', views.test, name='test'),
    # path('user/', views.userPage, name='user-page'),
  
    # path('register/', views.registerPage, name='register'),
    
    # path('news_home/', views.news_home, name='add-post'),
    
    # path('forupload/', views.forupload, name='video-upload'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)