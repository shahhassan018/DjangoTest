from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns=[
    url(r'^user_profile/', views.User_Profiles),  #For Create User Profile
    url(r'mydata/(?P<pk>[0-9]+)', views.myData),

    url(r'^view_items/', views.View_Items),  #User will able to view all list of dataitems with authentication
    url(r'^post_items/', views.Post_Items),  #User will able to post data in case of authentication
    url(r'^get_items/(?P<pk>[0-9]+)', views.Get_Items), # Items will show according to particular user
    url(r'^edit_items/(?P<pk>[0-9]+)', views.Edit_Items) #authenticated User will able to edit list of his own dataitems
]


