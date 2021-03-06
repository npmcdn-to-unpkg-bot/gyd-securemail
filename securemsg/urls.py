from django.conf.urls import url

from . import views

app_name = 'securemsg'

urlpatterns = [
#    url(r'^encryptfile$', views.encryptfile, name='encryptfile'),
    url(r'^$', views.genkey, name='index'),
    url(r'^genkey$', views.genkey, name='genkey'),
    url(r'^sendfile_index$', views.sendfile_index, name='sendfile_index'),
    url(r'^send$', views.sendfile_index, name='sendfile_index'),
    url(r'^decrypt_index$', views.decrypt_index, name='decrypt_index'),
    url(r'^json_get_publickey', views.json_get_publickey, name='json_get_publickey'),
    url(r'^json_get_datareq', views.json_get_datareq, name='json_get_datareq'),
    url(r'^json_addkeymaster$', views.json_addkeymaster, name='json_addkeymaster'),
    url(r'^json_confirmemail$', views.json_confirmemail, name='json_confirmemail'),
    url(r'^json_addkey$', views.json_addkey, name='json_addkey'),
    url(r'^json_addencrypted$', views.json_addencrypted, name='json_addencrypted'),
    url(r'^login/(?P<confirmation>[-\w]+)/$', views.login, name='login'),
    url(r'^.well-known/acme-challenge/VsvwecbgW-4Wo3pQxxcQVRL3vSN93yy7cGXQDF9vACU$', views.acme_challenge, name='acme_challenge')
]
