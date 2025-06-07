

from django.contrib import admin
from django.urls import path
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recepies/', recepies, name='recepies'),
    path('delete/<id>/', delete_recepie, name='delete_recepie'),
    path('update/<id>/', update_recepie, name='update_recepie'),
    path('login/', login_page,name='login'),
    path('register/', register,name='register'),
    path('logout/', logout_page,name='logout_page'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files
urlpatterns += staticfiles_urlpatterns()
