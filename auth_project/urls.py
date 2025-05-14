from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('register.urls')),
    path('register/',include('register.urls')),
    path('login/',include('login.urls')),
    path('mentalHealthInfo/',include('mentalHealthInfo.urls')),
    path('logout/',include('logout.urls')),
    path('aboutus/',include('aboutus.urls')),
    path('meditation/',include('meditation.urls')),
    path('groupTherapy/',include('groupTherapy.urls')),
    path('individualTherapy/',include('individualTherapy.urls')),
    path('physicalExercise/',include('physicalExercise.urls')),
    path('self/',include('self.urls')),
    path('jounnaling/',include('jounnaling.urls')),
    path('podcast/',include('podcast.urls')),
    path('quote/',include('quote.urls')),
    path('video/',include('video.urls')),
    path('contact/',include('contact.urls')),
]