from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.taste_note import TasteNoteModel

admin.site.register(TasteNoteModel)