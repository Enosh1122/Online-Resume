from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def gen_resume(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        education = request.POST.get('education','')
        projects = request.POST.get('projects','')
        skills = request.POST.get('skills','')
        certificates = request.POST.get('certificates','')
        return render(request, 'resume.html',{'name':name,'email':email,'phone':phone,'address':address,
        'education':education,'projects':projects,'skills':skills,'certificates':certificates})
    return render(request, 'index.html')