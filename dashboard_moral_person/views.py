from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Moral


@login_required
def create_moral(request):
    if request.method == 'POST':
        # استخراج البيانات من الطلب
        named = request.POST.get('Named')
        legal_form = request.POST.get('legal_form')
        address_social_headquarters = request.POST.get('address_social_headquarters')
        name_coordinator_transaction_and_nickname = request.POST.get('name_coordinator_transaction_and_nickname')
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
        # إنشاء كيان جديد في قاعدة البيانات
        Moral.objects.create(
            Named=named,
            legal_form=legal_form,
            address_social_headquarters=address_social_headquarters,
            name_coordinator_transaction_and_nickname=name_coordinator_transaction_and_nickname,
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
        
        # يمكنك تعديل الرد حسب الحاجة
        return HttpResponse('تم إنشاء السجل بنجاح!')
    else:
        # إذا لم يكن الطلب من نوع POST، عد إلى الصفحة الرئيسية أو صفحة النموذج
        return render(request, 'dashboard_moral.html')
