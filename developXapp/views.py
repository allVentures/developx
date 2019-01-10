from django.shortcuts import render
from django.views import View

from developXapp.forms import CashAmount


class MainPage(View):
    def get(self, request):
        form = CashAmount()
        ctx = {"form": form}
        return render(request, "main_page.html", ctx)

    def post(self, request):
        form = CashAmount(request.POST)
        if form.is_valid():
            cashamount = form.cleaned_data["cashamount"]

            msg = cashamount
            ctx = {"form": form, "msg": msg}
            return render(request, "main_page.html", ctx)

        else:
            error = "Form invalid, please try again!"
            ctx = {"form": form, "error": error}
            return render(request, "main_page.html", ctx)
