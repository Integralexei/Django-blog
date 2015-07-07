from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
                       url(r'^login', 'loginsys.views.login'),
                       url(r'^logout', 'loginsys.views.logout'),
                       )
