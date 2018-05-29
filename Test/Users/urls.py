from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from Users import views

urlpatterns=[
    url(r'^userprofile/', views.UserProfiles),

]


