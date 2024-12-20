# optimizer/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .forms import CSVUploadForm

def optimize(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            # Process the CSV file here
            return HttpResponse("CSV uploaded and optimization started.")
    else:
        form = CSVUploadForm()

    return render(request, 'optimizer/optimize.html', {'form': form})

def results(request):
    # Your logic to display results after the optimization
    return render(request, 'optimizer/results.html')
