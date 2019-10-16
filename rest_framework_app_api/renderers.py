"""
Renderers
"""
from rest_framework_app_api.utils import api_dic_response
from rest_framework import renderers
from collections import OrderedDict


class JSONRenderer(renderers.JSONRenderer):
    """
    The `JSONRenderer` exposes a number of methods that you may override if you need highly
    custom rendering control.

    Render a JSON response per the JSON API spec:

    .. code:: json

        {
            "data": [{
                "type": "companies",
                "id": 1,
                "attributes": {
                    "name": "Mozilla",
                    "slug": "mozilla",
                    "date-created": "2014-03-13 16:33:37"
                }
            }, {
                "type": "companies",
                "id": 2,
                ...
            }],
            'code': 200,
            'msg': "success!"
        }

    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        renderer_context = renderer_context or {}
        response = renderer_context.get('response', None)
        exchange = True
        if renderer_context:
            if isinstance(data, dict) and data.get('code') and data.get('msg'):
                exchange = False
        if exchange:
            ret = api_dic_response(data=data, code=response.status_code, msg=response.status_text)
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)

