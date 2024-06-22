from django.shortcuts import render
from .models import empdata

def MainPage(request):
    rows = empdata.objects.all()
    return render(request, 'MainPage.html',{'yash':rows})

def AddNewEmp(request):
    if request.method == 'GET':
        return render(request, 'NewEmpForm.html')
    else:
        empdata(
            First_name = request.POST.get('fname'),
            Last_name = request.POST.get('lname'),
            Email_id = request.POST.get('email'),
            Mobile_number = request.POST.get('mobile'),
            Qualification = request.POST.get('qualification'),
            Stream = request.POST.get('stream'),
            Percentage = request.POST.get('percentage'),
            Passed_out_year = request.POST.get('passed'),
            Skill_set = request.POST.get('skill'),
        ).save()
        rows = empdata.objects.all()
        return render(request, 'MainPage.html',{'yash':rows})
def update(request,id):
    if request.method == 'GET':
        row = empdata.objects.get(id=id)
        return render(request, "update.html", {'yash':row})
    else:
        row = empdata.objects.get(id = id)
        row.First_name = request.POST.get('fname')
        row.Last_name = request.POST.get('lname')
        row.Email_id = request.POST.get('email')
        row.Mobile_number = request.POST.get('mobile')
        row.Qualification = request.POST.get('qualification')
        row.Stream = request.POST.get('stream')
        row.Percentage = request.POST.get('percentage')
        row.Passed_out_year = request.POST.get('passed')
        row.Skill_set = request.POST.get('skill')
        row.save()
        rows = empdata.objects.all()
        return render(request, 'MainPage.html',{'yash':rows})


def Delete(request,id):
    row = empdata.objects.get(id= id)
    row.delete()
    rows = empdata.objects.all()
    return render(request, 'MainPage.html',{'yash':rows})




