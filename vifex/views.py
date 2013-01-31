from pyramid.view import view_config
from pyramid.response import Response
from datetime import datetime

@view_config(route_name='home', renderer='templates/main.pt')
def my_view(request):
    return {'project': 'Vifex', 'year' : datetime.now().year}

@view_config(route_name='content')
def content(request):
    return Response("here it comes")
