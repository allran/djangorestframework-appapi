from rest_framework.settings import api_settings


def api_dic_response(data=None, code=None, msg=None, kwargs=None):
    if data is None:
        data = {}
    data_obj = {
        'data': data,
        'code': code,
        'msg': msg
    }
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        data_obj.update(kwargs)
    return data_obj


def api_dic_list(list_data=None, total_count=0, total_pages=0, kwargs=None):
    if list_data is None:
        list_data = []

    if total_pages is 0:
        page_size = api_settings.PAGE_SIZE
        total_pages = (total_count + page_size - 1) / page_size
    data_dict = {
        'list': list_data,
        'total_count': total_count,
        'total_pages': total_pages
    }
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        data_dict.update(kwargs)
    return data_dict
