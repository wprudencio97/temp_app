from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        temp = request.POST['temp']
        convert_to = request.POST['convert_to']

        context = {
            'temp': temp,
            'convert_to': convert_to
        }

        if convert_to == 'celsius':
            celsius_temp = round((float(temp) - 32) * 5/9, 2)
            messages.success(request,(f'{temp} fahrenheit is {celsius_temp} celsius.'))

            return render(request, 'converter/home.html', context)

        elif convert_to == 'fahrenheit':
            fahrenheit_temp = round((float(temp) * 9/5) + 32, 2)
            messages.success(request,(f'{temp} celsius is {fahrenheit_temp} fahrenheit.'))
            
            return render(request, 'converter/home.html', context)
        else:
            messages.warning(request,('Select a temperature option.'))
            return redirect('home')

    else:
        context = {
            'convert_to': ''
        }
        return render(request, 'converter/home.html', context)