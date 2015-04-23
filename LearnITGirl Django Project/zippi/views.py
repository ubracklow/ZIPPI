from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Pin, UserProfile, Map
from .forms import NewPinForm, UserForm, UserProfileForm, MapCenterForm, EditPinForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from geopy.geocoders import Nominatim
from geopy.exc import GeopyError, ConfigurationError, GeocoderServiceError, GeocoderQueryError, GeocoderQuotaExceeded, GeocoderAuthenticationFailure, GeocoderInsufficientPrivileges, GeocoderTimedOut, GeocoderUnavailable, GeocoderParseError, GeocoderNotFound 
from django.contrib import messages

def zippi_start(request):
     return render(request, 'zippi/zippi_start.html')

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


def edit_profile(request):
    registered = True

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


def delete_profile(request):
    request.user.delete()
    messages.success(request, 'Your Zippi Profile has been deleted.')
    return redirect ('zippi_start')


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

def zippi_home(request):
     picture_user = UserProfile.objects.filter(user=request.user)
     picture = picture_user[0].picture     
     return render(request, 'zippi/zippi_home.html', {'picture':picture})

## MAPS

def new_map(request):
     ''' take userinput, geocode into coordinates and use as centerpoint for a map '''
     if request.method == 'POST':
          form = MapCenterForm(request.POST)
          if form.is_valid():
               new_map = form.save(commit=False)
               new_map.user = request.user
               geolocator = Nominatim()
               try:
                    location = geolocator.geocode(str(request.POST['country']), timeout=10)
                    new_map.map_long = location.longitude
                    new_map.map_lat = location.latitude
                    new_map.save()
                    messages.success(request, 'New Map saved. You can now start setting pins on it.')
                    return render (request, 'zippi/empty_map.html', {'map_long' : new_map.map_long, 'map_lat' : new_map.map_lat, 'map_title':new_map.map_title, 'map_id' : new_map.id })
               except: 
                    messages.error(request, 'Something went wrong. Please try again.')
                    form = MapCenterForm()
                    return render(request, 'zippi/new_map.html', {'form': form})
          else:
               form = MapCenterForm()
               return render(request, 'zippi/new_map.html', {'form': form})
     else:
          form = MapCenterForm()
          return render(request, 'zippi/new_map.html', {'form': form})

def map_list(request):
    ''' lists all maps for user '''
    maps = Map.objects.filter(user=request.user)
    return render(request, 'zippi/map_list.html', {'maps': maps})

def my_map(request, pk):
    ''' displays map with all associated pins '''
    my_map = get_object_or_404(Map, pk=pk)
    pins = Pin.objects.filter(related_map=my_map)
    return render(request, 'zippi/my_map.html', {'map_long' : my_map.map_long, 'map_lat' : my_map.map_lat, 'pins' : pins, 'map_id' : my_map.id, 'map_title' : my_map.map_title})

def delete_map(request, pk):
    my_map = get_object_or_404(Map, pk=pk)
    my_map.delete()
    messages.success(request, 'The Map has been deleted.')
    return redirect ('map_list')


## PINS

def new_pin(request, pk):
     ''' take user input to set new pin on related map '''
     if request.method == 'POST':
          form = NewPinForm(request.POST)
          if form.is_valid():
               pin = form.save(commit=False)
               related_map = Map.objects.filter(pk=pk)
               pin.related_map=related_map[0]
               geolocator = Nominatim()
               try:
                    location = geolocator.geocode(str(request.POST['address']))
                    pin.pin_long = location.longitude
                    pin.pin_lat = location.latitude
                    pin.pin_address = location.address
                    pin.save()
                    return redirect ('zippi.views.my_map', pk=pk)
               except:
                    messages.error(request, 'Something went wrong. Please try again.')
                    form = NewPinForm()
                    return render(request, 'zippi/new_pin.html', {'form': form})
          else:
               form = NewPinForm()
               return render(request,'zippi/new_pin.html', {'form': form})
     else:
          form = NewPinForm()
          return render(request,'zippi/new_pin.html', {'form': form})

def pin_list(request, pk):
    ''' show list of all pins of related map '''
    pins = Pin.objects.filter(related_map=pk).order_by('category')
    return render(request, 'zippi/pin_list.html', {'pins': pins})

def pin_detail(request, pk):
    ''' show pin object '''
    pin = get_object_or_404(Pin, pk=pk)
    my_map = pin.related_map
    return render(request, 'zippi/pin_detail.html', {'pin': pin, 'map_id':my_map.pk })

def pin_edit(request, pk):
    ''' edit existing pin object '''
    pin = get_object_or_404(Pin, pk=pk)
    if request.method == 'POST':
        form = EditPinForm(request.POST, instance=pin)
        if form.is_valid():
            pin = form.save(commit=False)
            geolocator = Nominatim()
            location = geolocator.geocode(str(request.POST['pin_address']))
            pin.pin_long = location.longitude
            pin.pin_lat = location.latitude
            pin.pin_address = location.address
            pin.save()
            messages.success(request, 'Information for this Pin was updated.')
            return redirect ('zippi.views.pin_detail', pk=pin.pk)
        else:
            form = EditPinForm(instance=pin)
    else:
        form = EditPinForm(instance=pin)
        return render(request, 'zippi/pin_edit.html', {'form': form})

def pin_delete(request, pk):
    pin = get_object_or_404(Pin, pk=pk)
    my_map = pin.related_map.pk
    pin.delete()
    messages.success(request, 'Pin deleted.')
    return redirect ('/mymap/'+str(my_map))
            
 
