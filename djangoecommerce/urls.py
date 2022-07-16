from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',  include("djangoecommerce_web.urls")),
    url(r'^musteri/', include("djangoecommerce_customer.urls")),
    url(r'^sirket/', include("djangoecommerce_company.urls")),
    url(r'^blog/', include("djangoecommerce_blog.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
