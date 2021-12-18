from django.conf.urls import url
from codestar import views

urlpatterns = [
    url('run',views.runcode),
    url('',views.greetings),
]
