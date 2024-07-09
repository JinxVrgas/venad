from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.shortcuts import HttpResponse, redirect, render # type: ignore
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from . models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return render(request,'loginpage.html')

def temporary(request):
    
    Vend_obj = VendorDetails.objects.all()
    
    context = {
        
        'vend' : Vend_obj,
       
    }
    return render(request,'temp.html',context)

def dashboard(request):
    return render(request,'dashboard.html')

def  checklogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dash/")
        else:
            return redirect("/")

def navbar(request):
    return render(request,'base.html')


def routsale(request):
    rou = RouteSaleDetails.objects.all()
    context = {
        'routesale': rou
    }
    return render(request, 'routesalelogin.html', context)

def routesale_edit(request):
    id = request.POST.get("id")
    routesale = get_object_or_404(RouteSaleDetails, pk=id)  # Retrieve the financial year object
    context = {
        'routesale': routesale
    }
    return render(request,"routeedit.html", context)

def saveroutesale(request):
    if request.method == 'POST':
        # Extracting data from the POST request

        id = request.POST.get('id')
        username= request.POST.get('username')
        password = request.POST.get('password')


        # Getting the FinancialYear instance or returning a 404 error if not found
        routesale_instance = get_object_or_404(RouteSaleDetails, id=id)

        # Updating the instance with new data
        routesale_instance.Username= username
        routesale_instance.password = password
   
        # Saving the updated instance to the database
        routesale_instance.save()

        # Redirecting to a success page or another relevant page
        return redirect('/route/')  # Change this to the appropriate URL


def financialyear(request):
    financial_years = FinancialYear.objects.all()  # Fetch all financial years
    context = {
        'financial_years': financial_years
    }
    return render(request, 'financialyear.html', context)



    






def routsale_add(request):
    return render(request,'routesaleadd.html')

def finadd(request):
    return render(request,'financialyearadd.html')



def financialedit(request):
    id = request.POST.get("id")
    financial_year = get_object_or_404(FinancialYear, pk=id)  # Retrieve the financial year object
    context = {
        'financial_year': financial_year
    }
    return render(request, "financialyearedit.html", context)



def financialyearadd_tbl(request):
    obj=FinancialYear()
    obj.financial_year=request.POST.get("financialYear")
    obj.start_date = request.POST.get("startDate")
    obj.end_date= request.POST.get("endDate")
    obj.save()
    return redirect('/finyr/')

def routesaleadd_tbl(request):
    obj=RouteSaleDetails()
    obj.Username=request.POST.get("username")
    obj.password = request.POST.get("password")
    
    obj.save()
    return redirect('/route/')






def routesaledetails(request):
    du=RouteSaleDetails.objects.all()
    return render(request,"routesalelogin.html",{"du":du})



def delete_row(request, id):
    try:
        obj = get_object_or_404(RouteSaleDetails, pk=id)
        obj.delete()
        return redirect('/route/')
    except Exception as e:
        return redirect('/route/') 
    
def delete_row_fin(request, id):
    try:
        obj = get_object_or_404(FinancialYear, pk=id)
        obj.delete()
        return redirect('/finyr/')
    except Exception as e:
        return redirect('/finyr/') 


def savefinancialyear(request):
    if request.method == 'POST':
        # Extracting data from the POST request

        id = request.POST.get('id')
        financial_year = request.POST.get('financial_year')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        print(id)
        print(financial_year)

        # Getting the FinancialYear instance or returning a 404 error if not found
        financial_year_instance = get_object_or_404(FinancialYear, id=id)

        # Updating the instance with new data
        financial_year_instance.financial_year = financial_year
        financial_year_instance.start_date = start_date
        financial_year_instance.end_date = end_date

        # Saving the updated instance to the database
        financial_year_instance.save()

        # Redirecting to a success page or another relevant page
        return redirect('/finyr/')  # Change this to the appropriate URL
    

def changepassword(request):
    return render(request,'changepassword.html')


def reset_password(request):
    username = request.POST.get("username")
    new_password = request.POST.get("password")
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    return redirect("/dash/")


def basicinformation(request):
    company = Company.objects.first()  # Assuming there is only one company record
    return render(request, 'companydetails.html', {'company': company})

def update_company_view(request):
    company = Company.objects.first()  # Assuming there is only one company record
    return render(request, "updatecompanydetails.html", {'company': company})


def update_company(request):
    if request.method == 'POST':
        company = get_object_or_404(Company, id=1)  # Adjust the ID or method to get the specific company

        company.corporate_identification_number = request.POST.get('cin', company.corporate_identification_number)
        company.company_name = request.POST.get('company_name', company.company_name)
        company.registration_number = request.POST.get('registration_number', company.registration_number)
        company.roc = request.POST.get('roc', company.roc)
        company.company_category = request.POST.get('company_category', company.company_category)
        company.company_subcategory = request.POST.get('company_subcategory', company.company_subcategory)
        company.class_of_company = request.POST.get('class_of_company', company.class_of_company)
        company.date_of_incorporation = request.POST.get('date_of_incorporation', company.date_of_incorporation)
        company.age_of_company = request.POST.get('age_of_company', company.age_of_company)
        company.total_members = request.POST.get('total_members', company.total_members)
        company.address = request.POST.get('address', company.address)
        company.phone_number_1 = request.POST.get('phone_number1', company.phone_number_1)
        company.phone_number_2 = request.POST.get('phone_number2', company.phone_number_2)
        company.email_id_1 = request.POST.get('email1', company.email_id_1)
        company.email_id_2 = request.POST.get('email2', company.email_id_2)
        company.website = request.POST.get('website', company.website)
        company.gstin = request.POST.get('gstin', company.gstin)
        company.company_activity = request.POST.get('company_activity', company.company_activity)

        company.save()
        return redirect('/companydetails/')  # Redirect to a success page or back to the form

    return HttpResponse(status=405)  # Method not allowed if not POST


#   director pages
    
def directordetails(request):
    director = DirectorDetails.objects.all()  # Fetch all financial years
    context = {
        'direct': director
    }
    return render(request, 'directordetails.html', context)


def director_det_add(request):
    return render(request,'director_det_add.html')



def director_details_add(request):
    direct=DirectorDetails()
    direct.name = request.POST.get('name', direct.name)
    direct.designation = request.POST.get('designation', direct.designation)
    if 'photo' in request.FILES:    
        direct.photo = request.FILES['photo']
    if 'signature' in request.FILES:
        direct.signature = request.FILES['signature']
    direct.father_name = request.POST.get('father_name', direct.father_name)
    direct.date_of_birth = request.POST.get('date_of_birth', direct.date_of_birth)
    direct.address = request.POST.get('address', direct.address)
    direct.e_mail = request.POST.get('email', direct.e_mail)
    direct.phone = request.POST.get('phone', direct.phone)
    direct.pan = request.POST.get('pan', direct.pan)
    direct.aadhar = request.POST.get('aadhar', direct.aadhar)
    direct.din = request.POST.get('din', direct.din)
    
    direct.save()
    return redirect('/dir_det/')


def director_del(request, id):
    try:
        obj = get_object_or_404(DirectorDetails, pk=id)
        obj.delete()
        return redirect('/dir_det/')
    except Exception as e:
        return redirect('/dir_det/') 
    

    return render(request,'director_det_edit.html')




def director_edit(request):
    id = request.POST.get("id")
    director = get_object_or_404(DirectorDetails, pk=id)  
    context = {
        'director': director
    }
    return render(request,"director_det_edit.html", context)


def savedirDet(request):

    if request.method == 'POST':
        # Extracting data from the POST request
        id = request.POST.get('id')
        
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        
        father_name = request.POST.get('father_name')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        e_mail = request.POST.get('email')
        phone = request.POST.get('phone')
        pan = request.POST.get('pan')
        aadhar = request.POST.get('aadhar')
        din = request.POST.get('din')

        # Getting the FinancialYear instance or returning a 404 error if not found
        direct = get_object_or_404(DirectorDetails, id=id)

        # Updating the instance with new data
        direct.name = name
        direct.designation = designation
        if 'photo' in request.FILES:
            direct.photo = request.FILES['photo']
        if 'photo' in request.FILES:
            direct.signature = request.FILES['signature']
        direct.father_name = father_name
        direct.date_of_birth = date_of_birth
        direct.address = address
        direct.e_mail = e_mail
        direct.phone = phone
        direct.pan = pan
        direct.aadhar = aadhar
        direct.din = din
        # Saving the updated instance to the database
        direct.save()

        # Redirecting to a success page or another relevant page
        return redirect('/dir_det/')  # Change this to the appropriate URL





# director pages end


#shareholder
def shareholdershome(request):
    shareholders = Shareholder.objects.all()

    return render(request,'shareholdershome.html', {'shareholders': shareholders})



# def addshareholder(request):
#     largest_member_id_shareholder = Shareholder.objects.order_by('-shareholder_id').first()

#     if largest_member_id_shareholder is not None:
#         next_member_id = largest_member_id_shareholder.shareholder_id
#         last = str(int(next_member_id[-1])+1)
#         next_member_id = next_member_id[:-1]+last

#     return render(request,'addshareholder.html',{'member_id' : next_member_id})


def addshareholder(request):
    try:
        largest_member_id_shareholder = Shareholder.objects.order_by('-shareholder_id').first()
        if largest_member_id_shareholder is not None:
            next_member_id = largest_member_id_shareholder.shareholder_id
            last = str(int(next_member_id[-1]) + 1)
            next_member_id = next_member_id[:-1] + last
        else:
            # Define a default initial shareholder ID if there are no shareholders in the database
            next_member_id = "SH0001"
    except ObjectDoesNotExist:
        # Handle the case where the Shareholder table is empty
        next_member_id = "SH0001"
    except ValueError as e:
        # Handle potential value errors, e.g., if the shareholder_id is not formatted as expected
        print(f"ValueError: {e}")
        next_member_id = "SH0001"
    except Exception as e:
        # Handle any other exceptions
        print(f"Unexpected error: {e}")
        next_member_id = "SH0001"

    return render(request, 'addshareholder.html', {'member_id': next_member_id})






def submit_shareholder(request):
    if request.method == 'POST':
        shareholder_name = request.POST.get('shareholderName')
        shareholder_id = request.POST.get('shareholderID')
        address = request.POST.get('address')
        pin = request.POST.get('pin')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        joining_date = request.POST.get('joiningDate')
        aadhar = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        bank_name = request.POST.get('bankName')
        account_number = request.POST.get('accountNumber')
        branch = request.POST.get('branch')
        ifsc = request.POST.get('ifsc')
        opening_balance = request.POST.get('openingBalance')
        no_of_shares = request.POST.get('noOfShares')
        dhalam = request.POST.get('dhalam')
        nominee_name = request.POST.get('nomineeName')
        relation = request.POST.get('relation')
        annual_turnover = request.POST.get('annualTurnover')

        # Save photo and signature files
        photo = request.FILES.get('photo')
        signature = request.FILES.get('signature')

        # Create Shareholder object and save to database
        shareholder = Shareholder()
        shareholder.shareholder_name=shareholder_name
        shareholder.shareholder_id=shareholder_id
        shareholder.address=address
        shareholder.pin=pin
        shareholder.age=age
        shareholder.phone=phone
        shareholder.dob=dob
        shareholder.joining_date=joining_date
        shareholder.aadhar=aadhar
        shareholder.pan=pan
        shareholder.bank_name=bank_name
        shareholder.account_number=account_number
        shareholder.branch=branch
        shareholder.ifsc=ifsc
        shareholder.opening_balance=opening_balance
        shareholder.no_of_shares=no_of_shares
        shareholder.dhalam=dhalam
        shareholder.nominee_name=nominee_name
        shareholder.relation=relation
        shareholder.annual_turnover=annual_turnover
        shareholder.photo=photo
        shareholder.signature=signature
        shareholder.save()


        # Redirect to success page or do something else
        return redirect("/shareholdershome/")
    else:
        return HttpResponse('Invalid request method')
    
def delshareholder(request, id):
    try:
        obj = get_object_or_404(Shareholder, pk=id)
        obj.delete()
        return redirect('/shareholdershome/')
    except Exception as e:
        return redirect('/shareholdershome/')

def editshareholder(request, id):
    shareholder = get_object_or_404(Shareholder, pk=id)  # Retrieve the financial year object
    context = {
        'shareholder': shareholder
    }
    return render(request, "editshareholder.html", context)
 
def edit_submit_shareholder(request):
    id = request.POST.get('id')
    shareholder = get_object_or_404(Shareholder, pk=id)
    if request.method == 'POST':
        shareholder_name = request.POST.get('shareholderName')
        shareholder_id = request.POST.get('shareholderID')
        address = request.POST.get('address')
        pin = request.POST.get('pin')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        joining_date = request.POST.get('joiningDate')
        aadhar = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        bank_name = request.POST.get('bankName')
        account_number = request.POST.get('accountNumber')
        branch = request.POST.get('branch')
        ifsc = request.POST.get('ifsc')
        opening_balance = request.POST.get('openingBalance')
        no_of_shares = request.POST.get('noOfShares')
        dhalam = request.POST.get('dhalam')
        nominee_name = request.POST.get('nomineeName')
        relation = request.POST.get('relation')
        annual_turnover = request.POST.get('annualTurnover')

        # Save photo and signature files
        photo = request.FILES.get('photo')
        signature = request.FILES.get('signature')

        shareholder.shareholder_name=shareholder_name
        shareholder.shareholder_id=shareholder_id
        shareholder.address=address
        shareholder.pin=pin
        shareholder.age=age
        shareholder.phone=phone
        shareholder.dob=dob
        shareholder.joining_date=joining_date
        shareholder.aadhar=aadhar
        shareholder.pan=pan
        shareholder.bank_name=bank_name
        shareholder.account_number=account_number
        shareholder.branch=branch
        shareholder.ifsc=ifsc
        shareholder.opening_balance=opening_balance
        shareholder.no_of_shares=no_of_shares
        shareholder.dhalam=dhalam
        shareholder.nominee_name=nominee_name
        shareholder.relation=relation
        shareholder.annual_turnover=annual_turnover
        shareholder.photo=photo
        shareholder.signature=signature
        shareholder.save()


        # Redirect to success page or do something else
        return redirect("/shareholdershome/")
    else:
        return HttpResponse('Invalid request method')
#share holder end



#licences
def licenses(request):
    licenses = Licenses.objects.all()  # Fetch all licenses
    context = {
        'licenses': licenses
    }
    return render(request, 'licenses.html', context)

def licensesaddview(request):
    return render (request,"licensesadd.html")




def licenses_add(request):
    if request.method == 'POST':
        obj = Licenses()
        li = request.POST.get('expiryRemainder')
        print(li)
        obj.license_name = request.POST.get('licenseName')
        obj.license_number = request.POST.get('licenseNumber')
        obj.expiry_remainder = li
        obj.expiry_date = request.POST.get('expiryDate')
        obj.licenseFile = request.FILES.get('licenseFile')
        obj.save()
        return redirect('/licenses/')


def licensesedit(request):
    id = request.POST.get("id")
    licenses = get_object_or_404(Licenses, pk=id)  # Retrieve the financial year object
    context = {
        'licenses': licenses
    }
    return render(request, "licensesedit.html", context)


def delete_row_licenses(request, id):
    try:
        obj = get_object_or_404(Licenses, pk=id)
        obj.delete()
        return redirect('/licenses/')
    except Exception as e:
        return redirect('/licenses/')

def savelicences(request):
    if request.method == 'POST':
        # Extracting data from the POST request

        id = request.POST.get('id')
        licenseName = request.POST.get('licenseName')
        licenseNumber = request.POST.get('licenseNumber')
        expiryRemainder = request.POST.get('expiryRemainder')
        expiryDate = request.POST.get('expiryDate')
        licenseFile = request.POST.get('licenseFile')




        # Getting the FinancialYear instance or returning a 404 error if not found
        Licenses_instance = get_object_or_404(Licenses, id=id)

        # Updating the instance with new data
        Licenses_instance.license_name = licenseName
        Licenses_instance.license_number = licenseNumber
        Licenses_instance.expiry_remainder = expiryRemainder
        Licenses_instance.expiry_date = expiryDate
        Licenses_instance.licenseFile = licenseFile

        # Saving the updated instance to the database
        Licenses_instance.save()

        # Redirecting to a success page or another relevant page
        return redirect('/licenses/')  # Change this to the appropriate URL
    
def licensesprint(request):
    return render(request, 'licensesprint.html')


#licences end
#bank 


def bankadd_page(request):
    return render (request,'bankadd.html')




def bankadd_tbl(request):

    obj=Bank()
    obj.bank_name = request.POST.get("bank-name")
    obj.bank_branch = request.POST.get("bank-branch")
    obj.bank_address= request.POST.get("bank-address")
    obj.bank_account_no=request.POST.get("account-no")
    obj.bank_ifsccode= request.POST.get("ifsc-code")
    obj.bank_balance =request.POST.get("opening-balance")
    obj.bank_date = request.POST.get("date")


    obj.save()
    return redirect('/bank/')





# def add_bank(request):
#     if request.method == "POST":
#         bank_name = request.POST.get('bank_name')
#         bank_branch = request.POST.get('bank_branch')
#         bank_address = request.POST.get('bank_address')
#         bank_account_no = request.POST.get('bank_account_no')
#         bank_ifsccode = request.POST.get('bank_ifsccode')
#         bank_balance = request.POST.get('bank_balance')
#         bank_date = request.POST.get('bank_date')
        
#         Bank.objects.create(
#             bank_name=bank_name,
#             bank_branch=bank_branch,
#             bank_address=bank_address,
#             bank_account_no=bank_account_no,
#             bank_ifsccode=bank_ifsccode,
#             bank_balance=bank_balance,
#             bank_date=bank_date
#         )
#         return redirect('dash')  # Redirect to a relevant page
#     return render(request, 'bank_form.html')

def edit_bank(request, id):
    bank = get_object_or_404(Bank, id=id)
    
    if request.method == 'POST':
        bank_name = request.POST.get('bank_name')
        bank_branch = request.POST.get('bank_branch')
        bank_ifsc = request.POST.get('bank_ifsc')
        bank_district = request.POST.get('bank_district')
        bank_state = request.POST.get('bank_state')
        
        # Ensure none of the fields are empty
        if bank_name and bank_branch and bank_ifsc and bank_district and bank_state:
            bank.bank_name = bank_name
            bank.bank_branch = bank_branch
            bank.bank_ifsc = bank_ifsc
            bank.bank_district = bank_district
            bank.bank_state = bank_state
            bank.save()
            return redirect('bank')  # Redirect to the desired page after saving
        else:
            # Handle the case where one or more fields are empty
            error_message = "All fields are required."
            return render(request, 'edit_bank.html', {'bank': bank, 'error_message': error_message})
    
    return render(request, 'edit_bank.html', {'bank': bank})



def deletebank(request, id):
    print(id)
    try:
        obj = get_object_or_404(Bank, pk=id)
        obj.delete()
        return redirect('/bank/')
    except Exception as e:
        return redirect('/bank/')


def bank_page(request):
    bank = Bank.objects.all()
    context = {
        'bank_det' : bank
    }
    return render (request,'bank.html',context)



def bank_edit(request):
    id = request.POST.get("id")
    print(id)
    obj = get_object_or_404(Bank, pk=id) # Retrieve the financial year object
    context = {
        'ban': obj
    }
    return render(request, "bankedit.html", context)

def save_bank(request):
    if request.method == 'POST':
        # Extracting data from the POST request

        id = request.POST.get('id')
        
     
        # Getting the FinancialYear instance or returning a 404 error if not found
        bank = get_object_or_404(Bank, id=id)

        bank.bank_name =request.POST.get('bank-name') 
        bank.bank_branch =request.POST.get('bank-branch') 
        bank.bank_address = request.POST.get('bank-address')
        bank.bank_account_no =request.POST.get('account-no') 
        bank.bank_ifsccode =request.POST.get('ifsc-code') 
        bank.bank_balance =request.POST.get('opening-balance') 
        bank.bank_date = request.POST.get('date')

        # Saving the updated instance to the database
        bank.save()

        # Redirecting to a success page or another relevant page
        return redirect('/bank/')

#bank end
# vendor details
def vendor_details_page(request):
    vendor = VendorDetails.objects.all()
    context = {
        'ven' : vendor
    }
    return render(request,'vendor/vendor_details_page.html',context)

def vendor_add_page(request):
    return render(request,'vendor/vendor_add_page.html')

def vendor_edit_page(request):
    id = request.POST.get("id")
    print(id)
    obj = get_object_or_404(VendorDetails, pk=id) # Retrieve the financial year object
    context = {
        'ven': obj
    }
    return render(request, "vendor/vendor_edit_page.html", context)


def vendor_add_tbl(request):
    obj=VendorDetails()
    obj.name=request.POST.get("name")
    obj.address = request.POST.get("address")
    obj.phone= request.POST.get("phone")
    obj.e_mail = request.POST.get("email")
    obj.state = request.POST.get("state")
    obj.state_type = request.POST.get("state_type")
    obj.gst = request.POST.get("gst")
    obj.taxtype = request.POST.get("taxtype")

    obj.save()
    return redirect('/v_det_page/')

def vendor_delete(request,id):
    try:
        obj = get_object_or_404(VendorDetails, pk=id)
        obj.delete()
        return redirect('/v_det_page/')
    except Exception as e:
        return redirect('/v_det_page/')


def vendor_edit(request):
    id = request.POST.get("id")
    obj = get_object_or_404(VendorDetails, id=id)
    obj.name = request.POST.get("name")
    obj.address = request.POST.get("address")
    obj.phone = request.POST.get("phone")
    obj.e_mail = request.POST.get("email")
    obj.stateandtin = request.POST.get("stateandtin")
    obj.gst = request.POST.get("gst")
    obj.taxtype = request.POST.get("taxtype")
    obj.save()
    return redirect('/v_det_page/')



# vendor end
# taxmaster

def taxmaster_list(request):
    hsncodes = taxmaster.objects.all()
    return render(request, 'taxmaster.html', {'hsncodes': hsncodes})


def taxmasteraddview(request):
    return render(request, 'taxmasteradd.html')

def add_taxmaster(request):
    if request.method == 'POST':
        obj = taxmaster()
        obj.hs_code = request.POST.get('hsCode')
        obj.description = request.POST.get('description')
        obj.goods_service = request.POST.get('goodsService')
        obj.igst = request.POST.get('igst')
        obj.sgst = request.POST.get('sgst')
        obj.cgst = request.POST.get('cgst')
        obj.cess = request.POST.get('cess')
        obj.compensation_cess = request.POST.get('compensationCess')
        obj.flood_cess = request.POST.get('floodCess')
        obj.save()
        return redirect('/taxmaster/')  # Redirect to the tax master list view




def edit_taxmaster(request, id):
    objtaxmaster = get_object_or_404(taxmaster, pk=id)  # Retrieve the financial year object
    context = {
        'taxmaster': objtaxmaster
    }
    return render(request, 'taxmasteredit.html', context)

def delete_taxmaster(request, id):
    hsncode = get_object_or_404(taxmaster, id=id)
    hsncode.delete()
    return redirect('/taxmaster/')

def save_taxmaster(request):
    if request.method == 'POST':
        # Extracting data from the POST request
        id = request.POST.get('id')
        hs_code = request.POST.get('hsCode')
        description = request.POST.get('description')
        goods_service = request.POST.get('goodsService')
        igst = request.POST.get('igst')
        sgst = request.POST.get('sgst')
        cgst = request.POST.get('cgst')
        cess = request.POST.get('cess')
        compensation_cess = request.POST.get('compensationCess')
        flood_cess = request.POST.get('floodCess')

        # Getting the HSNCodeTax instance or returning a 404 error if not found
        hsncode_instance = get_object_or_404(taxmaster, id=id)

        # Updating the instance with new data
        hsncode_instance.hs_code = hs_code
        hsncode_instance.description = description
        hsncode_instance.goods_service = goods_service
        hsncode_instance.igst = igst
        hsncode_instance.sgst = sgst
        hsncode_instance.cgst = cgst
        hsncode_instance.cess = cess
        hsncode_instance.compensation_cess = compensation_cess
        hsncode_instance.flood_cess = flood_cess

        # Saving the updated instance to the database
        hsncode_instance.save()

        # Redirecting to a success page or another relevant page
        return redirect('/taxmaster/')

# taxmaster end
#productdetails

def productcategory(request):
    category = ProductCategory.objects.all()
    return render(request, "productcategory.html",{'category':category})

def addcategory(request):
    return render(request, "addcategory.html")

def savecategory(request):
    id = request.POST.get("id")
    if id == '':
        id = -1
    if id == -1:
        obj = ProductCategory()
        obj.category_name = request.POST.get("category_name")
        obj.save()
    else:
        obj = get_object_or_404(ProductCategory, id=id)
        obj.category_name = request.POST.get("category_name")
        obj.save()

    return redirect("/productcategory/")

def editcategory(request,id):
    category = get_object_or_404(ProductCategory, pk=id)
    return render(request, "addcategory.html",{'category':category})

def deletecategory(request, id):
    try:
        obj = get_object_or_404(ProductCategory, pk=id)
        obj.delete()
        return redirect('/productcategory/')
    except Exception as e:
        return redirect('/productcategory/')

#productdetails end

#member

def members_page(request):
    obj = Member.objects.all()
    context = {
        "Member": obj
    }
    return render (request,'member/member.html',context)

def members_add_page(request):
    return render(request,'member/addmember.html')



def members_add(request):
    obj = Member()
    image = request.FILES['photo']
    fs = FileSystemStorage()
    file = fs.save(image.name, image)
    url = fs.url(file)
    obj.Member_PHOTO = url
  
   
   
 
    obj.Member_TYPE = request.POST.get("member-type")
    obj.Member_NAME =request.POST.get("member-name")
    obj.Member_ADDRESS= request.POST.get("member-address")
    obj.Member_PHONE_NNUMBER= request.POST.get("member-phone-number")
    obj.Member_EMAIL= request.POST.get("member-email")
    obj.Member_ADHAR_NO =request.POST.get("member-adhar-no")
    obj.Member_GST= request.POST.get("member-gst")
    obj.Member_DATE_OF_JOINING = request.POST.get("member-date-of-joining")
    obj.Member_OPENING_BALENCE = request.POST.get("opening-balance")
    obj.Member_CURRENT_BALANCE = request.POST.get("current-balance")
    obj.Member_ID = request.POST.get("member-id")
    
    obj.save()
    return redirect('/members_page/')


def member_edit_page(request,id):
    obj = get_object_or_404(Member, pk=id)
    return render(request,'member/memberedit.html',{'mem' :obj})

def member_del_page(request, id):
    print(id)
    try:
        obj = get_object_or_404(Member, pk=id)
        obj.delete()
        return redirect('/members_page/')
    except Exception as e:
        return redirect('/members_page/')

#member end
#product
def product(request):
    product = Products.objects.all()
    context = {
        'prod': product
    }
    return render(request, 'product/product.html', context)


def prodAdd(request):
    data=ProductCategory.objects.all()
    data1 = taxmaster.objects.all()
    return render(request, "product/productadd.html",{"data":data,"data1":data1})


def product_add(request):
    obj = Products()
    obj.product_category_id = request.POST.get("product-category")
    obj.product_type = request.POST.get("product-Type")
    obj.product_code = request.POST.get("product-Code")
    obj.product_name = request.POST.get("product-Name")
    obj.product_unit = request.POST.get("product-Unit")
    obj.hsn_code_description_id = request.POST.get("hsn-code-description")
    obj.opening_stoct = request.POST.get("opening_stock")
    obj.minimum_stock = request.POST.get("minimum_stock")
    obj.r1price = request.POST.get("R1_price")
    obj.r2price = request.POST.get("R2_price")
    obj.r3price = request.POST.get("R3_price")
    obj.description = request.POST.get("description")
    obj.save()
    return redirect("/product/")
def take_hsn_code(request):
    hsn=request.GET.get("hsn")
    data=taxmaster.objects.get(id=hsn)
    hsn_code=data.hs_code
    return JsonResponse({"hsn_code":hsn_code})
def product_del_tbl(request, id):
    try:
        obj = get_object_or_404(Products, pk=id)
        obj.delete()
        return redirect('/product/')
    except Exception as e:
        return redirect('/product/')


def product_edit_page(request, id):
    obj = get_object_or_404(Products, pk=id)
    data = ProductCategory.objects.all()
    data1 = taxmaster.objects.all()
    context = {
        "prod": obj,
        'data':data,
        "data1":data1
    }
    return render(request, "product/productedit.html", context)


def save_product_edit(request):
    id = request.POST.get("id")
    obj = get_object_or_404(Products, pk=id)
    obj.product_category_id = request.POST.get("product-category")
    obj.product_type = request.POST.get("product-Type")
    obj.product_code = request.POST.get("product-Code")
    obj.product_name = request.POST.get("product-Name")
    obj.product_unit = request.POST.get("product-Unit")
    obj.hsn_code_description_id = request.POST.get("hsn-code-description")
    obj.hsn_code = request.POST.get("hsn-code")
    obj.opening_stoct = request.POST.get("opening_stock")
    obj.minimum_stock = request.POST.get("minimum_stock")
    obj.r1price = request.POST.get("R1_price")
    obj.r2price = request.POST.get("R2_price")
    obj.r3price = request.POST.get("R3_price")
    obj.description = request.POST.get("description")
    obj.save()
    return redirect("/product/")
#product end
#purchase

def purchase_details_page(request):
    obj = purchased_products.objects.all()
    context = {
        'det' : obj
    }
    return render(request,"purchase/purchase_details_page.html",context)


def purchase_delete(request,id):
    try:
        obj = get_object_or_404(purchased_products,pk=id)
        obj.delete()
        return redirect('/purchase_det_page/')
    except Exception as e:
        return redirect('/purchase_det_page/')
    
def purchase_edit(request,id):
    obj = get_object_or_404(purchased_products, pk=id)
    pur_prods = purchased_products.objects.filter(vendor_id=obj.vendor_id, purchased_prod__reciept_date=obj.purchased_prod.reciept_date,purchased_prod__bill_no = obj.purchased_prod.bill_no )
    

    now = datetime.now()
    Vend_obj = VendorDetails.objects.all()


    context = {
        
        'pur' : pur_prods,
        'current_date': now,
        'vend': Vend_obj,
        }
    
    return render(request,'purchase/purchase_edit_page.html',context)



def invoice_page(request,id):
    obj = get_object_or_404(purchased_products, pk=id)
    
    # Filter objects where the vendor matches the vendor of the retrieved object
    x = purchased_products.objects.filter(vendor_id=obj.vendor_id, purchased_prod__reciept_date=obj.purchased_prod.reciept_date,purchased_prod__bill_no = obj.purchased_prod.bill_no )

    now = datetime.now()    
    context = {
        'invo' : obj,
        'current_date': now,
        'prod':x

    }
    return render(request,"purchase/invoice.html",context)








def purchase_add_save(request):
    obj1 = PurchaseDetails()
    obj1.bill_no = request.POST.get("bill_number")
    obj1.ref_no = request.POST.get("ref_number")
    obj1.purchase_date = request.POST.get("purchase_date")
    obj1.reciept_date = request.POST.get("reciept_date")
    obj1.mop = request.POST.get("MOP")
    obj1.tax_mode =request.POST.get("tax_mode")
    obj1.gross_amount = request.POST.get("gross-amount")
    obj1.purchase_tax = request.POST.get("purchase-tax")
    obj1.paid_amount = request.POST.get("paid-amount")
    obj1.qty_total = request.POST.get("qty-total")
    obj1.old_balalnce = request.POST.get("old-balance")
    obj1.total_amount = request.POST.get("total_amount")
    obj1.new_balance = request.POST.get("new-balance")
    obj1.taxable_amount = request.POST.get("taxable-amount")
    obj1.total_discount = request.POST.get("total-discount")

    obj1.save()


   
    serial_numbers = request.POST.getlist('serial_number[]')
    item_names = request.POST.getlist('product_drop[]')
    bill_no = request.POST.get("bill_number")
    dropdown = request.POST.get("dropdown")
    quantities = request.POST.getlist('qty[]')
    units = request.POST.getlist('unit[]')
    prates = request.POST.getlist('prate[]')
    mrps = request.POST.getlist('mrp[]')
    
    discounts = request.POST.getlist('discount[]')
    amounts = request.POST.getlist('amount[]')
    taxable_amounts = request.POST.getlist('taxable-amt[]')
    cgst_amounts = request.POST.getlist('cgst-amt[]')
    sgst_amounts = request.POST.getlist('sgst-amt[]')
    igst_amounts = request.POST.getlist('igst-amt[]')
    net_amounts = request.POST.getlist('net-amt[]')

    for i in range(len(serial_numbers)):
        obj = purchased_products()
        print(quantities[i])
        obj.qty = quantities[i]
        obj.unit = units[i]
        obj.product_id = item_names[i]
        obj.purchased_prod_id = obj1.id
        obj.vendor_id = dropdown
        obj.prate = prates[i]
        obj.MRP = mrps[i]
        obj.discount = discounts[i]
        obj.amount = amounts[i]
        obj.taxable_amount = taxable_amounts[i]
        obj.cgst_amount = cgst_amounts[i]
        obj.sgst_amount = sgst_amounts[i]
        obj.igst_amount = igst_amounts[i]
        obj.net_amount = net_amounts[i]
        obj.save()
    return redirect("/purchase_det_page/")

            
            # Retrieve other fields similarly

@csrf_exempt
def ajax_view_for_products(request):
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option')
        obj = get_object_or_404(Products, pk=selected_option)
        x = Products.objects.get(id = selected_option)
        hsncode = x.hsn_code_description.hs_code
        r1= obj.r1price
        r2 = obj.r2price
        r3 = obj.r3price
        cgst= x.hsn_code_description.cgst
        sgst= x.hsn_code_description.sgst
        igst= x.hsn_code_description.igst

        response_data = {
            'message': f'Selected option is {selected_option}',
            'hsncode': hsncode,
            'r1' : r1,
            'r2' : r2,
            'r3' : r3,
            'cgst' : cgst,
            'sgst' : sgst,
            'igst' : igst,


            
        }

        print(response_data)
        return JsonResponse(response_data)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)




            
@csrf_exempt
def ajax_view(request):
    if request.method == 'POST':
        
        selected_option = request.POST.get('selected_option')
       
        #latest_product = purchased_products.objects.filter(vendor_id=selected_option).order_by('-product__reciept_date').first()
        latest_product = purchased_products.objects.filter(vendor_id=selected_option ).order_by('-purchased_prod__reciept_date').first()
        obj = get_object_or_404(VendorDetails, pk=selected_option)
        state = obj.state
        state_type = obj.state_type
        gst = obj.gst
        taxtype = obj.taxtype
        old_bal = latest_product.purchased_prod.new_balance
        print(old_bal)
        

        response_data = {
            'message': f'Selected option is {selected_option}',
            'state': state,
            'state_type': state_type,
            'gst': gst,
            'taxtype': taxtype,
            'bal' : old_bal
            
        }

        print(response_data)
        return JsonResponse(response_data)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)


def process_form(request):
    if request.method == 'POST':
        
        return redirect('success_page')  # Redirect to a success page

    return render(request, 'your_template.html')






def purchase_edit_save(request):
    b_no = request.POST.get("bill_number")
    obj1 = get_object_or_404(PurchaseDetails,bill_no = b_no )
    obj1.ref_no = request.POST.get("ref_number")
    obj1.purchase_date = request.POST.get("purchase_date")
    obj1.reciept_date = request.POST.get("reciept_date")
    obj1.mop = request.POST.get("MOP")
    obj1.tax_mode =request.POST.get("tax_mode")
    obj1.gross_amount = request.POST.get("gross-amount")
    obj1.purchase_tax = request.POST.get("purchase-tax")
    obj1.paid_amount = request.POST.get("paid-amount")
    obj1.qty_total = request.POST.get("qty-total")
    obj1.old_balalnce = request.POST.get("old-balance")
    obj1.total_amount = request.POST.get("total_amount")
    obj1.new_balance = request.POST.get("new-balance")
    obj1.taxable_amount = request.POST.get("taxable-amount")
    obj1.total_discount = request.POST.get("total-discount")
    obj1.save()


   
    serial_numbers = request.POST.getlist('serial_number[]')
    item_names = request.POST.getlist('product_drop[]')
    dropdown = request.POST.get("dropdown")
    quantities = request.POST.getlist('qty[]')
    units = request.POST.getlist('unit[]')
    prates = request.POST.getlist('prate[]')
    mrps = request.POST.getlist('mrp[]')
    discounts = request.POST.getlist('discount[]')
    amounts = request.POST.getlist('amount[]')
    taxable_amounts = request.POST.getlist('taxable-amt[]')
    cgst_amounts = request.POST.getlist('cgst-amt[]')
    sgst_amounts = request.POST.getlist('sgst-amt[]')
    igst_amounts = request.POST.getlist('igst-amt[]')
    net_amounts = request.POST.getlist('net-amt[]')
    obj_list = purchased_products.objects.filter(purchased_prod_id=obj1.id)

    for i, obj in enumerate(obj_list):
        obj.qty = quantities[i]
        obj.unit = units[i]
        obj.product_id = item_names[i]
        obj.purchased_prod_id = obj1.id
        obj.vendor_id = dropdown
        obj.prate = prates[i]
        obj.MRP = mrps[i]
        obj.discount = discounts[i]
        obj.amount = amounts[i]
        obj.taxable_amount = taxable_amounts[i]
        obj.cgst_amount = cgst_amounts[i]
        obj.sgst_amount = sgst_amounts[i]
        obj.igst_amount = igst_amounts[i]
        obj.net_amount = net_amounts[i]
        # Save the updated object
        obj.save()
    return redirect("/purchase_det_page/")


def del_pur_row(request,id):
    try:
        obj = get_object_or_404(purchased_products, pk=id)
        obj.delete()
        return redirect('/purchase_det_page/')
    except Exception as e:
        return redirect('/purchase_det_page/')


def purchase_add_page(request):
    now = datetime.now()
    Vend_obj = VendorDetails.objects.all()
    prod_obj = Products.objects.all()
    try:
       
        largest_bill_record = PurchaseDetails.objects.order_by('-bill_no').first()
        if largest_bill_record is not None:
            next_bill_number = largest_bill_record.bill_no
            try:
                # Assuming bill_no is an integer stored as a string
                next_bill_number = str(int(next_bill_number) + 1)
            except ValueError as e:
                print(f"ValueError: {e}")
                next_bill_number = "6875"
        else:
            next_bill_number = "6875"
    except ObjectDoesNotExist:
        next_bill_number = "6875"
    except Exception as e:
        print(f"Unexpected error: {e}")
        next_bill_number = "6875"

    return render(request, 'purchase/purchase_det_add_page.html', {
        'bill_no': next_bill_number,
        'current_date': now,
        'vend': Vend_obj,
        'prod': prod_obj,
        
    })


    



#purchase end


#attendance




#attendance end





#damaged products

def damaged_products_page(request):
    obj = Damaged_products.objects.all()
    context = {
        'dam' : obj
    }
    return render(request,"damaged products/damagedproduct_manage.html",context)


@csrf_exempt
def damaged_prod_ajax(request):
    if request.method == 'POST':
        
        selected_option = request.POST.get('selected_option')
       
        #latest_product = purchased_products.objects.filter(vendor_id=selected_option).order_by('-product__reciept_date').first()
        
        obj = get_object_or_404(Products,pk=selected_option)
        current_stock = obj.opening_stoct
        unit = obj.product_unit
        print(selected_option)
        

        response_data = {
            'message': f'Selected option is {selected_option}',
            'current' : current_stock,
            'unit' : unit
            
        }

        print(response_data)
        return JsonResponse(response_data)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)


def damaged_products_add_page(request):
    now = datetime.now()
    obj_prod = Products.objects.all()
    context = {
        'current_date' : now,
        'prod' : obj_prod
     }
    return render(request,"damaged products/damagedproduct_add.html",context)




def damaged_products_add(request):
    serial_numbers = request.POST.getlist('serial_number[]')
    name = request.POST.getlist("product_drop[]")
    damaged_qty = request.POST.getlist("damaged_qty[]")
   
    units = request.POST.getlist('unit[]')
    current_stock = request.POST.getlist("current_stock[]")
    bal_stock = request.POST.getlist("stock_balance[]")
    date = request.POST.get("reciept_date")
    


    for i in range(len(serial_numbers)): 
       
        obj = Damaged_products()
        obj.prod_name_id = name[i]
        obj.damaged_qty = damaged_qty[i]
        obj.unit = units[i]
        obj.current_stock = current_stock[i]    
        obj.stock_balance = bal_stock[i]
        obj.date = date
        obj.save()
    return redirect("/damaged_prod_page/")


def del_damaged_product(request,id):
    try: 
        obj = get_object_or_404(Damaged_products,pk=id)
        obj.delete()
        return redirect('/damaged_prod_page/')
    except Exception as e:
        return redirect('/damaged_prod_page/')
    
def edit_damaged_product(request,id):
    now = datetime.now()
    obj_prod = Products.objects.all()
    context = {
        'current_date' : now,
        'prod' : obj_prod
     }
    return render(request,"damaged products/damaged_products_edit_page.html",context)




#sale

def salehome(request):
    sale =Sale.objects.all()
    return render(request, "sale/salehome.html",{'sale':sale})

def addsale(request):
    current_date = datetime.now()
    largest_billno = Sale.objects.order_by('-id').first()
    

    if largest_billno is not None:
        next_bill_no = largest_billno.invoice
        last = str(int(next_bill_no[-1])+1)
        next_bill_no = next_bill_no[:-1]+last
    else:
        next_bill_no = "KPAC0001"
        
    product = Products.objects.all()

    context = {
        'current_date': current_date,
        'bill_no':next_bill_no,
        'prod':product
    }
    return render(request, "sale/addsale.html",context)


def get_customers(request):
    customer_type = request.GET.get('type')
    if customer_type == 'Shareholder':
        customers = Shareholder.objects.all()
        customer_data = [{'id': customer.id, 'name': customer.name} for customer in customers]
    elif customer_type == 'Wholesale':
        customers = Member.objects.filter(Member_TYPE ='wholesale')
        customer_data = [{'id': customer.id, 'name': customer.name} for customer in customers]
    elif customer_type == 'Retail':
        customers = Member.objects.filter(Member_TYPE ='Retail')
        customer_data = [{'id': customer.id, 'name': customer.name} for customer in customers]
    else:
        customers = []

    
    return JsonResponse(customer_data, safe=False)



from django.http import JsonResponse
from .models import Products

def get_product_details(request):
    product_name = request.GET.get('product_name')
    product = Products.objects.filter(product_name=product_name).first()
    
    if product:
        taxmaster_instance = product.hsn_code_description  # This is the related taxmaster instance
        data = {
            'product_code': product.product_code,
            'hsn_code_description': taxmaster_instance.hs_code if taxmaster_instance else '',
            'rate_r1': product.r1price,
            'rate_r2': product.r2price,
            'rate_r3': product.r3price,
            'igst' : product.hsn_code_description.igst,
            'cgst' :product.hsn_code_description.cgst,
            'sgst' :product.hsn_code_description.sgst,
        }
    else:
        data = {}
    
    return JsonResponse(data)

def save_sale(request):
    if request.method == 'POST':
        customer_type_model = request.POST.get('customer_type')
        customer_name_select = request.POST.get('customer_name_select')
        customer_name_input = request.POST.get('customer_name_input')

        # Determine the customer name based on the input field
        if customer_name_select == 'other':
            customer_name = customer_name_input
        else:
            customer_name = customer_name_select
        mop = request.POST.get('MOP')
        sale_date = request.POST.get('purchase_date')
        invoice = request.POST.get('bill_number')
        address = request.POST.get('address', '')
        mobile = request.POST.get('mobile_no', '')
        old_balance = request.POST.get('old-balance', 0)
        total_qty = request.POST.get('qty-total', 0)
        sale_amount = request.POST.get('total-amount', 0)
        discount = request.POST.get('discount-amount', 0)
        shareholder_discount = request.POST.get('shareholder-discount', 0)
        net_total = request.POST.get('gross-amount', 0)
        received_amount = request.POST.get('received-amount', 0)
        new_balance = request.POST.get('balance', 0)
        if (customer_type_model == "Wholesale" or customer_type_model == "Retail"):
            customer_type_model ="Member"
     
    
        customer_type = ContentType.objects.get(model=customer_type_model.lower())
        print(customer_type.name)

        sale = Sale.objects.create(
            customer_name=customer_name,
            customer_type=customer_type,
            customer_id=request.POST.get('customer_id', 0),
            mop=mop,
            sale_date=sale_date,
            invoice=invoice,
            address=address,
            mobile=mobile,
            old_balance=old_balance,
            total_qty=total_qty,
            sale_amount=sale_amount,
            discount=discount,
            shareholder_discount=shareholder_discount,
            net_total=net_total,
            received_amount=received_amount,
            new_balance=new_balance
        )

        product_codes = request.POST.getlist('product_code[]')
        rate_types = request.POST.getlist('rate_Type[]')
        prices = request.POST.getlist('rate[]')
        quantities = request.POST.getlist('qty[]')
        discounts = request.POST.getlist('discount[]')
        sgstamounts = request.POST.getlist('sgst-amt[]')
        cgstamounts = request.POST.getlist('cgst-amt[]')
        igstamounts = request.POST.getlist('igst-amt[]')
        netamounts = request.POST.getlist('net-amt[]')
        amounts = request.POST.getlist('amount[]')
        tamounts = request.POST.getlist('taxable-amt[]')

        for i in range(len(product_codes)):
            product = Products.objects.get(product_code=product_codes[i])
            SaleProducts.objects.create(
                sale=sale,
                product_code=product,
                r_type=rate_types[i],
                price =prices[i],
                qty=quantities[i],
                discount=discounts[i],
                sgstamount=sgstamounts[i],
                cgstamount=cgstamounts[i],
                igstamount = igstamounts[i],
                amount = amounts[i],
                tamount = tamounts[i],
                netamount=netamounts[i]
            )

        return redirect('/sale_home/')

def invoice(request,id):
    obj = get_object_or_404(Sale, pk=id)
    obj2 = SaleProducts.objects.filter(sale_id =id)
    total_tamount = sum(item.netamount for item in obj2)
    total_dis = total_tamount - obj.net_total
    bal = obj.net_total+obj.new_balance-obj.received_amount
    price =obj
    return render(request,'sale/invoice.html',{'sale':obj,'prod':obj2,'total_tamount':total_tamount,'total_dis':total_dis,'bal':bal})

def get_old_balance(request):
    user_name = request.GET.get('user', None)
    if user_name:
        try:
            customer = Sale.objects.filter(customer_name=user_name).order_by('-id').first()
            old_balance = customer.new_balance  # Assuming 'old_balance' is a field in the Customer model
            return JsonResponse({'oldBalance': old_balance})
        except Sale.DoesNotExist:
            return JsonResponse({'oldBalance': 'User not found'}, status=404)
    else:
        return JsonResponse({'oldBalance': 'No user specified'}, status=400)
    
def delete_sale(request,id):
    try:
        obj = get_object_or_404(Sale, pk=id)
        obj2 = SaleProducts.objects.filter(sale =id)
        obj.delete()
        obj2.delete()
        return redirect('/sale_home')
    except Exception as e:
        return redirect('/sale_home/')

#sale end




#purchase return
def purchase_return_page(request):
    obj  = purchased_products.objects.all()
    obj_ret = PurchaseReturn.objects.all()
    context = {

        'prod' : obj,
        'ret' : obj_ret
    }
    return render(request,"purchase_return\purchase_return_details_page.html",context)

def purchase_return_edit(request,id):
    obj = get_object_or_404(purchased_products, pk=id)
    pur_prods = purchased_products.objects.filter(vendor_id=obj.vendor_id, purchased_prod__reciept_date=obj.purchased_prod.reciept_date,purchased_prod__bill_no = obj.purchased_prod.bill_no )
    now = datetime.now()
    context = {
        'pur' : pur_prods,
        'current_date': now,
        }
    return render(request,'purchase_return/purchase_return_edit.html',context)

def save_return(request):
        now = datetime.now()
        r_qty = request.POST.getlist("return_qty")
        r_amt = request.POST.getlist("return_amt")
        id = request.POST.getlist("id")
        for i in range(len(id)):
            obj = PurchaseReturn()
            print(id)
            obj.ret_qty = r_qty[i]
            obj.ret_amt = r_amt[i]
            obj.ret_date = now.date()
            obj.pur_ret_id = id[i]
            obj.save() 
        return redirect("/purchase_return_page/")

#purchase return end