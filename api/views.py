import logging

from django.http import HttpResponse
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

import csv
import io

from .models import Client, Bill, Product, BillProduct
from .serializers import (
    ClientSerializer,
    BillSerializer,
    ProductSerializer,
    BillProductSerializer,
)

logger = logging.getLogger(__name__)

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

jwt_payload_handler = RefreshToken.for_user
jwt_encode_handler = RefreshToken.for_user

class ClientViewSet(viewsets.ModelViewSet):
    logger.warning('Creating a new Client')
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class BillViewSet(viewsets.ModelViewSet):
    logger.warning('Creating a new Bill')
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class ProductViewSet(viewsets.ModelViewSet):
    logger.warning('Creating a new Product')
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BillProductViewSet(viewsets.ModelViewSet):
    logger.warning('Creating a new BillProduct')
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer

    @action(detail=False, methods=['get'])
    def export_csv(self, request):
        logger.warning('Exporting CSV')
        clientes = Client.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="clientes.csv"'
        writer = csv.writer(response)
        writer.writerow(['documento', 'nombres', 'apellidos'])
        for c in clientes:
            writer.writerow([c.documento, c.nombres, c.apellidos])
        return response

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def bulk_create(self, request):
        logger.warning('Bulk creating clients from CSV')
        csv_file = request.FILES['archivo_clientes']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Client.objects.update_or_create(
                documento=column[0], nombres=column[1], apellidos=column[2]
            )
        return Response(status=status.HTTP_201_CREATED)

class AuthViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def login(self, request):
        logger.warning('User login attempt')
        email = request.data.get("email")
        password = request.data.get("password")
        logger.warning('Authenticating......')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            user.token = token
            user.save()
            logger.warning('Autenticated')
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            logger.warning('Invalid login attempt')
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
