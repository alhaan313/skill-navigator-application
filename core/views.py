from django.shortcuts import render, redirect
from .forms import PersonForm

def person_create_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = PersonForm()
    
    return render(request, 'core\index.html', {'form': form})

def success_view(request):
    return render(request, 'core\success.html')
