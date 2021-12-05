from django.shortcuts import render
from django.http import HttpResponse

# lets get some dummy data

projectsList = [
	{
		'id': '1',
		'title': 'Lorem Ipsum',
		'description': 'Lorem ipsum dolor sit amet precurorum nihil sit'
	},

	{
		'id': '2',
		'title': 'Dolor Sit',
		'description': 'Lorem ipsum dolor sit amet precurorum nihil sit'
	},
	{
		'id': '3',
		'title': 'Ament Nomet',
		'description': 'Lorem ipsum dolor sit amet precurorum nihil sit'
	},
	{
		'id': '4',
		'title': 'Perpetuum Lorems',
		'description': 'Lorem ipsum dolor sit amet precurorum nihil sit'
	},
]

def projects(request):
    msg = 'Hello, You are viewing the Projects App Home Page'
    context = {'message':msg, 'projects':projectsList}
    return render(request, 'projects/projects.html', context )

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project':projectObj})

