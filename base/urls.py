from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('rooms/', views.home_rooms, name='rooms'),
    path('room/<str:pk>/', views.room_page, name='room_page'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('update-user/', views.updateUser, name="update-user"),

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),



    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),



    path('upload_notes/', views.upload_notes, name="upload_notes"),


    path('login/', views.login_reg, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/',views.log_out,name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
