from django.conf.urls import url

from djangoecommerce_company.views import IndexView

app_name = 'djangoecommerce_company'

urlpatterns = [
    url(r'^$', IndexView, name='homepage')
]
