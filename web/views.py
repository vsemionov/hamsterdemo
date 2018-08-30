from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from api.models import Note


def index(request):
    latest_notes = Note.objects.order_by("-id")[:10]
    context = {"notes": latest_notes}
    return render(request, "web/index.html", context)


@login_required
def require_auth(request):
    return HttpResponse("Thank you")
