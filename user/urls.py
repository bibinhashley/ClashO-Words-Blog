from django.urls import path
from . import views as user_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', user_views.LoginFormView.as_view(), name='login'),
    path('logout/', user_views.logout_request, name='logout'),
    path('<str:username>/', user_views.profile, name='profile'),
    path('<str:username>/social/', user_views.addsocial, name='social'),
    path('post/new/', user_views.CreatePost.as_view(), name='post_create'),
    path('post/<int:pk>/', user_views.PostDetail.as_view(), name='post_detail'),
    path('<str:username>/drafts', user_views.DraftListView.as_view(), name='drafts'),
    path('post/new/publish/', user_views.publish, name='publish'),
    path('<str:username>/posts/',
         user_views.PublishedPosts.as_view(), name='post_list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
