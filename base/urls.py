

from django.urls import path
from .  import views




urlpatterns= [
    path('',views.home,name='home'),
    path('room/<str:url2>',views.room, name='room'),
   path('create_room/',views.create_room, name='create_room'),
   path('room/<str:url2>/update_room/',views.update_room,name="update-room"),
   path('room/<str:url2>/delete_room/',views.delete_room,name="delete-room"),
   path('register/',views.register,name="register"),
   path('login/',views.login_page,name="login"),
   path('logout/',views.logout_page,name="logout"),



    ]