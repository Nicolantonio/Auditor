from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('settings/', include('backend.urls')), # main will be the name of your app 
    path('', include('main.urls')), # main will be the name of your app 

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)