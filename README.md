from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from fbvApp.serializers import StudentSerializer

from fbvApp.models import Student
s=Student(id='15', name='kang', score=98)
s.save()

serializer=StudentSerializer(s)
serializer.data
{'id': 15, 'name': 'kang', 'score': '98.000'}

content=JSONRenderer().render(serializer.data)
>>> content
b'{"id":15,"name":"kang","score":"98.000"}'
