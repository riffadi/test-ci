"""
	Template sebagai controller bersalam denan urls.py sebagai pengatur alur data
"""

from django.shortcuts import render, redirect
from .models import Misi, Tujuan, Sasaran, Indikator
from .forms import MisiForm, TujuanForm, SasaranForm, IndikatorForm

# Create your views here.
def misi(request):
	misi_form = MisiForm(request.POST or None)

	if request.method == 'POST':
		if misi_form.is_valid():
			misi_form.save()
		return redirect('indikator:list')

	context = {
		'page_title' : 'Tambah Misi',
		'misi_form' : misi_form,
	}

	return render(request, 'indikator/create.html', context)

def tujuan(request):
	tujuan_form = TujuanForm(request.POST or None)

	if request.method == 'POST':
		if tujuan_form.is_valid():
			tujuan_form.save()
		return redirect('indikator:list')

	context = {
		'page_title' : 'Tambah Tujuan',
		'misi_form' : tujuan_form,
	}

	return render(request, 'indikator/create.html', context)

def sasaran(request):
	sasaran_form = MisiForm(request.POST or None)

	if request.method == 'POST':
		if sasaran_form.is_valid():
			sasaran_form.save()
		return redirect('indikator:list')

	context = {
		'page_title' : 'Tambah Sasaran',
		'sasaran_form' : sasaran_form,
	}

	return render(request, 'indikator/create.html', context)

def indikator(request):
	indikator_form = IndikatorForm(request.POST or None)

	if request.method == 'POST':
		if indikator_form.is_valid():
			indikator_form.save()
		return redirect('indikator:list')

	context = {
		'page_title' : 'Tambah Indikator',
		'misi_form' : indikator_form,
	}

	return render(request, 'indikator/create.html', context)

def list(request):
	misi = Misi.objects.all()
	tujuan = Tujuan.objects.all()
	sasaran = Sasaran.objects.all()
	indikator = Indikator.objects.all()

	context = {
		'page_title' : 'Indikator Kinerja Utama',
		'misi' : misi,
		'tujuan' : tujuan,
		'sasaran': sasaran,
		'indikator' : indikator,
	}
	return render(request, 'index.html', context)