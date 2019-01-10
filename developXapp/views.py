from django.shortcuts import render
from django.views import View


class MainPage(View):
    def get(self, request):
        print("xxx")

        ctx = {}
        return render(request, "main_page.html", ctx)
