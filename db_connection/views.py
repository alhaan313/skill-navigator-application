from django.shortcuts import render, redirect
from .forms import PersonForm

def person_create_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = PersonForm()
    
    return render(request, 'db_connection\index.html', {'form': form})

def success_view(request):
    return render(request, 'db_connection\success.html')
