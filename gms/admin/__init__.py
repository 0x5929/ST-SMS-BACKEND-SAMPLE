from django.contrib import admin

from .cna import ModelAdminCNARotationConfig, ModelAdminCNAStudentConfig, ModelAdminCNATheoryRecordConfig, ModelAdminCNAClinicalRecordConfig
from ..models.cna import CNARotation, CNAStudent, CNATheoryRecord, CNAClinicalRecord


admin.site.register(CNARotation, ModelAdminCNARotationConfig)
admin.site.register(CNAStudent, ModelAdminCNAStudentConfig)
admin.site.register(CNATheoryRecord, ModelAdminCNATheoryRecordConfig)
admin.site.register(CNAClinicalRecord, ModelAdminCNAClinicalRecordConfig)
