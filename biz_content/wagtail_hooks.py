from django.conf.urls import include, url
from django.core import urlresolvers
from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.menu import MenuItem
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from biz_content import views


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^dashboard/$', views.dashboard, name='wagalytics_dashboard'),
    ]


@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Analytics'),
        urlresolvers.reverse('wagalytics_dashboard'),
        classnames='icon icon-fa-bar-chart',
        order=1000
    )


@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Resource Matcher'),
        urlresolvers.reverse('admin:index'),
        classnames='icon icon-fa-map-pin',
        order=1000
    )
