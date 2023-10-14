from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Company,Employee
from .serializers import CompanySerializers,EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        print('Get Primary Key ', pk, " f Company")

        try:
            company = Company.objects.get(pk=pk)
            emp = Employee.objects.filter(company=company)

            if len(emp) == 0:
                return Response({'Message':'Company Has No Employee!!'})

            else:
                emp_serializer = EmployeeSerializers(emp, many=True, context={'request': request})
                return Response(emp_serializer.data)

        except Exception as e:
            print(e)
            return Response(
                {'Error Message': 'Company Does Not Exist!!'}
            )

        pass

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers