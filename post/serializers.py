from rest_framework import serializers
from .models import Company, JobPost, JobPostSkillSet

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class JobPostSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()

    def get_company_name(self, obj):
        return obj.company.name

    class Meta:
        model = JobPost
        fields = ["job_type", "company_name", "job_description", "salary"]


class JobPostSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSkillSet
        fields = "__all__"