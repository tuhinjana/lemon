from django.db.transaction import atomic
from django.http import Http404

from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import OrderSerializer

# Create your views here.


class OrderView(GenericAPIView):
    serializer_class = OrderSerializer

    @atomic
    def post(self, request, account_uuid):
        try:
            account_obj = self.serializer_class.validate_account(account_uuid)
        except Exception:
            raise Http404("No Account uuid matches the given uuid.")
        print(request.data)
        #request.data["account"] = account_obj
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #serializer.account = account_obj
        serializer.save(account=account_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

