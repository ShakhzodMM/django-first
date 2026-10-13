from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, PasswordChangeView
from users.forms import MarketplaceAuthenticationForm, UzbekPasswordChangeForm

from django.conf import settings                                                             
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),  # Bosh sahifa uchun
    path('users/login/', LoginView.as_view(authentication_form=MarketplaceAuthenticationForm), name='login'),
    path('users/password_change/', PasswordChangeView.as_view(form_class=UzbekPasswordChangeForm), name='password_change'),
    path('users/', include('users.urls',)),  # Foydalanuvchilar uchun URL manzillarini qo'shish
    path('users/', include('django.contrib.auth.urls')),  # Foydalanuvchilar uchun URL manzillarini qo'shish
    path('products/', include('products.urls')),
]

# Ushbu qatorni urls.py faylining eng oxiriga qo'shing:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)