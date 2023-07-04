from django.contrib import admin
from django.urls import path, include
from core import views
from services import urls as services_urls
from blog import urls as blog_urls
from pages import urls as pages_urls
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('blog/', include(blog_urls)),
    path('about/', views.about, name='about'),
    path('sample/', include(pages_urls)),
    path('services/', include(services_urls)),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
