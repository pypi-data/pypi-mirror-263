# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdForm(Component):
    """An AntdForm component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the tab - will only be displayed if this tab is
    selected.

- id (string; optional)

- className (string | dict; optional)

- colon (boolean; default True)

- formValidateStatus (boolean; optional):
    监听搜集内部表单输入类组件的校验结果.

- helps (dict with strings as keys and values of type a list of or a singular dash component, string or number; optional):
    统一设置内部各AntdFormItem的help值，键为对应AntdFormItem的label值
    优先级低于各AntdFormItem的help值.

- key (string; optional)

- labelAlign (a value equal to: 'left', 'right'; default 'right')

- labelCol (dict; optional)

    `labelCol` is a dict with keys:

    - flex (string | number; optional)

    - offset (number; optional)

    - span (number; optional)

- labelWrap (boolean; default False)

- layout (a value equal to: 'horizontal', 'vertical', 'inline'; default 'horizontal')

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- resetForm (boolean; default False):
    控制参数，用于重置表单项校验状态（不能重置表单项包裹的组件的值，需要通过回调重置表单项包裹的组件的值），回调设置为True后会自动变为False.

- resetFormClicks (number; default 0):
    辅助监听表单重置参数.

- style (dict; optional)

- submitForm (boolean; default False):
    控制参数，用于提交表单时手动搜集表单的校验结果，回调设置为True后会自动变为False.

- submitFormClicks (number; default 0):
    辅助监听表单提交参数.

- validateStatuses (dict with strings as keys and values of type a value equal to: 'success', 'warning', 'error', 'validating'; optional):
    统一设置内部各AntdFormItem的validateStatus值，键为对应AntdFormItem的label值
    优先级低于各AntdFormItem的validateStatus值.

- values (dict; optional):
    监听搜集内部表单输入类组件的输入值变化情况.

- wrapperCol (dict; optional)

    `wrapperCol` is a dict with keys:

    - flex (string | number; optional)

    - offset (number; optional)

    - span (number; optional)"""
    _children_props = ['helps{}']
    _base_nodes = ['children']
    _namespace = 'feffery_antd_components'
    _type = 'AntdForm'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, layout=Component.UNDEFINED, labelCol=Component.UNDEFINED, wrapperCol=Component.UNDEFINED, colon=Component.UNDEFINED, labelAlign=Component.UNDEFINED, labelWrap=Component.UNDEFINED, values=Component.UNDEFINED, formValidateStatus=Component.UNDEFINED, submitForm=Component.UNDEFINED, submitFormClicks=Component.UNDEFINED, resetForm=Component.UNDEFINED, resetFormClicks=Component.UNDEFINED, validateStatuses=Component.UNDEFINED, helps=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'colon', 'formValidateStatus', 'helps', 'key', 'labelAlign', 'labelCol', 'labelWrap', 'layout', 'loading_state', 'resetForm', 'resetFormClicks', 'style', 'submitForm', 'submitFormClicks', 'validateStatuses', 'values', 'wrapperCol']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'colon', 'formValidateStatus', 'helps', 'key', 'labelAlign', 'labelCol', 'labelWrap', 'layout', 'loading_state', 'resetForm', 'resetFormClicks', 'style', 'submitForm', 'submitFormClicks', 'validateStatuses', 'values', 'wrapperCol']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(AntdForm, self).__init__(children=children, **args)
