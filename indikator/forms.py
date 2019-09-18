"""
	Berisi kode untuk membuat form
"""
from django import forms
from .models import Misi, Tujuan, Sasaran, Indikator
class MisiForm(forms.ModelForm):
	class Meta:
		model = Misi
		fields = {
			'misi',
		}
class TujuanForm(forms.ModelForm):
	class Meta:
		model = Tujuan
		fields = {
			'tujuan',
		}

class SasaranForm(forms.ModelForm):
	class Meta:
		model = Sasaran
		fields = {
			'sasaran',
		}

class IndikatorForm(forms.ModelForm):
	class Meta:
		model = Indikator
		fields = {
			'indikator',
		}