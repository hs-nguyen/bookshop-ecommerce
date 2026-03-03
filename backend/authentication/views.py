from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer, UpdateUserSerializer


class RegisterView(generics.CreateAPIView):
    """View for user registration."""
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    """View for retrieving, updating, and deleting user profile."""
    serializer_class = UpdateUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        """Return the authenticated user."""
        return self.request.user
    
    def get_serializer_class(self):
        """Use different serializers for different methods."""
        if self.request.method == 'GET':
            return UserSerializer
        return UpdateUserSerializer
    
    def destroy(self, request, *args, **kwargs):
        """Delete user account."""
        user = self.get_object()
        user.delete()
        return Response(
            {'message': 'User account deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
