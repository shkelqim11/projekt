
# Create your models here.
from django.db import models


class Rezervim(models.Model):
    SHERBIMI_CHOICES = [
        ("kontroll", "Kontroll & Higjienizim"),
        ("zbardhim", "Zbardhim Dentar"),
        ("implant", "Implantologji"),
        ("ortodonci", "Ortodonci"),
        ("femije", "Stomatologji Fëmijësh"),
        ("tjeter", "Tjetër"),
    ]

    ORA_CHOICES = [
        ("", "Nuk kam preferencë"),
        ("mengjes", "09:00 – 12:00"),
        ("dite", "12:00 – 16:00"),
        ("pasdite", "16:00 – 19:00"),
    ]

    STATUS_CHOICES = [
        ("e_re", "E re"),
        ("konfirmuar", "Konfirmuar"),
        ("anulluar", "Anulluar"),
        ("perfunduar", "Përfunduar"),
    ]

    emri = models.CharField(max_length=120)
    telefoni = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    sherbimi = models.CharField(max_length=20, choices=SHERBIMI_CHOICES)
    data = models.DateField()
    ora = models.CharField(max_length=20, choices=ORA_CHOICES, blank=True)
    mesazhi = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="e_re")
    krijuar_me = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-krijuar_me"]

    def __str__(self):
        return f"{self.emri} — {self.data} ({self.get_sherbimi_display()})"
    
    

class Service(models.Model):
    service_slug = models.SlugField(unique=True, null=True, blank=True)
    service_name = models.CharField(max_length=200, null=True, blank=True)
    service_description = models.TextField(null=True, blank=True)
    service_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    service_svg = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.service_name