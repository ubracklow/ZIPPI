from django.shortcuts import render, get_object_or_404
from .models import Pin
from .forms import PinForm

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


