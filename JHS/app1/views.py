from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Contact,Courses,Gallery,Registration,Placements
#sending email
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage
# Create your views here.

def home(request):
    if request.method=='POST':
        reservation_name=request.POST.get('reservation_name')
        reservation_email=request.POST.get('reservation_email')
        reservation_phone=request.POST.get('reservation_phone')
        select_course=request.POST.get('select_course')
        Date=request.POST.get('Date')
        form_message=request.POST.get('form_message')
        query=Registration(reservation_name=reservation_name,reservation_email=reservation_email,select_course=select_course, reservation_phone= reservation_phone,form_message=form_message, Date= Date)
        query.save()

         #email sending starts from here

        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()

        email_message=mail.EmailMessage(f'Email from{reservation_name}',
        f'UserEmail : {reservation_name}\nUserPhoneNumber : { reservation_phone}\n\n\nQUERY : {form_message}',from_email,['madathamani60@gmail.com'],
        connection=connection)

        email_client=mail.EmailMessage('mk2100484 Response',
        f'Thanks for Reaching Us\nmk2100484\n9912791510\mk2100484@gmail.com',from_email,[ reservation_email],
        connection=connection)


        connection.send_messages([email_message, email_client])
        connection.close()


        messages.info(request,"Thanks for Registration We will get back soon...")
        return redirect('/')
        
    allPosts=Gallery.objects.all()
    print(allPosts)
    context={'allPosts':allPosts}
    return render(request,"home.html",context)


def about(request):
    return render(request,"app1/about.html")

def courses(request):
    allPosts=Courses.objects.all()
    print(allPosts)
    context={'allPosts':allPosts}

    return render(request,"app1/courses.html",context)

def placements(request):
    videos=Placements.objects.all()
    print(videos)
    context={'videos':videos}
    return render(request,"app1/placements.html",context)

def contact(request):
   
    if request.method=='POST':
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        phone=request.POST.get("phoneNumber")
        fsubject=request.POST.get("subject")
        fmessage=request.POST.get("message")
        query=Contact(name=fname,email=femail,phoneNumber=phone,subject=fsubject,message=fmessage)
        query.save()

        #email sending starts from here

        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()

        email_message=mail.EmailMessage(f'Email from{fname}',
        f'UserEmail : {femail}\nUserPhoneNumber : {phone}\nUserSubject : {fsubject}\n\n\nQUERY : {fmessage}',from_email,['madathamani60@gmail.com'],
        connection=connection)

        email_client=mail.EmailMessage('mk2100484 Response',
        f'Thanks for Reaching Us\nmk2100484\n9912791510\mk2100484@gmail.com',from_email,[femail],
        connection=connection)


        connection.send_messages([email_message, email_client])
        connection.close()



        messages.info(request,"Thanks for Reaching Us We will get back soon...")
        return redirect('/contact')
    return render(request,"contact.html")

def signup(request):
    if request.method=='POST':
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number is Invalid")
            return redirect('/signup')
        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.info(request,"Phone Number is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"email is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()


        messages.info(request,"User is created Please Login")
        return redirect('/login')
    return render(request,'signup.html')

def handlelogin(request):
    if request.method=='POST':
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Successfully')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')
    return render(request,'handlelogin.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('/login')


