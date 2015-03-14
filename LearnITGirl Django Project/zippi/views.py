from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Pin, UserProfile, Map
from .forms import PinForm, UserForm, UserProfileForm, PinSearchForm, MapCenterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from geopy.geocoders import Nominatim


#auth.user functions

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
                    picture_user = UserProfile.objects.filter(user=request.user)
                    picture = picture_user[0].picture
                    return render(request, 'zippi/zippi_home.html',{'picture': picture})
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
    return render(request, 'zippi/zippi_start.html')

def zippi_start(request):
     return render(request, 'zippi/zippi_start.html')

def zippi_home(request):
     return render(request, 'zippi/zippi_home.html')

## MAPS
    
def show_map(request, pk):
    new_map = get_object_or_404(Map, pk=pk)
    return render(request,'zippi/show_map.html', {'long' : new_map.long, 'lat' : new_map.lat })     

## set map center: user input is calculated into coordinates and saved in map db model

def map_center(request):
    if request.method == 'POST':
        form = MapCenterForm(request.POST)
        if form.is_valid():
            new_map = form.save(commit=False)
            new_map.author = request.user
            geolocator = Nominatim()
            location = geolocator.geocode(str(request.POST['country']))
            new_map.map_long = location.longitude
            new_map.map_lat = location.latitude
            new_map.save()
            return render (request, 'zippi/show_map.html', {'map_long' : new_map.map_long, 'map_lat' : new_map.map_lat, 'map_id' : new_map.pk, })
                  
        else:
            form = MapCenterForm()
            return render(request, 'zippi/map_center.html', {'form': form})
    else:
        form = MapCenterForm()
        return render(request, 'zippi/map_center.html', {'form': form})

## PINS

def pin_list(request):
    pins= Pin.objects.filter(author=request.user)
    pins = Pin.objects.order_by('category')
    return render(request, 'zippi/pin_list.html', {'pins': pins})


def pin_search(request, map_id):
    ## search field to take user input for pin location and transfer into geocode lat and long
    if request.method == 'POST':
        form = PinSearchForm(request.POST)
        if form.is_valid():
            map_id = Map.objects.filter(pk=map_id)
            geolocator = Nominatim()
            location = geolocator.geocode(str(request.POST['address']))
            pin_long = location.longitude
            pin_lat = location.latitude
            return redirect (request, 'zippi.views.pin_new', pin_lat, pin_long, map_id)
        else:
            form = PinSearchForm()
            return render(request, 'zippi/pin_search.html', {'form': form})
    else:
          form = PinSearchForm()
    return render(request, 'zippi/pin_search.html', {'form': form})


def pin_new(request, map_id, pin_lat, pin_long):
    ## takes pin_search lat and long and prompts remaining user input to fill Pin model and save in DB
    if request.method == "POST":
        form = PinForm(request.POST)
        if form.is_valid():
            pin = form.save(commit=False)
            pin.author = request.user
            map_id = Map.objects.filter(pk=map_id)
            pin.map_title = map_id[0]
            pin.pin_lat = pin_lat
            pin.pin_long = pin_long
            pin.save()
            return redirect('zippi.views.pin_detail', pk=pin.pk)
    else:
        form = PinForm()
    return render(request, 'zippi/pin_edit.html', {'form': form})


def pin_detail(request, pk):
    pin = get_object_or_404(Pin, pk=pk)
    return render(request, 'zippi/pin_detail.html', {'pin': pin})

