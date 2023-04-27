from rest_framework.permissions import BasePermission


class IsSuperAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsAdminUser(BasePermission):
    # def has_permission(self, request, view):
    #     UserGroup = User.groups.through
    #     return UserGroup.objects.filter(user=request.user,group__name="Admin").exits()

    def has_permission(self, request, view):
        user_groups = request.user.groups.all().values_list('name',flat=True)
        return "Admin" in user_groups


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        user_groups = request.user.groups.all().values_list('name', flat=True)
        return "Student" in user_groups


class IsTutor(BasePermission):
    def has_permission(self, request, view):
        user_groups = request.user.groups.all().values_list('name', flat=True)
        return "Tutor" in user_groups




