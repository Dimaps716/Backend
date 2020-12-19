from django.shortcuts import render
from django.http import JsonResponse
from students.models import studen, technologi, project, courses, milestone, info
from rest_framework.decorators import api_view
from rest_framework.response import Response


#  create your views here.
from .models import studen, technologi, project, courses, milestone
from students.serializers import studenSerializer, technologiSerializer, projectSerializer, coursesSerializer, milestoneSerializer, informationSerializer

# list all 
@api_view(['GET'])
def studentsList(request):
    studens = studen.objects.all()
    serializer = studenSerializer(studens, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tecnologieList(request):
    technologies = technologi.objects.all()
    serializer = technologiSerializer(technologies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def projeList(request):
    projects = project.objects.all()
    serializer = projectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def milestonsList(request):
    milesto = milestons.objects.all()
    serializer = milestonSerializer(milesto, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def coursList(request):
    course = courses.objects.all()
    serializer = coursesSerializer(course, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def infoList(request):
    informat = information.objects.all()
    serializer = informationSerializer(informat, many=True)
    return Response(serializer.data)



# lits detail

@api_view(['GET'])
def studensDetail(request, pk):
    studens = studen.objects.get(id=pk)
    serializer = studenSerializer(studens, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def tecnologieDetail(request, pk):
    technologies = technologi.objects.get(id=pk)
    serializer = technologiSerializer(technologies, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def projetDetail(request, pk):
    projects = project.objects.get(id=pk)
    serializer = projectSerializer(projects, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def milestonsDetail(request, pk):
    milesto = milestons.objects.get(id=pk)
    serializer = milestonsSerializer(milesto, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def coursDetail(request, pk):
    course = courses.objects.get(id=pk)
    serializer = coursesSerializer(course, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def infoList(request, pk):
    informat = information.objects.get(id=pk)
    serializer = informationSerializer(informat, many=True)
    return Response(serializer.data)

# create 

@api_view(['POST'])
def studensCreate(request):
    serializer = studensSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def tecnologieCreate(request):
    serializer = technologiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def projeListCreate(request):
    serializer = projectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def milestonsCreate(request):
    serializer = milestonsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def coursCreate(request):
    serializer = coursesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def infoCreate(request):
    serializer = informationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update 
@api_view(['POST'])
def studensUpdate(request, pk):
    studens = studen.objects.get(id=pk)
    serializer = studenSerializer(instance=studens, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def tecnologieUpdate(request, pk):
    technologies = technologi.objects.get(id=pk)
    serializer =technologiSerializer (instance=technologies, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def studensUpdate(request, pk):
    studens = studen.objects.get(id=pk)
    serializer = studenSerializer(instance=studens, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def projeUpdate(request, pk):
    projects = project.objects.get(id=pk)
    serializer = projectSerializer(instance=projects, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def milestonsUpdate(request, pk):
    milesto = milestons.objects.get(id=pk)
    serializer = milestonSerializer(instance=milesto, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def coursUpdate(request, pk):
    course = courses.objects.get(id=pk)
    serializer = coursesSerializer(instance=course, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def infoCreate(request, pk):
    informat = information.objects.get(id=pk)
    serializer = informationSerializer(instance=informat, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete 
@api_view(['DELETE'])
def studentsDelete(request, pk):
    tudens = studen.objects.get(id=pk)
    studens.delete()

    return Response('studens succsesfully delete!')

@api_view(['DELETE'])
def tecnologieDelete(request, pk):
    technologies = technologi.objects.get(id=pk)
    technologies.delete()

    return Response('technologies succsesfully delete!')

@api_view(['DELETE'])
def projeDelete(request, pk):
    projects = project.objects.get(id=pk)
    projects.delete()

    return Response('projects succsesfully delete!')

@api_view(['DELETE'])
def milestonsDelete(request, pk):
    milesto = milestons.objects.get(id=pk)
    milesto.delete()

    return Response('milestons succsesfully delete!')

@api_view(['DELETE'])
def coursDelete(request, pk):
    course = courses.objects.get(id=pk)
    courses.delete()

    return Response('courses succsesfully delete!')