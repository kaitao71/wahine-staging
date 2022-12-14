from django.urls import path, include

from django.contrib import admin
from backend.views import *

admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
	path("formset/",create_bank_model_form,name="formset"),
	path("",index,name="index"),
	path("joinnow",joinnow,name="joinnow"),
	path("whoweare/",whoweare,name="whoweare"),
	path("contact/",contactus,name="contactus"),
	path("terms-of-service/",terms_of_service,name="terms-of-service"),
	path("privacy-policy/",privacy_policy,name="privacy-policy"),
	path("return-refund-policy/",return_refund_policy,name="return-refund-policy"),
	path("profile/",profile,name="profile"),
	path("signup/",signup,name="signup"),
	path("login/",login_view,name="login"),
	path("plan/",selectplan,name="plan"),
	path("dashboard/",dashboard,name="dashboard"),
	path("logout/",logout_view,name="logout"),
	## Onboarding Assets 
	path("assets/overview",assets_overview,name="assets_overview"),
	path("assets/bank",bank_account_form,name="bank_account_form"),
	path("assets/epf",epf_socso_form,name="epf_socso_form"),
	path("assets/insurance/",insurance_form,name="insurance_form"),
	path("assets/investment/",investment_form,name="investment_form"),
	path("assets/property/",property_form,name="property_form"),
	path("assets/vehicles/",vehicles_form,name="vehicles_form"),
	path("assets/others/",asset_others_form,name="asset_others_form"),
	
	## Editing Assets
	path("assets/bank/edit/<uuid>",edit_bank_account_form,name="edit_bank_account_form"),
	path("assets/epf/edit/<uuid>",edit_epf_socso_form,name="edit_epf_socso_form"),
	path("assets/insurance/edit/<uuid>",edit_insurance_form,name="edit_insurance_form"),
	path("assets/investment/edit/<uuid>",edit_investment_form,name="edit_investment_form"),
	path("assets/property/edit/<uuid>",edit_property_form,name="edit_property_form"),
	path("assets/vehicles/edit/<uuid>",edit_vehicle_form,name="edit_vehicles_form"),
	path("assets/others/edit/<uuid>",edit_asset_others_form,name="edit_asset_others_form"),
	## Onboarding Liabilities
	path("liabilities/overview",liabilities_overview,name="liabilities_overview"),
	path("liabilities/card/",liability_credit_card_form,name="credit_card_form"),
	path("liabilities/personal/",personal_loan_form,name="personal_loan_form"),
	path("liabilities/vehicles/",vehicles_loan_form,name="vehicles_loan_form"),
	path("liabilities/property/",property_loan_form,name="property_loan_form"),
	path("liabilities/others/",liabilities_others_form,name="liabilities_others_form"),

	## Editing Liabilities
	path("liabilities/card/edit/<uuid>",edit_liability_credit_card_form,name="edit_credit_card_form"),
	path("liabilities/personal/edit/<uuid>",edit_personal_loan_form,name="edit_personal_loan_form"),
	path("liabilities/vehicles/edit/<uuid>",edit_vehicle_loan_form,name="edit_vehicles_loan_form"),
	path("liabilities/property/edit/<uuid>",edit_property_loan_form,name="edit_property_loan_form"),
	path("liabilities/others/edit/<uuid>",edit_liabilities_others_form,name="edit_liabilities_others_form"),

	## Onboarding Trigger Events
	path("triggers/notifier/",notifier_list_form,name="notifier_list_form"),
	path("triggers/accesslist/",access_list_form,name="access_list_form"),
 	
 	path("dashboard/", dashboard,name="dashboard"),
 	path("admin/", admin.site.urls),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
