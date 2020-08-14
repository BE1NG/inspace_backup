from django.contrib import admin
from django.urls import path
import inspace.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inspace/write/', views.write),
    path('coord_to_address/', views.coord_to_address),
    path('inspace/signup/', views.signup),
    path('signup/check_id/', views.check_id),
    path('inspace/signin/', views.signin),
    path('inspace/signout/', views.signout),
    path('inspace/mypage/', views.mypage),
    path('inspace/main/', views.main),
    path('inspace/comment/', views.comment),
    path('inspace/comment/<int:id>/', views.comment_id),
    path('inspace/posting/<int:id>/', views.posting_id),
]
