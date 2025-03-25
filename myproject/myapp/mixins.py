from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

class JsonResponseMixin:
    def render_json(self, context):
        return JsonResponse(context)

class ObjectMixin:
    model = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

class UserPermissionMixin:
    def check_permission(self, user):
        if not user.is_authenticated or not user.has_perm('app.view_model'):
            raise PermissionDenied

class DateTimeMixin:
    def get_current_datetime(self):
        from datetime import datetime
        return datetime.now()

class SuccessMessageMixin:
    success_message = "Operation completed successfully."

    def get_success_message(self):
        return self.success_message

class PaginateMixin:
    paginate_by = 10

    def get_paginate_by(self):
        return self.paginate_by

class FilterMixin:
    def apply_filters(self, queryset, filters):
        return queryset.filter(**filters)

class CustomContextMixin:
    def get_custom_context(self):
        return {"custom_key": "custom_value"}

class RedirectMixin:
    def get_redirect_url(self):
        return "/somewhere/"

class FileUploadMixin:
    def handle_uploaded_file(self, file):
        with open(f'uploads/{file.name}', 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return f'uploads/{file.name}'
