from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from .models import Member
from .serializers import MemberSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET","PUT","DELETE"])
def member(request,pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'GET':
        serializer =MemberSerializer(member)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MemberSerializer(member, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            context = {
                "success": True,
                "message": "Updated successfully",
                "data": serializer.data,
                "code": 200
            }
            return Response(context, status=status.HTTP_200_OK)
        
        return Response(
            {
                "success": False,
                "message": "Validation error",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST

        )
    elif request.method == "DELETE":
        member.delete()
        return Response({
            "message":"deleted",
            "status":True
        })


@api_view(['GET', 'POST'])
def members(request):
    if request.method == "GET":
        members_queryset = Member.objects.all()
        print('here')
        serializer = MemberSerializer(members_queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "success": True,
                "code": 200

            }
            return Response(context)
        else:
            return Response(serializer.errors)

       
    