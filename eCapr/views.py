from .models import Bet
from rest_framework import generics, permissions
from .serializers import BetSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class BetList(generics.ListCreateAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [IsOwnerOrReadOnly]