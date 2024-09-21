from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views


urlpatterns = [
    path("", views.core, name="main"),
    path("home/", views.home, name="home"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("lobby/", views.home, name="lobby"),
    path("room/<str:pk>", views.room, name="room"),
    path("create-room", views.createroom, name="create-room"),
    path("update-room/<str:pk>/", views.updateroom, name="update-room"),
    path("delete-room/<str:pk>/", views.deleteroom, name="delete-room"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
