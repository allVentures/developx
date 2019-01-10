from json import dumps

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from developXapp.forms import CashAmount


class MainPage(View):
    @staticmethod
    def notes_delivery(amount):
        avilable_notes = [10, 20, 50, 100]
        try:
            if amount == None:
                raise Exception([])
            if amount <= 0:
                raise Exception("InvalidArgumentException")
            if amount % 10 != 0:
                raise Exception("NoteUnavailableException")
            sub_amount = amount
            notes = []
            x = len(avilable_notes) - 1
            while sub_amount > 0:
                while x >= 0:
                    while sub_amount >= avilable_notes[x]:
                        sub_amount = sub_amount - avilable_notes[x]
                        notes.append(avilable_notes[x])
                    x = x - 1
        except Exception as e:
            notes = e
        return notes

    def get(self, request):
        form = CashAmount()
        ctx = {"form": form}
        return render(request, "main_page.html", ctx)

    def post(self, request):
        form = CashAmount(request.POST)
        if form.is_valid():
            cashamount = form.cleaned_data["cashamount"]

            msg = MainPage.notes_delivery(cashamount)
            ctx = {"form": form, "msg": msg}
            return render(request, "main_page.html", ctx)

        else:
            msg = "Form invalid, please try again!"
            ctx = {"form": form, "msg": msg}
            return render(request, "main_page.html", ctx)


# very simple API
class NotesAPI(View):
    def get(self, request):
        amount = request.GET.get('amount')
        if amount != None:
            try:
                notes = str(MainPage.notes_delivery(float(amount)))
            except ValueError:
                notes = "ValueError"
            response_data = {"notes": notes}
            return HttpResponse(dumps(response_data), content_type="application/json")
        else:
            ctx = {}
            return render(request, "api.html", ctx)
