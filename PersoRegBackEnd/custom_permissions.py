from rest_framework import permissions

class SpecialUserPermission(permissions.BasePermission):
	SELECTED_GROUP = 'special'
	def has_permission(self, request, view):
		result = request.user and request.user.groups.filter(name=self.SELECTED_GROUP)
		return result