from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.
def send_mail_page(request):
    context = {}
    if request.method == 'POST':
        address = request.POST.get('address')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        attachment = request.FILES.get('attachment')    
        if address and message and subject:
            try:
                email=EmailMessage(subject, message, settings.EMAIL_HOST_USER, [address])
                if attachment:
                    email.attach(attachment.name, attachment.read(), attachment.content_type)
                    print(f'Attachment name: {attachment.name}')
                    print(f'Attachment content type: {attachment.content_type}')
                email.send()
                context['email_sent'] = True
                context['result'] = 'Email sent successfully.'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'Please fill all the fields.'
    return render(request, 'user/home.html', context)