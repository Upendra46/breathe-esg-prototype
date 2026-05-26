from django.contrib import admin
from .models import *

admin.site.register(Tenant)
admin.site.register(DataSource)
admin.site.register(RawRecord)
admin.site.register(NormalizedActivity)
admin.site.register(ReviewDecision)
admin.site.register(AuditLog)
