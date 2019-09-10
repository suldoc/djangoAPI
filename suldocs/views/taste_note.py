from rest_framework.response import Response
from rest_framework.views import APIView

from suldocs.models.taste_note import TasteNoteModel, TasteNoteSerializer


class TasteNote(APIView):
    def get(self, request):
        taste_notes = TasteNoteModel.objects.all()
        taste_notes_serialize = TasteNoteSerializer(taste_notes, many=True)

        return Response(taste_notes_serialize.data)

    def post(self, request):
        note_data = request.data

        return Response({"":""})

