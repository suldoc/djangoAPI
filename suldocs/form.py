from django import forms
from .models.taste_note import TasteNoteModel


class PostForm(forms.ModelForm):
    class Meta:
        model = TasteNoteModel
        fields = ('user_id', 'name', 'comment', 'stars_taste', 'stars_costvalue', 'img_path',
                  )
