from django.contrib import admin

from .cna import ModelAdminCNARotationConfig, ModelAdminCNAStudentConfig, ModelAdminCNATheoryRecordConfig, ModelAdminCNAClinicalRecordConfig
from .hha import ModelAdminHHARotationConfig, ModelAdminHHAStudentConfig, ModelAdminHHATheoryRecordConfig, ModelAdminHHAClinicalRecordConfig

from ..models.cna import CNARotation, CNAStudent, CNATheoryRecord, CNAClinicalRecord
from ..models.hha import HHARotation, HHAStudent, HHATheoryRecord, HHAClinicalRecord


# CNA GMS
admin.site.register(CNARotation, ModelAdminCNARotationConfig)
admin.site.register(CNAStudent, ModelAdminCNAStudentConfig)
admin.site.register(CNATheoryRecord, ModelAdminCNATheoryRecordConfig)
admin.site.register(CNAClinicalRecord, ModelAdminCNAClinicalRecordConfig)

# HHA GMS
admin.site.register(HHARotation, ModelAdminHHARotationConfig)
admin.site.register(HHAStudent, ModelAdminHHAStudentConfig)
admin.site.register(HHATheoryRecord, ModelAdminHHATheoryRecordConfig)
admin.site.register(HHAClinicalRecord, ModelAdminHHAClinicalRecordConfig)
