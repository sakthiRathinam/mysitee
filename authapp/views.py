from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import inVoice
from .forms import createForm
from .filters import poFilter
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
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