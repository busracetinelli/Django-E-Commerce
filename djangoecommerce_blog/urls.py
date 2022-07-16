from django.conf.urls import url
from djangoecommerce_blog.views import CategoryListView, BlogListView, BlogDetailView,HashtagListView


app_name = 'djangoecommerce_blog'


urlpatterns = [
    url(r'^$', BlogListView, name='homepage'),
    url(r'^(?P<slug>[-\w]+)/$',BlogDetailView, name='blog_single'),
    url(r'^category/(?P<category_slug>[-\w]+)/$',CategoryListView, name='category_all'),
    url(r'^hashtag/(?P<hashtag>[-\w]+)/$',HashtagListView, name='hashtag'),
]
