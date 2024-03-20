# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdIcon(Component):
    """An AntdIcon component.


Keyword arguments:

- id (string; optional):
    Component id.

- className (string | dict; optional):
    CSS class name.

- debounceWait (number; default 0):
    Configures the debounce wait time (in milliseconds) for value
    change updates, default is 0.

- icon (string; optional):
    Specifies the icon type.

- key (string; optional):
    A unique identifier key used for refreshing assistance.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- nClicks (number; default 0):
    Records the number of times the button has been clicked since
    rendering, default is 0.

- style (dict; optional):
    Custom CSS styles."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdIcon'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, icon=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, nClicks=Component.UNDEFINED, debounceWait=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'debounceWait', 'icon', 'key', 'loading_state', 'nClicks', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'debounceWait', 'icon', 'key', 'loading_state', 'nClicks', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AntdIcon, self).__init__(**args)
