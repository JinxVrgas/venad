from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone

# Create your models here.
class FinancialYear(models.Model):
    financial_year = models.CharField(max_length=9, null=True)  # Format: YYYY-YYYY
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

class RouteSaleDetails(models.Model):
    Username = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)

class Company(models.Model):
    corporate_identification_number = models.CharField(max_length=20, unique=True)
    company_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=20)
    roc = models.CharField(max_length=50)
    company_category = models.CharField(max_length=50)
    company_subcategory = models.CharField(max_length=50)
    class_of_company = models.CharField(max_length=50)
    date_of_incorporation = models.CharField(max_length=50)
    age_of_company = models.CharField(max_length=50)
    total_members = models.PositiveIntegerField()
    address = models.TextField()
    phone_number_1 = models.CharField(max_length=15)
    phone_number_2 = models.CharField(max_length=15, blank=True, null=True)
    email_id_1 = models.EmailField()
    email_id_2 = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    gstin = models.CharField(max_length=15)
    company_activity = models.TextField()


class DirectorDetails(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/' )
    signature = models.ImageField(upload_to='photos/', null=True)
    father_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=350)
    e_mail = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    pan = models.CharField(max_length=255)
    aadhar = models.CharField(max_length=255)
    din = models.CharField(max_length=255)

class Shareholder(models.Model):
    shareholder_name = models.CharField(max_length=255)
    shareholder_id = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    pin = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    joining_date = models.DateField()
    aadhar = models.CharField(max_length=12, unique=True)
    pan = models.CharField(max_length=10, unique=True)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=11)
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_shares = models.PositiveIntegerField()
    dhalam = models.CharField(max_length=255)
    nominee_name = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)
    annual_turnover = models.DecimalField(max_digits=15, decimal_places=2)
    photo = models.ImageField(upload_to='shareholder_photos/', blank=True, null=True)
    signature = models.ImageField(upload_to='shareholder_signatures/', blank=True, null=True)


class Licenses(models.Model):
    license_name = models.CharField(max_length=10, null=True)
    license_number = models.CharField(max_length=50, null=True)
    expiry_remainder = models.CharField(max_length=50, null=True)
    expiry_date = models.CharField(max_length=10, null=True)
    licenseFile = models.ImageField(upload_to='licenses/', null=True, blank=True)


class Bank(models.Model):
    bank_name = models.CharField(max_length=50,null=True)
    bank_branch = models.CharField(max_length=50,null=True)
    bank_address = models.CharField(max_length=50,null=True)
    bank_account_no =models.CharField(max_length=50,null=True)
    bank_ifsccode =models.CharField(max_length=50,null=True)
    bank_balance = models.CharField(max_length=50,null=True)
    bank_date =models.CharField(max_length=10, null=True)    





class taxmaster(models.Model):
    hs_code = models.CharField(max_length=15, null=True)
    description = models.CharField(max_length=255, null=True)
    goods_service = models.CharField(max_length=10, null=True)  # Consider using choices here if applicable
    igst = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    sgst = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cgst = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cess = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    compensation_cess = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    flood_cess = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)



class ProductCategory(models.Model):
    category_name = models.CharField(max_length=255)



class Member(models.Model):
    Member_PHOTO = models.ImageField(upload_to='memberphoto/', blank=True, null=True)
    Member_TYPE = models.CharField(max_length=50,null=True)
    Member_ID =   models.CharField(max_length=50,null=True)
    Member_NAME =models.CharField(max_length=50,null=True)
    Member_ADDRESS= models.CharField(max_length=50,null=True)
    Member_PHONE_NNUMBER= models.CharField(max_length=255)
    Member_EMAIL=models.EmailField(max_length=255)
    Member_ADHAR_NO=models.CharField(max_length=50,null=True)
    Member_GST=models.CharField(max_length=50,null=True)
    Member_DATE_OF_JOINING=models.CharField(max_length=10, null=True)
    Member_OPENING_BALENCE=models.CharField(max_length=50,null=True)
    Member_CURRENT_BALANCE=models.CharField(max_length=50,null=True)


class Products(models.Model):
    product_category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,null=True)
    product_type = models.CharField(max_length=255,null=True)
    product_code = models.CharField(max_length=20,null=True)
    product_name= models.CharField(max_length=50,null=True)
    product_unit = models.CharField(max_length=50,null=True)
    hsn_code_description = models.ForeignKey(taxmaster,on_delete=models.CASCADE,null=True)
    opening_stoct= models.CharField(max_length=50,null=True)
    minimum_stock = models.CharField(max_length=50,null=True)
    r1price = models.CharField(max_length=50,null=True)
    r2price = models.CharField(max_length=50,null=True)
    r3price = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=200,null=True)

class VendorDetails(models.Model):
    name = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=350,null=True)
    phone = models.CharField(max_length=255,null=True)
    e_mail = models.EmailField(max_length=255,null=True)
    state = models.EmailField(max_length=255,null=True)
    state_type = models.EmailField(max_length=255,null=True)
    gst = models.CharField(max_length=50,null=True)
    taxtype = models.EmailField(max_length=255,null=True)


class PurchaseDetails(models.Model):
    bill_no = models.BigIntegerField(max_length=50,null=True)
    ref_no = models.BigIntegerField(max_length=50,null=True)
    purchase_date = models.CharField(max_length=50,null=True)
    reciept_date = models.CharField(max_length=50,null=True)
    mop = models.CharField(max_length=50,null=True)
    tax_mode = models.CharField(max_length=50,null=True)
    gross_amount = models.BigIntegerField(max_length=50,null=True)
    purchase_tax = models.BigIntegerField(max_length=50,null=True)
    taxable_amount = models.BigIntegerField(max_length=50,null=True)
    paid_amount = models.BigIntegerField(max_length=50,null=True)
    total_discount = models.BigIntegerField(max_length=50,null=True)
    qty_total = models.BigIntegerField(max_length=50,null=True)
    old_balalnce = models.BigIntegerField(max_length=50,null=True)
    total_amount = models.BigIntegerField(max_length=50,null=True)
    new_balance = models.BigIntegerField(max_length=50,null=True)






class purchased_products(models.Model):
    purchased_prod = models.ForeignKey(PurchaseDetails,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Products ,on_delete=models.CASCADE, null=True)
    vendor = models.ForeignKey(VendorDetails,on_delete=models.CASCADE,null=True)
   
    qty = models.CharField(max_length=50,null=True)
    unit = models.CharField(max_length=50,null=True)
    prate = models.CharField(max_length=50,null=True)
    MRP = models.CharField(max_length=50,null=True)
    discount = models.CharField(max_length=50,null=True)
    amount = models.CharField(max_length=50,null=True)
    taxable_amount = models.CharField(max_length=50,null=True)
    cgst_amount = models.CharField(max_length=50,null=True)
    sgst_amount = models.CharField(max_length=50,null=True)
    igst_amount = models.CharField(max_length=50,null=True)
    net_amount = models.CharField(max_length=50,null=True)

class PurchaseReturn(models.Model):
    pur_ret = models.ForeignKey(purchased_products,on_delete=models.CASCADE,null=True)
    ret_qty = models.CharField(max_length=35, null = True,default='0')
    ret_amt = models.CharField(max_length=250,null=True)
    ret_date = models.DateField(max_length=50,null=True)



class Damaged_products(models.Model):
    prod_name = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    damaged_qty = models.CharField(max_length=50,null=True)
    unit = models.CharField(max_length=50,null=True)
    current_stock = models.CharField(max_length=50,null=True)
    stock_balance = models.CharField(max_length=50,null=True)
    date = models.CharField(max_length=50,null=True)
    

class Sale(models.Model):
    customer_name = models.CharField(max_length=100)
     
    customer_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    customer_id = models.PositiveIntegerField()
    customer = GenericForeignKey('customer_type', 'customer_id')
    mop = models.CharField(max_length=10)
    sale_date = models.DateField(default=timezone.now)
    invoice = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    old_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sale_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shareholder_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Percentage
    net_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    received_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    new_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class SaleProducts(models.Model):
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE,null=True)
    product_code = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    r_type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    qty = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sgstamount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cgstamount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    igstamount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tamount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    netamount = models.DecimalField(max_digits=10, decimal_places=2, default=0)




