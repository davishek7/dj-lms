from django.contrib import admin
from .models import User,Student,EmailVerificationToken

admin.site.register(User)
admin.site.register(Student)
admin.site.register(EmailVerificationToken)

