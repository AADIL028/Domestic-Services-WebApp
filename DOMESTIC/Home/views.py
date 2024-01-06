from django.shortcuts import render,HttpResponse
from .models import contactMe
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from Account.models import Signup
from django.utils.timezone import timezone

# Create your views here.

# For Home page.
def home(request):
    request.session.set_expiry(1800)    #session expire after 30 min.
    return  render(request, 'index.html')

# For About-us page.
def aboutus(request):
    return  render(request, 'aboutus.html')

# For Contact-us page.
def contactus(request):
    if request.method=='POST':
        success = None
        uname=request.POST['uname']
        email=request.POST['email']
        text=request.POST['text']
        ins=contactMe(uname=uname,email=email,text=text)
        ins.save()
        recipient_list = [email]
        html_content=render_to_string('thankyou.html',{'uname':uname})
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
            "Thanks for contact us",
            text_content,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        success="success"
    else:
        return  render(request, 'contactus.html')
    return  render(request, 'contactus.html',{'sent_msg':success})
