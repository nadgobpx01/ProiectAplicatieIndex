from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from accounts import views as account_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rute principale
    path('', core_views.home, name='home'),
    path('signup/', account_views.signup_view, name='signup'),
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),

    # Resetare parolă
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Aplicații
    path('accounts/', include('accounts.urls')),
    path('utilities/', include('utilities.urls')),
    path('user/', include('userloginmain.urls')),
    path('moneymanager/', include('moneymanager.urls')),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
