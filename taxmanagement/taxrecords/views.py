from django.shortcuts import render, redirect
from .models import TaxRecord
from .forms import TaxRecordForm

def home_view(request):
    return render(request, 'taxrecords/home.html')

def create_view(request):
    if request.method == 'POST':
        form = TaxRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaxRecordForm()
    return render(request, 'taxrecords/create.html', {'form': form})

def read_view(request):
    records = TaxRecord.objects.all()
    return render(request, 'taxrecords/read.html', {'records': records})

def update_view(request, pk):
    record = TaxRecord.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaxRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = TaxRecordForm(instance=record)
    return render(request, 'taxrecords/update.html', {'form': form})

def delete_view(request, pk):
    record = TaxRecord.objects.get(pk=pk)
    record.delete()
    return redirect('read')

def bulk_import_view(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        # Import the CSV file and save the records
        # For simplicity, we'll assume the CSV file has the same columns as the model
        records = []
        for row in csv.reader(csv_file):
            record = TaxRecord(**dict(zip(['assessment_year', 'assessment_number', 'door_number', 'owner_name', 'relative_name', 'house_tax', 'library_cess', 'water_tax', 'lightning_tax', 'fire_tax', 'sports_cess', 'drainage_tax', 'total_current_year_tax', 'arrear_tax', 'total_tax', 'cluster_number', 'payment'], row)))
            records.append(record)
        TaxRecord.objects.bulk_create(records)
        return redirect('home')
    return render(request, 'taxrecords/bulk_import.html')