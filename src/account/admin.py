from django.contrib import admin
from account.models.account import User
from account.models.otp import OTPVerification
from account.models.verification import VerifyUser

admin.site.register(User)
admin.site.register(OTPVerification)
admin.site.register(VerifyUser)