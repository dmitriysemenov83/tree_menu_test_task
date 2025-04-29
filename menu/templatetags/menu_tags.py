from django import template

from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path  # Получаем текущий URL

    # Получаем все пункты меню за один запрос
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': []}

    menu_items = MenuItem.objects.filter(menu=menu).select_related('parent').order_by('id')

    # Строим дерево в памяти
    items_dict = {item.id: {'item': item, 'children': [], 'open': False, 'active': False} for item in menu_items}

    root_items = []

    for item in menu_items:
        if item.parent_id:
            items_dict[item.parent_id]['children'].append(items_dict[item.id])
        else:
            root_items.append(items_dict[item.id])

    # Ищем активный элемент
    active_item = None
    for item in items_dict.values():
        if item['item'].get_absolute_url() == current_path:
            item['active'] = True
            active_item = item
            break

    # Помечаем всех родителей активного элемента как открытые
    def mark_open(item):
        parent = item['item'].parent
        if parent and parent.id in items_dict:
            items_dict[parent.id]['open'] = True
            mark_open(items_dict[parent.id])

    if active_item:
        mark_open(active_item)

    return {
        'menu_tree': root_items,
    }
