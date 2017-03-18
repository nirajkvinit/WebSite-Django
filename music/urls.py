from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="music"

urlpatterns=[
    url(r"^$",views.IndexView.as_view(),name="index"),
    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="detail"),
    #/music/id/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name="favorite"),
    #Album Add
    url(r'album/add/$',views.AlbumCreate.as_view(),name="album-add"),
    #Album Update
    url(r'/album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name="album-update"),
    #Album Delete
    url(r'/album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name="album-delete"),
    url(r"^/song$", views.SongView.as_view(), name="all-song"),
    #Register
    url(r"^/register/$",views.register,name="register"),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^user/(?P<name>.*)/$', views.ProfileView.as_view(), name="profile"),

   # url(r'^/user/(?P<user_id>[0-9]+)/$', views.ProfileView.as_view(), name='profile'),

]



