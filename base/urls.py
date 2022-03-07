

from django.urls import path
from .  import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [
    path('',views.home,name='home'),
    path('room/<str:url2>',views.room, name='room'),
   path('create_room/',views.create_room, name='create_room'),
   path('room/<str:url2>/update_room/',views.update_room,name="update-room"),
   path('room/<str:url2>/delete_room/',views.delete_room,name="delete-room"),
   path('register/',views.register,name="register"),
   path('login/',views.login_page,name="login"),
   path('logout/',views.logout_page,name="logout"),

   path('delete_message/<str:pk>/',views.delete_message,name="delete-message"),

   path('profile/<str:name>/',views.profile,name="profile"),
   path('profile/<str:name>/update/',views.update_profile,name="update-profile")



    ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)