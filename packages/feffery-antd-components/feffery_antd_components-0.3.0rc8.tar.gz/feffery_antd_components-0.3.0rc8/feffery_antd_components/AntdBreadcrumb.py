# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdBreadcrumb(Component):
    """An AntdBreadcrumb component.


Keyword arguments:

- id (string; optional)

- className (string | dict; optional)

- clickedItem (dict; optional)

    `clickedItem` is a dict with keys:

    - itemKey (string; optional):
        记录点击事件对应子项key值.

    - itemTitle (string; optional)

    - timestamp (number; optional)

- items (list of dicts; optional)

    `items` is a list of dicts with keys:

    - href (string; optional)

    - icon (string; optional)

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional)

    - key (string; optional):
        定义节点唯一key值.

    - menuItems (list of dicts; optional)

        `menuItems` is a list of dicts with keys:

        - disabled (boolean; optional)

        - href (string; optional)

        - icon (string; optional)

        - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional)

        - target (string; optional)

        - title (string; optional)

    - target (string; optional)

    - title (string; optional)

- key (string; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- separator (a list of or a singular dash component, string or number; default '/')

- style (dict; optional)"""
    _children_props = ['separator']
    _base_nodes = ['separator', 'children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdBreadcrumb'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, items=Component.UNDEFINED, separator=Component.UNDEFINED, clickedItem=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'clickedItem', 'items', 'key', 'loading_state', 'separator', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'clickedItem', 'items', 'key', 'loading_state', 'separator', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdBreadcrumb, self).__init__(**args)
