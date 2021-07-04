from django.contrib import admin
from .models import UserProfile, SequenceTest, TestHistory

admin.site.register(UserProfile)
admin.site.register(SequenceTest)
admin.site.register(TestHistory)
