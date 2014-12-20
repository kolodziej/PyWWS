from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from newsletter.models import Subscriber
from django.forms import ModelForm
from newsletter.utils import salt
import smtplib
import hashlib

def index(request):
	status = None
	activated = None
	if request.POST:
			sub = Subscriber()
			sub.name = request.POST.get("name")
			sub.email = request.POST.get("email")
			hashdata = sub.name + sub.email + salt(12)
			sub.checksum = hashlib.sha256(hashdata.encode('utf-8')).hexdigest()
			sub.activated = False
			sub.save()
			
			message = render_to_string('activation_mail.html', {
				'subscriber': sub
			})
			
			status = True

			try:
				msg = EmailMessage('Patrycja Mynarska - Newsletter', message, 'list@patrycjamynarska.com', [sub.email], []);
				msg.content_subtype = "html"
				msg.send()
			except smtplib.SMTPException:
				status = False


	return render(request, 'newsletter.html', {
		'status': status,
		'activated': activated,
	})

def activate(request, checksum):
	status = None
	activated = None
	sub = Subscriber.objects.get(checksum=checksum)
	sub.activated = True
	sub.save()
	activated = True
	return render(request, 'newsletter.html', {
		'status': status,
		'activated': activated,
	})
