from django.contrib import admin

# Register your models here.
from .models import Misi, Tujuan, Sasaran, Indikator, KondisiAwal, KondisiAkhir

admin.site.register(Misi)
admin.site.register(Tujuan)
admin.site.register(Sasaran)
admin.site.register(Indikator)
admin.site.register(KondisiAwal)
admin.site.register(KondisiAkhir)
