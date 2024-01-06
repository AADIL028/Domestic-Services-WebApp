from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header='Domestico Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('services/', include('Services.urls')),
    path('account/', include('Account.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    #for setting media-url for images.