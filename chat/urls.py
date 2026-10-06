from django.urls import path
from . import views


urlpatterns = [

    path(
        "signup/",
        views.signup_view,
        name="signup"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
    "chat/",
    views.chat_view,
    name="chat"
    ),

    path(
    "chat/new/",
    views.new_chat,
    name="new_chat"
    ),

    path(
        "chat/<int:thread_id>/",
        views.chat_thread,
        name="chat_thread"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),
]