from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)

from .serializers import CompanySerializer, JobPostSerializer, JobPostSkillSetSerializer

from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)
        skill_list = JobPostSkillSet.objects.filter(
            Q(skill_set=skills) | Q(skill_set=skills)
        )
        return Response(JobPostSkillSetSerializer(skill_list, many=True).data, status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        jobtype_serializer = JobPostSerializer(data=request.data)

        if jobtype_serializer.is_valid():
            job_type = int(request.data.get("job_type", None))
            company_name = request.data.get("company_name", None)

            if job_type is not None:
                JobPostSerializer.save()
                return Response({"message":"저장완료!"}, status=status.HTTP_200_OK)

                return Response(JobPostSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


        return Response(status=status.HTTP_200_OK)

