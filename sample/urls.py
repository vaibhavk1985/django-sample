"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from custom_messages.views import InboxView, HomeView, MessageDeleteView
from custom_messages.forms import CustomComposeForm
from django_messages.views import compose
from .views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    re_path(r'^messages/inbox/$', InboxView.as_view(), name='messages_inbox'),
    re_path(r'^messages/compose/$', compose,
            {'form_class': CustomComposeForm, }, name='messages_compose'),
    re_path(r'^ajax/messages/delete/(?P<pk>[\d]+)/$', MessageDeleteView.as_view(), name='ajax_messages_delete'),
    re_path(r'^messages/', include('django_messages.urls')),
    path('user/', include('django.contrib.auth.urls')),
    # re_path(r"^notifications/", include("pinax.notifications.urls", namespace="pinax_notifications")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = handler404
handler500 = handler500
