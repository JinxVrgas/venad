from django.urls import include, path # type: ignore
from django.conf.urls.static import static
from venad1 import settings
from venadApp import views



urlpatterns = [
    path("",views.index),
    path("dash/",views.dashboard),
    path("checklogin/",views.checklogin),
    path("nav",views.navbar),
    path("route/",views.routsale),
    path("routeadd/",views.routsale_add),
    path("finyradd/",views.finadd,),
    path("finyr/",views.financialyear,),
    path("finedit/",views.financialedit),
    path("fintbl/",views.financialyearadd_tbl),
    path("routetbl/",views.routesaleadd_tbl),
    path("routeedit/",views.routesale_edit),
    path("delrow_f/<id>",views.delete_row_fin),
    path("delrow/<id>",views.delete_row),
    path("saveroutesale/", views.saveroutesale),
    path("savefinancialyear/", views.savefinancialyear),
    path("changepassword/",views.changepassword),
    path("reset_password/",views.reset_password),
    path("companydetails/",views.basicinformation),
    path("update_company/",views.update_company),
    path("update_company_view/",views.update_company_view),
    path("temp/",views.temporary),
    path("dir_det/",views.directordetails),
    path("dir_add/",views.director_det_add),
    path("dir_det_add/",views.director_details_add),
    path("dir_del/<id>",views.director_del),
    path("dir_edit/",views.director_edit),
    path("dir_edit_save/",views.savedirDet),
    path("shareholdershome/",views.shareholdershome),
    path("addshareholder/",views.addshareholder),
    path("editshareholder/<id>",views.editshareholder),
    path('edit_submit_shareholder/', views.edit_submit_shareholder),
    path('submit_shareholder/', views.submit_shareholder),
    path("delshareholder/<id>",views.delshareholder),
    path("licenses/", views.licenses),
    path('licensesadd/', views.licensesaddview),
    path("licensesedit/", views.licensesedit),
    path("delrowlicenses/<id>",views.delete_row_licenses),
    path("savelicenses/", views.savelicences),
    path('licenses_add/',views.licenses_add),
    path("licensesprint/",views.licensesprint),
    path('bank/',views.bank_page),
    path("bank_add/",views.bankadd_tbl),
    # path('bankadd/', views.add_bank),
    path('bankadd/', views.bankadd_page),
    path("delbank1/<id>", views.deletebank),
    path("editbank/",views.bank_edit),
    path("savebankedit/",views.save_bank),
    path("v_det_page/",views.vendor_details_page),
    path("v_edit_page/",views.vendor_edit_page),
    path("v_add_page/",views.vendor_add_page),
    path("vendor_add/",views.vendor_add_tbl),
    path("vendor_del/<id>",views.vendor_delete),
    path('vendor_edit/',views.vendor_edit),
    path('taxmaster/', views.taxmaster_list),
    path('taxmasteraddpage/', views.taxmasteraddview),
    path('taxmasteradd/', views.add_taxmaster),
    path('taxmasteredit/<id>/', views.edit_taxmaster),
    path('deltaxmaster/<id>/', views.delete_taxmaster),
    path('savetaxmasteredit/', views.save_taxmaster),
    path("productcategory/", views.productcategory),
    path("addcategory/", views.addcategory),
    path("savecategory/", views.savecategory),
    path("editcategory/<id>",views.editcategory),
    path("deletecategory/<id>",views.deletecategory),
    path("members_page/",views.members_page),
    path("add_members_page/",views.members_add_page),
    path("add_members/",views.members_add),
    path("member_edit_page/<id>",views.member_edit_page),
    path("member_del_page/<id>",views.member_del_page),
    

    path("product/",views.product),
    path("add_product/",views.prodAdd),
    path("product_add/",views.product_add),
    path("save_product_edit/",views.save_product_edit),
    path("product_edit/<id>",views.product_edit_page),
    path("product_del/<id>",views.product_del_tbl),
    path("take_hsn_code/",views.take_hsn_code,name="take_hsn_code"),
    
    path('process_form/', views.process_form, name='process_form'),

    path("purchase_det_page/",views.purchase_details_page),
    path("purchase_add_page/",views.purchase_add_page),
    path('add_purchase/', views.purchase_add_save),
    path('your-url_products/', views.ajax_view_for_products),
    path('invoice/<id>',views.invoice_page),
    path('purchase_edit/',views.purchase_edit_save),
    path('del_pur_row/<id>',views.del_pur_row),
    path('your-url/', views.ajax_view),
    path('del_purchase/<id>',views.purchase_delete),
    path('edit_purchase/<id>',views.purchase_edit),



    

    path('damaged_prod_page/',views.damaged_products_page),
    path('damaged_prod_add_page/',views.damaged_products_add_page),
    path('damaged_prod_add/',views.damaged_products_add),
    path('damaged_prod_ajax/',views.damaged_prod_ajax),

    path('damaged_product_del/<id>',views.del_damaged_product),
    path('damaged_product_edit_page/<id>',views.edit_damaged_product),

    path('purchase_return_page/',views.purchase_return_page),
    path('purchase_return_edit_page/<id>',views.purchase_return_edit),
    path('return_save/',views.save_return),




    path("sale_home/",views.salehome),
    path("addsale/",views.addsale),
    path('get_customers/', views.get_customers, name='get_customers'),
    path('get-product-details/', views.get_product_details, name='get_product_details'),
    path("savesale/",views.save_sale),
    path('invoice/<id>',views.invoice),
    path('deletesale/<id>',views.delete_sale),
    path('getOldBalance/', views.get_old_balance, name='get_old_balance'),

    


    


   
    



    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

  
