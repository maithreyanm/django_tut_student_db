from django.shortcuts import render
from blog_ap.models import Person

class DataSync:

    @classmethod
    def fetch_data(cls, request):
        try:
            id = request.POST.get('id')
            cont = Person.objects.get(id=id)
            if cont:
                context = {
                    'datass': cont
                }
                return render(request=request, template_name="blog_ap/get_student_display.html", context=context)

        except Exception as e:
            context = {
                'datass': 'WRONG ID OR ID DOESNT EXIST'
            }
            return render(request=request, template_name="blog_ap/get_student_display.html", context=context)

    @classmethod
    def save_data(cls, request):
        try:
            name = request.POST.get('Name')
            age = request.POST.get('Age')
            email_1 = request.POST.get('email_1')
            email_2 = request.POST.get('email_2')
            pers = Person()
            pers.name = name
            pers.age = age
            pers.email_1 = email_1
            pers.email_2 = email_2
            pers.save()
            return render(request, template_name="blog_ap/save_student.html")

        except Exception as e:
            return render(request, template_name="blog_ap/save_student.html")