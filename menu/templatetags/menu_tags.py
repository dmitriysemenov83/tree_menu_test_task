from django import template

from menu.models import MenuItem, Menu

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {'menu_tree': []}

    items = list(MenuItem.objects.filter(menu=menu).select_related('parent'))
    nodes = {item.id: {"item": item, "children": [], "open": False, "active": False} for item in items}

    root_nodes = []

    # построим дерево
    for node in nodes.values():
        item = node['item']
        if item.parent_id:
            nodes[item.parent_id]["children"].append(node)
        else:
            root_nodes.append(node)

    # найдём активный путь
    for node in nodes.values():
        if node['item'].get_absolute_url() == current_path:
            node['active'] = True
            # раскрыть родителей
            parent = node['item'].parent
            while parent:
                parent_node = nodes.get(parent.id)
                if parent_node:
                    parent_node['open'] = True
                parent = parent.parent

    return {'menu_tree': root_nodes}
