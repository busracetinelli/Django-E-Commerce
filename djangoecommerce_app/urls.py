from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include

from djangoecommerce import settings

app_name = 'djangoecommerce_app'
router = routers.DefaultRouter()

urlpatterns = \
    [
        url(r'^company/', include('djangoecommerce_company_api.urls')),
        url(r'^customer/', include('djangoecommerce_customer_api.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)