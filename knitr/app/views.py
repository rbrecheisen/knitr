from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Document


class DocumentListView(generics.RetrieveAPIView):

    queryset = Document.objects.all()
    renderer_classes = (TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        return Response(template_name='app/document_list.html')
