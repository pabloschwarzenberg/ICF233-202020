from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView
from .views import login

urlpatterns = {
    url(r'^curso/$', CreateView.as_view(), name="create"),
    url(r'^curso/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
    url(r'api/login', login)
}
urlpatterns = format_suffix_patterns(urlpatterns)
