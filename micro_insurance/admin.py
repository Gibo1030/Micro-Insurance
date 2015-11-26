from django.contrib import admin
from micro_insurance.models import Insurance, Underwriter, Branch, Position, User

admin.site.register(Underwriter)
admin.site.register(Branch)
admin.site.register(Insurance)
admin.site.register(Position)
admin.site.register(User)