from django.urls import path
from .views import SignUpView, ProfileView, UpdateProfileView, AddRemoveSavedView, SavedView, RecentlyViewedView
app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('addremovesaved/<int:product_id>/', AddRemoveSavedView.as_view(), name='addremovesaved'),
    path('saveds/', SavedView.as_view(), name='saved'),
    path('recently-viewed/', RecentlyViewedView.as_view(), name='recently_viewed'),

]