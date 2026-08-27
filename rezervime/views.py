from django.shortcuts import render
from datetime import date, datetime
import re

from .models import Rezervim, Service

def index(request):

    return render(request, "index.html")

def rreth_nesh(request):
    return render(request, "rreth-nesh.html")

def kontakt(request):
    context = {
        "form_data": request.POST,
        "service_choices": Rezervim.SHERBIMI_CHOICES,
        "time_choices": Rezervim.ORA_CHOICES,
    }
    if request.method == "POST":
        form_data = request.POST
        errors = {}

        if len(form_data.get("emri", "").strip()) < 3:
            errors["emri"] = "Shkruani emrin dhe mbiemrin (min. 3 shkronja)."
        if not re.fullmatch(r"[+0-9\s]{8,20}", form_data.get("telefoni", "").strip()):
            errors["telefoni"] = "Numri i telefonit nuk duket i saktë."
        if form_data.get("email") and not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", form_data["email"].strip()):
            errors["email"] = "Email-i nuk duket i saktë."
        if form_data.get("sherbimi") not in dict(Rezervim.SHERBIMI_CHOICES):
            errors["sherbimi"] = "Zgjidhni një shërbim të vlefshëm."

        try:
            selected_date = datetime.strptime(form_data.get("data", ""), "%Y-%m-%d").date()
            if selected_date < date.today():
                errors["data"] = "Data nuk mund të jetë në të shkuarën."
        except ValueError:
            errors["data"] = "Zgjidhni një datë të vlefshme."

        if form_data.get("ora", "") not in dict(Rezervim.ORA_CHOICES):
            errors["ora"] = "Ora e zgjedhur nuk është e vlefshme."

        if not errors:
            Rezervim.objects.create(
                emri=form_data["emri"].strip(),
                telefoni=form_data["telefoni"].strip(),
                email=form_data.get("email", "").strip(),
                sherbimi=form_data["sherbimi"],
                data=selected_date,
                ora=form_data.get("ora", ""),
                mesazhi=form_data.get("mesazhi", "").strip(),
            )
            context.update({"success": True, "form_data": {}})
        else:
            context["errors"] = errors

    return render(request, "kontakt.html", context)

def sherbimet(request):
    sherbimets = Service.objects.all()
    return render(request, "sherbimet.html", {"sherbimets": sherbimets})
