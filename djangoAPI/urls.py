from suldocs.views.user import User
from suldocs.views.taste_note import TasteNote, TasteNoteDB


# router = routers.DefaultRouter()
# router.register('user', UserModel)

from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', User.as_view(), name="user"),
    path("taste", TasteNote.as_view(), name='taste'),
    path("db", TasteNoteDB, name='db'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
