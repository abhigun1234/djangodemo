from django.http import HttpResponse
from rest_framework.decorators import api_view




@api_view(['GET'])
def home(request):
    from django.shortcuts import render_to_response
    return render_to_response('index.html')


@api_view(['GET'])
def getStudentDetails(request):

    return HttpResponse('This page shows a list of most recent posts.')



@api_view(['GET'])
def mypage(request):

    return HttpResponse('show me the new page')

