from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .forms import form_signup, form_login
from django.contrib.auth.models import User
import random
def home_page(request):
    return render(request, 'home_and_login/home_page.html',
                  {'form_signup': form_signup, 'form_login': form_login})

def add_new_user(request):
    if request.method == 'POST':
        form = form_signup(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            username_email = form.cleaned_data['username_email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username_email, username_email, password)
            full_name = full_name.split()
            #get first name or first two if three names
            if len(full_name) == 1:
                user.first_name = full_name[0]
            else:
                user.last_name = full_name[-1]
                user.first_name = " ".join(full_name[:-1])
            one_word_first_name = user.first_name.split(' ')
            #ADD functionality to check if hash is unique
            user_profile_hash = one_word_first_name[0].lower() + str(random.randrange(1000,9999))
            full_name = ' '.join(full_name)
            # user_details_save = user_details.objects.create(
            #     user=user, full_name=full_name, profile_link=user_profile_hash)
            user.save()
    else:
        return JsonResponse({'logged_in': 'No'})
    user = authenticate(username=username_email, password=password)
    login(request, user)
    # return render(request, 'main/welcome_user.html')
    return JsonResponse({'logged_in': 'yes'})