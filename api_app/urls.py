from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter


# creating Router object
router = DefaultRouter()

# Register Studentviewset with Router - the router will do all the crud operations here know need to mention any specific int or pk keywords
router.register('studentapi',views.StudentViewSet,basename= 'student')

urlpatterns= [
    path('',include(router.urls)),
]