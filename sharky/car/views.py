from django.shortcuts import render

from rest_framework import viewsets
# this viewset combine the listview & detailview
from rest_framework.decorators import action, renderer_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers

from car.models import Car
from car.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly]
    # Do not know how does this work

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        car = self.get_object()
        return Response(car.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
