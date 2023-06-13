from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, HttpResponse
from django.conf import settings


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 无需登录
        if request.path_info in ["/login/", '/logout/']:
            return

        # 获取session值
        user_info = request.session.get("user_info")

        # 非空已登录
        if user_info:
            request.unicom_userid = user_info['id']
            request.unicom_username = user_info['username']
            request.unicom_role = user_info['role']
            return

        # 无值
        return redirect('/login/')

    def process_view(self, request, view_func, args, kwargs):
        if request.path_info in ["/login/", '/logout/']:
            return

        role = request.unicom_role

        user_permission_list = settings.UNICOM_PERMISSION[role]

        if request.resolver_match.url_name in user_permission_list:
            return

        return HttpResponse("无权访问")
