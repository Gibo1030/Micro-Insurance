from django.contrib import admin
from micro_insurance.models import Insurance, Underwriter, Branch, Position, UserProfile, MicroInsuranceCompany

admin.site.register(Underwriter)
admin.site.register(MicroInsuranceCompany)
admin.site.register(Position)
admin.site.register(UserProfile)
admin.site.register(Branch)
admin.site.register(Insurance)
