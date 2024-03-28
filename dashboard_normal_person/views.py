from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Normal
from django.contrib import messages

@login_required
def create_normal(request):
    if request.method == "POST":
        # استخراج البيانات من الطلب
        name = request.POST.get('name')
        nickname = request.POST.get('nickname')
        place_of_birth = request.POST.get('place_of_birth')
        mother_name = request.POST.get('mother_name')
        fathers_name = request.POST.get('fathers_name')
        location = request.POST.get('location')
        phone = request.POST.get('phone')
        commercial_registration_no = request.POST.get('commercial_registration_no')
        date_of_commercial = request.POST.get('date_of_commercial')
        card_number_artisan = request.POST.get('card_number_artisan')
        date_of_artisan = request.POST.get('date_of_artisan')
        written_request = request.FILES.get('written_request')
        property_contract = request.FILES.get('property_contract')
        site_plan = request.FILES.get('site_plan')
        block_plan = request.FILES.get('block_plan')
        technical_data_sheet = request.FILES.get('technical_data_sheet')
        report = request.FILES.get('report')
        # إنشاء نموذج جديد وحفظ البيانات
        normal_instance = Normal(
            name=name,
            nickname=nickname,
            place_of_birth=place_of_birth,
            mother_name=mother_name,
            fathers_name=fathers_name,
            location=location,
            phone=phone,
            commercial_registration_no=commercial_registration_no,
            date_of_commercial=date_of_commercial,
            card_number_artisan=card_number_artisan,
            date_of_artisan=date_of_artisan,
            written_request=written_request,
            property_contract=property_contract,
            site_plan=site_plan,
            block_plan=block_plan,
            technical_data_sheet=technical_data_sheet,
            report=report
        )
        print(request.POST, request.FILES)
        
        # هنا، يجب أن تتأكد من أن البيانات مُستخرجة بشكل صحيح
        # ...

        # بعد إنشاء الكائن وقبل حفظه
        try:
            normal_instance.save()
            messages.success(request, 'تم إنشاء السجل بنجاح!')
        except Exception as e:
            # هذا سيطبع الاستثناء إذا وقع خطأ أثناء الحفظ
            print(e)
            messages.error(request, 'لم يتم إنشاء السجل.')
        normal_instance.save()
        messages.success(request, 'تم إنشاء السجل بنجاح!')
        return redirect('dashboard_n:create_normal')
    else:
        return render(request, 'dashboard_normal.html')
