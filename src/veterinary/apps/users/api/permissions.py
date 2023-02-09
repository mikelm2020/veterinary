from rest_framework.permissions import BasePermission

class IsAssistant(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == "A":
            return True
        return False

class IsVeterinary(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == "V":
            return True
        return False


class IsRecepcionist(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == "R":
            return True
        return False

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == "G":
            return True
        return False

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user