from django.conf.urls import url, patterns

urlpatterns = patterns('',
                       url(r'^login', 'loginsys.views.login'),
                       url(r'^logout', 'loginsys.views.logout'),
                       url(r'^register', 'loginsys.views.register'),
                       )
