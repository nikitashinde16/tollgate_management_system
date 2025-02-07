from django.shortcuts import render
from system.models import*
def register(request):
	msg=""
	if request.method=="POST":
		d=StudentDetails()
		d.fullname=request.POST["fullname"]
		d.contactnumber=request.POST["contactnumber"]
		d.address=request.POST["address"]
		d.gender=request.POST["gender"]
		d.dateofbirth=request.POST["dateofbirth"]
		d.qualification=request.POST["qualification"]
		d.username=request.POST["username"]
		d.password=request.POST["password"]
		d.save()
		msg="Registered Successfully"
	return render(request,"register.html",{"msg":msg})
	
def studentdata(request):
	msg=""
	if request.method=="POST":
		sid=request.POST["sid"]
		StudentDetails.objects.filter(id=sid).delete()
		msg="Record deleted Successfully"
	data=StudentDetails.objects.all()
	return render(request,"studentdata.html",{"data":data,"msg":msg})
def searchperson(request):
	data=""
	msg=""
	if request.method=="POST":
		Searchby=int(request.POST["Searchby"])
		value=request.POST["value"]
		if Searchby==1:
			data=StudentDetails.objects.filter(fullname__contains=value)
		elif Searchby==2:
			data=StudentDetails.objects.filter(contactnumber__contains=value)
		elif Searchby==3:
			data=StudentDetails.objects.filter(username__contains=value)
			if data.exists():
				pass;
			else:
				msg="User Not Found"	
	return render(request,"searchperson.html",{"data":data,"msg":msg})
def login(request):
	msg=""
	if request.method=="POST":
		p_username=request.POST["username"]
		p_password=request.POST["password"]
		if StudentDetails.objects.filter(username=p_username,password=p_password):
			request.session["username"]=p_username
			request.session["password"]=p_password
			return render(request,"home.html")
		else:
			msg="invalid login details"
	return render(request,"login.html",{"msg":msg})
def home(request):
	return render(request,"home.html")
def changepassword(request):
	msg=""
	p_username=""
	if request.method=="POST":
		currentpassword=request.POST["currentpassword"]
		newpassword=request.POST["newpassword"]
		confirmnewpassword=request.POST["confirmnewpassword"]
		request.session["username"]=p_username
		if newpassword==confirmnewpassword:
			if StudentDetails.objects.filter(username=p_username,password=currentpassword).exists():
				StudentDetails.objects.filter(username=p_username,password=currentpassword).update(password=newpassword)
				msg="password changed Successfully"
			else:
				msg="password changed Successfully"
		else:
			msg="New Password & confirmnewpassword must match"
	return render(request,"changepassword.html",{"msg":msg})
def ticketbook(request):
	msg=""
	if request.method=="POST":
		d=tolldetails()
		d.state=request.POST["state"]
		d.nhnumber=request.POST["nhnumber"]
		d.vehicletype=request.POST["vehicletype"]
		d.vehiclenumber=request.POST["vehiclenumber"]
		d.selectplan=request.POST["selectplan"]
		d.contactnumber=request.POST["contactnumber"]
		d.save()
		msg="Vehicle Entry Submitted Successfully"
	return render(request,"ticketbook.html",{"msg":msg})

def tollnumber(request):
	msg=""
	if request.method=="POST":
		d=tolldetails()
		d.tollnumber=request.POST["tollnumber"]
		d.startpoint=request.POST["startpoint"]
		d.endpoint=request.POST["endpoint"]
		d.tickettype=request.POST["tickettype"]
		d.cost=request.POST["cost"]
		d.save()
		msg="Ticket Saved Successfully"
	return render(request,"tollnumber.html",{"msg":msg})
def tolldata(request):
	msg=""
	if request.method=="POST":
		sid=request.POST["sid"]
		tolldetails.objects.filter(id=sid).delete()
		msg="Record deleted Successfully"
	data=tolldetails.objects.all()
	return render(request,"tolldata.html",{"data":data,"msg":msg})
def home(request):
	return render(request,"home.html")

def pay(request):
	msg=""
	if request.method=="POST":
		d=paydetails()
		d.cardaccepted=request.POST["cardaccepted"]
		d.nameoncard=request.POST["nameoncard"]
		d.cardnumber=request.POST["cardnumber"]
		d.amount=request.POST["amount"]
		d.save()
		msg="Transaction Completed Successfully"
	return render(request,"pay.html",{"msg":msg})
def paydata(request):
	msg=""
	if request.method=="POST":
		sid=request.POST["sid"]
		paydetails.objects.filter(id=sid).delete()
		msg="Record deleted Successfully"
	data=paydetails.objects.all()
	return render(request,"paydata.html",{"data":data,"msg":msg})



# Create your views here.
