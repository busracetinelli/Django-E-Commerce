from django.conf.urls import url

from djangoecommerce_web.views import IndexView, ProductDetailView, BlogDetailView,ContactView

app_name = 'djangoecommerce_web'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^urun/(?P<id>[-\w]+)/$',ProductDetailView, name='product_detail'),
    url(r'^contact/$', ContactView, name='contact'),
]
