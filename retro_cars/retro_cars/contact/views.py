from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render

from retro_cars.contact.forms import ContactForm


@login_required
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        text = [
            f'Hello {request.user.username}',
            'Thank you for contacting us.',
            'We have received your message and will get back to you soon.',
        ]
        if form.is_valid():
            send_mail(
                subject='Hello',
                message='\n'.join(text),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=(request.user.email,),
            )
            return render(request, 'contacts/contacted.html')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contacts/contact.html', context)


def contacted_page(request):
    return render(request, 'contacts/contacted.html')

