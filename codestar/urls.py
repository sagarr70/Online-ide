from django.conf.urls import url
from codestar import views

urlpatterns = [
    url('run',views.runcode),
    url('report',views.report),
    url('home',views.greetings),
    url('',views.greetings),

    
]
