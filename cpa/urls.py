from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.homepage, name='home'),
    path('account/', include('account.urls')),
    path('profiles/', include('profiles.urls')),
    path('ctcs/', include('ctcs.urls')),
    path('ctcs2/', include('ctcs2.urls')),
    path('semplan/', include('semplan.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
