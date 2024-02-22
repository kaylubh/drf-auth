from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        # read-only for GET, HEAD, and OPTIONS methods
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if authenticated user is user associated with obj for all other methods
        return obj.user == request.user
