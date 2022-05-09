from django.urls import path, include

from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'tests',views.TestView,'test')


urlpatterns=[
    path('test/',views.test1,name='test'),
    path('api/', include(router.urls))
]