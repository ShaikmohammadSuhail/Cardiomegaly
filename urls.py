from django.urls import path
from. import views


urlpatterns=[

    path('',views.index,name="index"),
    path('base',views.base,name="base"),
    path('about',views.about,name="about"),
    path('upload',views.upload,name="upload"),
    path('register',views.register,name="register"),
    path('login',views.logins,name="login"),
    path('result',views.result,name="result"),
]
