from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Pin
from .forms import PinForm, UserForm, UserProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def zippi_home(request):
     context_dict = {'boldmessage': "I am bold font from the context"}
     return render(request, 'zippi/zippi_home.html', context_dict)

def pin_list(request):
    pins = Pin.objects.order_by('category')
    return render(request, 'zippi/pin_list.html', {'pins': pins})

def pin_detail(request, pk):
    pin = get_object_or_404(Pin, pk=pk)
    return render(request, 'zippi/pin_detail.html', {'pin': pin})

def pin_new(request):
    if request.method == "POST":
        form = PinForm(request.POST)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.author = request.user
            pin.save()
            return redirect('zippi.views.pin_detail', pk=pin.pk)
    else:
        form = PinForm()
    return render(request, 'zippi/pin_edit.html', {'form': form})


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
        'zippi/register.html',
        {'user_form' : user_form, 'profile_form' : profile_form, 'registered' : registered})

def user_login(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']

          user = authenticate(username=username, password=password)

          if user:
               if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('')
               else:
                    return HttpResponse('Your Zippi account is disabled.')
          else:
               print('Invalid login details: {0}, {1}'.format(username, password))
               return HttpResponse('Invalid login details supplied.')
     else:
          return render(request, 'zippi/login.html',{})
                     
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('')


          
     














     
