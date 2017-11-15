from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mysite import settings

admin.autodiscover()



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('registrationmod.urls')),
   
    url(r'^booking/', include('booking.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


