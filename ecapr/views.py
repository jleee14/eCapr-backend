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
    
    def get_queryset(self):
        user = self.request.user.username
        return Bet.objects.filter(owner__username=user).all()

class BetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [IsOwnerOrReadOnly]