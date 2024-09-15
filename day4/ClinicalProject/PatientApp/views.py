from django.shortcuts import render, redirect
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})
def patient_create(request):
    if request.method == 'POST':
        Patient.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            disease=request.POST['disease']
        )
        return redirect('patient_list')
    return render(request, 'patient_form.html')
def patient_update(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        patient.disease = request.POST['disease']
        patient.save()
        return redirect('patient_list')
    return render(request, 'patient_form.html', {'patient': patient})
def patient_delete(request, id):
    Patient.objects.get(id=id).delete()
    return redirect('patient_list')
