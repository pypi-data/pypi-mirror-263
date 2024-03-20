# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdAnchor(Component):
    """An AntdAnchor component.


Keyword arguments:

- id (string; optional)

- affix (boolean; default True)

- align (a value equal to: 'left', 'right'; default 'right')

- bounds (number; default 5)

- className (string | dict; optional)

- clickedLink (dict; optional)

- containerId (string; optional)

- key (string; optional)

- linkDict (optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- offsetTop (number; optional)

- style (dict; optional)

- targetOffset (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdAnchor'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, linkDict=Component.UNDEFINED, align=Component.UNDEFINED, containerId=Component.UNDEFINED, targetOffset=Component.UNDEFINED, affix=Component.UNDEFINED, bounds=Component.UNDEFINED, offsetTop=Component.UNDEFINED, clickedLink=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'affix', 'align', 'bounds', 'className', 'clickedLink', 'containerId', 'key', 'linkDict', 'loading_state', 'offsetTop', 'style', 'targetOffset']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'affix', 'align', 'bounds', 'className', 'clickedLink', 'containerId', 'key', 'linkDict', 'loading_state', 'offsetTop', 'style', 'targetOffset']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdAnchor, self).__init__(**args)
