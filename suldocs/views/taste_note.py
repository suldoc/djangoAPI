from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render
from django.http import HttpResponse

from suldocs.models.taste_note import TasteNoteModel, TasteNoteSerializer
from suldocs.form import PostForm

from suldocs import dbconnetion


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


def TasteNoteDB(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        note_data = form.save(commit=False)
        if form.is_valid():
            note_data.save()

        #TODO: html화면 변경(모바일대응, 저장 후 피드백, 술종류 선택)
        conn = dbconnetion.get_connection()
        cur = dbconnetion.get_cursor(conn)

        SQL = "SELECT COUNT(*) AS count FROM suldocs_tastenotemodel"
        cur.execute(SQL)
        num = cur.fetchall()
        num = num[0]['count']
        # print(num[0]['count'])

        return render(request, 'notes/db.html', {"form": form, "num": num})

    if request.method == "GET":
        form = PostForm()
        return render(request, 'notes/db.html', {"form": form})