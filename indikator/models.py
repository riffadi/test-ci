"""
	Kode untuk membuar model database
"""
from django.db import models

# Create your models here.
class Misi(models.Model):
	misi = models.CharField(max_length=255)

	def __str__(self):
		return self.misi

class Tujuan(models.Model):
	tujuan = models.CharField(max_length=255)

	def __str__(self):
		return self.tujuan

class Sasaran(models.Model):
	sasaran = models.CharField(max_length=100)
	
	def __str__(self):
		return self.sasaran

class Indikator(models.Model):
	indikator = models.CharField(max_length=100)

	def __str__(self):
		return self.indikator

class KondisiAwal(models.Model):
	kondisi_awal = models.CharField(max_length=100)

	def __str__(self):
		return self.kondisi_awal

class KondisiAkhir(models.Model):
	kondisi_akhir = models.CharField(max_length=100)

	def __str__(self):
		return self.kondisi_akhir
