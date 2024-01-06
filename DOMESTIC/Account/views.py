from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail
from DOMESTIC import settings 
# from .models import UserDetails , Empdetails , Login ,Sigup
from .models import Empdetails ,Signup,Bookings 
from Services.models import Cleaning,Plumbing,Carpenter,Electics
from django.contrib.auth.decorators import login_required
# from allauth.account.models import EmailConfirmation
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .Paytm import CheckSum
from datetime import datetime,timedelta
from .encrypt_util import *
from django.utils import timezone
import random
MERCHANT_KEY = 'kbzk1DSbJiV_03p5'

# Create your views here.
# For Login page.
def view_login(request):
    if request.method=="POST":
        checks=request.POST.get('check')
        username=request.POST['username']
        password=request.POST['password']
        # print(username,password)
        if checks == "ServiceProvider":
            username = "EMP_"+username
        # query_emp=Empdetails.objects.filter(fname__startswith='EMP_')
        user=authenticate(request,username=username,password=password)
        error = None
        if checks =="ServiceProvider" and user is not None:
            login(request,user)
            # print(username,password+"employee login")
            request.session['username'] = username
            return redirect('emp')
        elif user is not None:
            login(request,user)
            # print(username,password+"user log in")
            request.session['username'] = username
            return redirect("/")
        else:
            error="Username or Password is incorrect!! Please try again."
            if checks =="ServiceProvider":
                username=username[4:]
            param={'error':error,'uname':username}
            return render(request, 'login.html',param)
    return render(request, 'login.html')
        
        
# Logout logic.
def logout_view(request):
    logout(request)
    # print("logout")
    return redirect("/login") 
    # return render(request, 'logout.html')

# profile and update profile logic.
def profile(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        mobile = request.POST.get('phone')
        address = request.POST.get('address')
        user = Signup.objects.get(username=request.user)
        user.fname=fname
        user.phone=mobile
        user.address=address
        user.save()
        return redirect('/profile')
    info=Signup.objects.get(username=request.user)
    return render(request, 'profile.html',{'info':info})

# display customer booking page logic.
def bookings(request):
    user = request.user;    
    bookings = Bookings.objects.all().filter(User=user)
    bidlist=[]
    bookinglist=[]
    ass_emp=[]
    count=0
    emp_send=[]
    for booking in bookings:
        count=count+1
        bid = booking.BookingId
        bidlist.append(bid)
        sercat = booking.category
        sercat1 = sercat.split(',')
        serno = booking.sno
        serno1 = serno.split(':')
        ass_emps = booking.Employee
        emp_list = ass_emps.split(',')
        ser_list =[]
        emp_objects=[]

        #for display employees for every booking.
        for emp in emp_list:
            if emp!="":
                emp_obj = Empdetails.objects.get(username=emp)
                emp_objects.append(emp_obj)
        emp_send.append(emp_objects) 
        #for displaying service details for every booking
        for i,cat in enumerate(sercat1):
            if cat[:8]=="Cleaning":
                sno=serno1[i]
                ser = Cleaning.objects.get(sno=sno)
                ser_list.append(ser)

            if cat[:8]=="Plumbing":
                sno=serno1[i]
                ser = Plumbing.objects.get(sno=sno)
                ser_list.append(ser) 
                
            if cat[:9]=="Electrics":
                sno=serno1[i]
                ser = Electics.objects.get(sno=sno)
                ser_list.append(ser)

            if cat[:9]=="Carpenter":
                sno=serno1[i]
                ser = Carpenter.objects.get(sno=sno)
                ser_list.append(ser)
        bookinglist.append(ser_list)

    param={'bookingserlist':bookinglist,'ass_emp':emp_send,'bookings':bookings}
    return render(request, 'bookings.html',param)

# Sign-up page for user.
def sign_up(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        hno = request.POST.get('houseno')
        area = request.POST.get('area')
        zipn = request.POST.get('zipn')
        city = request.POST.get('city')
        address = hno+' ,'+area+' ,'+' zip-'+zipn
        email=request.POST.get('email')
        password=request.POST.get('password')
        repass = request.POST.get('re-password')
        value={'uname':username, 'fname':fname, 'lname':lname, 'phone':phone, 'email':email, 'hno':hno, 'area':area, 'zipn':zipn, 'city':city } #for holding values.
        # print(username,password,email)
        data=Signup(username=username,email=email,password=password,fname=fname,lname=lname,phone=phone,address=address,city=city)
        error_msg = None
        if Signup.objects.filter(email = email):
            error_msg="Email is already registered."
        elif password != repass:
            error_msg = "Both Password field should be same."
        elif Signup.objects.filter(username = username):
            error_msg="This User Name is already taken from another user. Please choose another."
        else:
            # print('Original Password:', request.POST['password'])
            encryptpass= encrypt(request.POST['password'])
            # print('Encrypt Password:',encryptpass)
            decryptpass= decrypt(encryptpass)
            # print('Decrypt Password:',decryptpass)
            data.save()
            subject = 'Welcome to DOMESTICO.com '
            message = f'Hi {username}, Thanks for regestering in DOMESTICO.com \n'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            myuser=User.objects.create_user(username=username,email=email,password=password)
            myuser.save()
            # print(username,password,email)
            value={}
            return redirect('login')
    else:
        return render(request,'sign_up.html')
    param={
        'error':error_msg,
        'values':value
    }
    return render(request, 'sign_up.html',param)

# sign-up page for employee.
def signupemp(request):
    if request.method=="POST":
        username = request.POST.get('username')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        hno = request.POST.get('houseno')
        work=request.POST.get('profession')
        area = request.POST.get('area')
        city = request.POST.get('city')
        address = hno+' ,'+area+' ,'+city
        password = request.POST.get('password')
        repass = request.POST.get('re-password')
        dob=request.POST.get('dob')
        username="EMP_"+username
        value={ 'fname':fname, 'lname':lname, 'phone':phone, 'email':email, 'hno':hno, 'area':area, 'dob':dob} #for holding values.
        data = Empdetails(username=username,fname=fname,lname=lname,phone=phone,email=email,address=address,password=password,work=work,dob=dob)
        error_msg = None
        if Empdetails.objects.filter(email = email):
            error_msg="Email is already registered."
        elif password != repass:
            error_msg = "Both Password field should be same."
        elif Empdetails.objects.filter(username = username):
            error_msg="This User Name is already taken from another Employee. Please choose another."
        else:
            # print('Original Password:', request.POST['password'])
            encryptpass= encrypt(request.POST['password'])
            # print('Encrypt Password:',encryptpass)
            decryptpass= decrypt(encryptpass)
            # print('Decrypt Password:',decryptpass)
            data.save()
            subject = 'Welcome to DOMESTICO.com '
            message = f'Hi {username}, Thanks for regestering for employee in DOMESTICO.com \n'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            myuser=User.objects.create_user(username=username,email=email,password=password,is_staff=True)
            myuser.save()
            # print(myuser)
            value={}
            return redirect('login')
    else:
        return render(request,'signup-emp.html')
    param={
        'error':error_msg,
        'values':value
    }
    return render(request, 'signup-emp.html',param)

# Showing Cart page logic.
def cart(request):
    try:
        services = list(request.session.get('cart').keys())
        serdic=[]
        cnt=0
        for ser in services:
            if ser[:8] == "Cleaning":
                sno = int(ser[9:])
                service = Cleaning.objects.filter(sno=sno)
                serdic.append(service)

            if ser[:8] == "Plumbing":
                sno = int(ser[9:])
                service = Plumbing.objects.filter(sno=sno)
                serdic.append(service)

            if ser[:9] == "Carpenter":
                sno = int(ser[10:])
                service = Carpenter.objects.filter(sno=sno)
                serdic.append(service)
                
            if ser[:9] == "Electrics":
                sno = int(ser[10:])
                service = Electics.objects.filter(sno=sno)
                serdic.append(service)
        param = {'serdic':serdic,'counter':len(serdic)}
        return render(request, 'cart.html',param)
    except:
        return render(request, 'cart.html')

# page for getting user detail at checkout page.   
def bookingform(request):
    if request.user:
        try:
            info=Signup.objects.all().get(username=request.user)
            if request.method=="POST":
                booking = Bookings.objects.get(BookingId=request.POST.get('bid'))
                data_dict={
                'MID': 'VMLskh33374131769871',
                'ORDER_ID': str(booking.BookingId),
                'TXN_AMOUNT': str(booking.price),
                'CUST_ID': booking.User,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/account/handlereq/',
                }
                data_dict['CHECKSUMHASH'] = CheckSum.generate_checksum(data_dict,MERCHANT_KEY)
                return render(request,'paytm.html',{'data_dict':data_dict})
            price = request.GET.get('gprice');
            if request.session.get('cart'):
                return  render(request, 'bookingform.html',{'info':info,'price':price})
            else:
                return redirect('/cart')
        except:
            return HttpResponse("Not login!!Login first.")
    
# paytm request handle here.
@csrf_exempt
def handlereq(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = CheckSum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('Booking successful')
        else:
            print('Booking was not successful because' + response_dict['RESPMSG'])
    return render(request, 'payment_status.html', {'response': response_dict})
    
# logic for book the service.
def makeBooking(request):  
    if request.user in User.objects.all():
        luser = request.user;
        cart = request.session.get('cart').keys();
        all_ser={}
        all_emp=[]
        empdes=[]
        for ser in cart:
            if len(ser)<=10:
                category = ser[:8]
                sno = ser[9:]
                if category == "Cleaning":
                    allemp=Empdetails.objects.filter(work="Cleaning").all()
                    emp=random.choice(allemp)
                    if emp.username not in empdes:
                        empdes.append(emp.username)
                if category == "Plumbing":
                    allemp=Empdetails.objects.filter(work="Plumber").all()
                    emp=random.choice(allemp)
                    if emp.username not in empdes:
                        empdes.append(emp.username)
            else:
                category = ser[:9]
                sno = ser[10:]
                if category == "Electrics":
                    allemp=Empdetails.objects.filter(work="Electrician").all()
                    emp=random.choice(allemp)
                    if emp.username not in empdes:
                        empdes.append(emp.username)
                if category == "Carpenter":
                    allemp=Empdetails.objects.filter(work="Carpenter").all()
                    emp=random.choice(allemp)
                    if emp.username not in empdes:
                        empdes.append(emp.username)
            all_ser[category+sno] = sno 
        # print(empdes)
        cat = all_ser.keys()
        store_ser=""
        store_sno=""
        store_emp=""
        for key in cat:
            store_ser = store_ser + key + ","
        # print(store_ser)
        sn = all_ser.values()
        for value in sn:
            store_sno = store_sno + value + ":"
        # print(store_sno)
        for emp in empdes:
            store_emp = store_emp+emp+","
        price = request.POST.get('price')
        serdate = request.POST.get('serdate')    #yyyy-mm-dd formate
        slote = request.POST.get('slote')
        name = request.POST.get('fname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        otp = random.randint(1000,9999)
        booking = Bookings(User=luser,Employee=store_emp,category=store_ser,sno=store_sno,price=price,service_date=serdate,slote=slote,name=name,address=address,phone=phone,otp=otp)
        booking.save()   
        cart = request.session.get('cart')
        cart={}
        request.session['cart']=cart
    return redirect('/bookings')

# logic for cancelation of service.
def cancelBooking(request):
    if request.method=='POST':
        bid=request.POST.get('book_id')
        booking = Bookings.objects.get(BookingId=bid)
        sdate = booking.service_date
        sslote = booking.slote
        booking_datetime_str = f"{sdate} {sslote}"
        booking_datetime = datetime.strptime(booking_datetime_str, "%Y-%m-%d %I:%M %p")
        time_diff = booking_datetime - datetime.now()
        if time_diff >= timedelta(hours=24):
            booking.cancel_booking=True
            booking.save()
            request.session['is_cancelled']=True
        else:
            request.session['is_cancelled']=False
        return redirect('/bookings')

# home/assigned work page for the employee.
@login_required(login_url='login')
def emp(request):
    bookings = Bookings.objects.all()
    booking_object=[]
    customer_object =[]
    service=[]
    bookinglist=[]
    for booking in bookings:
        all_emp = booking.Employee 
        all_emp_list = all_emp.split(",")
        for emp in all_emp_list:
            if emp != "":
                # print(emp)
                # print(str(request.user))
                if emp == str(request.user):
                    # print(booking)
                    booking_object.append(booking)
                    cus = Signup.objects.get(username=booking.User.username)
                    if cus not in customer_object:
                        customer_object.append(cus)
                    # print(booking.category)
                    # print(booking.sno)
                    temp1 = booking.category.split(',')
                    temp2 = booking.sno.split(':')
                    ser_list=[]
                    for i,cat in enumerate(temp1):
                        if cat[:8]=="Cleaning":
                            sno=temp2[i]
                            ser = Cleaning.objects.get(sno=sno)
                            empdtls = Empdetails.objects.get(username=request.user)
                            if empdtls.work == "Cleaning":
                                ser_list.append(ser)
                        if cat[:8]=="Plumbing":
                            sno=temp2[i]
                            ser = Plumbing.objects.get(sno=sno)
                            empdtls = Empdetails.objects.get(username=request.user)
                            if empdtls.work == "Plumber":
                                ser_list.append(ser)
                            
                        if cat[:9]=="Electrics":
                            sno=temp2[i]
                            ser = Electics.objects.get(sno=sno)
                            empdtls = Empdetails.objects.get(username=request.user)
                            if empdtls.work == "Electrician":
                                ser_list.append(ser)

                        if cat[:9]=="Carpenter":
                            sno=temp2[i]
                            ser = Carpenter.objects.get(sno=sno)
                            empdtls = Empdetails.objects.get(username=request.user)
                            if empdtls.work == "Carpenter":
                                ser_list.append(ser)
                    bookinglist.append(ser_list)           
                            
    param = {'bookings':booking_object,"Customer":customer_object,"service":bookinglist}
    return render(request,'emp.html',param)

# profile page for employee.
def emp_profile(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        mobile = request.POST.get('phone')
        address = request.POST.get('address')
        emp = Empdetails.objects.get(username=request.user)
        emp.fname=fname
        emp.phone=mobile
        emp.address=address
        emp.save()
        return redirect('/emp_profile')
    info=Empdetails.objects.get(username=request.user)
    return render(request, 'emp_profile.html',{'info':info})

# logic for completed service by employee.
def complete_booking(request):
    if request.method == "POST":
        bid = request.POST.get('book_id')
        otp = request.POST.get('otp')
        booking = Bookings.objects.get(BookingId=bid)
        cotp = booking.otp
        if str(cotp) == otp:
            booking.complete_status=True
            booking.save()
            request.session['is_completed']=True
        else:
            request.session['is_completed']=False
    return redirect('/emp')
    