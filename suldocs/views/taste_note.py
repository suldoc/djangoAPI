from rest_framework.response import Response
from rest_framework.views import APIView

from suldocs.models.taste_note import TasteNoteModel, TasteNoteSerializer


class TasteNote(APIView):
    def get(self, request):
        taste_notes = TasteNoteModel.objects.all()
        taste_notes_serialize = TasteNoteSerializer(taste_notes, many=True)

        return Response(taste_notes_serialize.data)

    def post(self, request):
        try:
            note_data = request.data

            tastenote_data = TasteNoteModel()

            note_data_keys = ['user_id', 'name', 'comment', 'stars_taste', 'stars_costvalue', 'img_path']

            if list(note_data.keys()) == note_data_keys:
                tastenote_data.user_id = note_data['user_id']
                tastenote_data.name = note_data['name']
                tastenote_data.comment = note_data['comment']
                tastenote_data.stars_taste = note_data['stars_taste']
                tastenote_data.stars_costvalue = note_data['stars_costvalue']
                tastenote_data.img_path = note_data['img_path']

                tastenote_data.save()

            else:
                return Response({"Result":"is not allowed"})

            return Response({"Result":"SUCCESS"})

        except (ValueError, TypeError) as e:
            return Response({"Result":e})
