from django.template import Library
from django.conf import settings
import copy

register = Library()


@register.inclusion_tag('menu.html')
def unicom_menu(request):
    role = request.unicom_role

    user_menu_list = copy.deepcopy(settings.UNICOM_MENU[role])
    print(user_menu_list)
    for row in user_menu_list:
        if request.path_info.startswith(row['url']):
            row['class'] = "active"

    return {'menu_list': user_menu_list}
