from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.id

    
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own feet items"""
    
    def has_object_permission(self, request, view, obj):
        """Check to see if user is trying to update their own feed item/status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id