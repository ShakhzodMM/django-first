from .views import SignUpView, ProfileView, UpdateProfileView, AddRemoveSavedView, SavedView, RecentlyViewedView
from django.urls import path

app_name = 'users'  # => users:signup
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # Signup sahifasi uchun URL manzili
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),  # Profil sahifasi uchun URL manzili, username parametrini qabul qiladi
    path('update', UpdateProfileView.as_view(), name='update'),  # Profilni yangilash sahifasi uchun URL manzili
    path('addremovesaved/<int:product_id>', AddRemoveSavedView.as_view(), name='addremovesaved'),
    path('saveds', SavedView.as_view(), name='saveds'),
    path('recently-viewed', RecentlyViewedView.as_view(), name='recently_viewed')

]