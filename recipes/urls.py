from django.conf.urls.defaults import *
from .views import test


urlpatterns = patterns('',
    # Example:
    (r'^', test),
)
