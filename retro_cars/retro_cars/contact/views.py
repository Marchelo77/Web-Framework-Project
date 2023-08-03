from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def contact_page(request):
    user = request.user
    user_full_name = f'{user.first_name} {user.last_name}'
    user_email = user.email

    if user.first_name is None and user.last_name is None:
        user_full_name = user.username
    elif user.first_name is None:
        user_full_name = user.last_name
    elif user.last_name is None:
        user_full_name = user.first_name

    context = {
        'user_full_name': user_full_name,
        'user_email': user_email,
    }
    return render(request, 'contacts/contact.html', context)
