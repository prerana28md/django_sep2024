from django.shortcuts import render, redirect
from .models import Doctor

# List all doctors
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

# Create a new doctor
def doctor_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        specialization = request.POST['specialization']
        years_of_experience = request.POST['years_of_experience']
        Doctor.objects.create(name=name, specialization=specialization, years_of_experience=years_of_experience)
        return redirect('doctor_list')
    return render(request, 'doctor_form.html')

# Update an existing doctor
def doctor_update(request, id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        doctor.name = request.POST['name']
        doctor.specialization = request.POST['specialization']
        doctor.years_of_experience = request.POST['years_of_experience']
        doctor.save()
        return redirect('doctor_list')
    return render(request, 'doctor_form.html', {'doctor': doctor})

# Delete a doctor
def doctor_delete(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('doctor_list')