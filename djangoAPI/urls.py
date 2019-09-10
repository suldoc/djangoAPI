from suldocs.views.user import User
from suldocs.views.taste_note import TasteNote

# router = routers.DefaultRouter()
# router.register('user', UserModel)

from django.urls import path

urlpatterns = [
    path('', User.as_view(), name="user"),
    path("taste", TasteNote.as_view(), name='taste'),
]
