from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import inVoice
from .forms import createForm
from .filters import poFilter
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import io
from reportlab.lib import colors
from django.template.loader import get_template
from .utils import render_to_pdf
from rest_framework.views import APIView
def home(request):
	count=User.objects.count()
	return render(request,'home.html',{'count':count})
def signup(request):
	if request.method =="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request, 'registration/signup.html',{'form':form})
@login_required
def form(request):
	data=inVoice.objects.all()
	myFilter=poFilter(request.GET,queryset=data)
	data=myFilter.qs
	paginator=Paginator(data,4)
	page=request.GET.get('page')
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		posts=paginator.page(1)
	except EmptyPage:
		posts=paginator.page(paginator.num_pages)

	
	context={'page':page,'posts':posts,'myFilter':myFilter}
	return render(request,'form.html',context)
def createOrder(request):
	form=createForm()
	if request.method=="POST":
		form=createForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('form')

	return render(request,'forms.html',{'form':form})
def updateOrder(request,name):
	data=inVoice.objects.get(name=name)
	form=createForm(instance=data)
	if request.method=="POST":
		form=createForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('form')

	context={'form':form}
	return render(request,'forms.html',context)
def deleteOrder(request,name):
	data=inVoice.objects.get(name=name)
	data.delete()
	return redirect('form')
def excelUpload(request):
	items=inVoice.objects.all()
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment; filename="invoice.csv"'
	writer=csv.writer(response)
	writer.writerow(['PoNumber','Name','PersonName','PhoneNumber','Email','Address','Status'])
	for user in items:
		writer.writerow([user.ponumber,user.name,user.personName,user.phoneNumber,user.email,user.address,user.status])
	return response
def pdfDownload(request):
	items=inVoice.objects.all()
	template=get_template('invoice.html')
	context={'posts':items}
	html=template.render(context)
	pdf=render_to_pdf('invoice.html',context)
	return HttpResponse(pdf,content_type='application/pdf')
	return response