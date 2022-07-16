from django.conf.urls import url

from djangoecommerce_customer.views import IndexView

app_name = 'djangoecommerce_customer'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
]
