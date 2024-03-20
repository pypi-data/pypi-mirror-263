from typing import Union

from msanic.tool import json_encode, json_parse


def pack_msg(
        cmd_type: (int, str),
        cmd_code: (int, str),
        data: Union[dict, list] = None,
        sta_code: int = 0,
        hint='',
        req=None,
        log_fun=None):
    """
    WS打包消息
    """
    if isinstance(cmd_code, int) and isinstance(cmd_type, int):
        if 0 <= cmd_code < 1000:
            return json_encode({'c': cmd_type * 1000 + cmd_code, 'd': data, 's': sta_code, 'e': req, 'm': hint})
    if isinstance(cmd_code, str) or isinstance(cmd_type, str):
        return json_encode({'c': f'{cmd_type}.{cmd_code}', 'd': data, 's': sta_code,  'm': hint, 'e': req})
    err_info = f'打包消息出错,消息结构错误: {cmd_type}, {cmd_code},{data},{sta_code},{sta_code},{req}'
    log_fun(err_info) if callable(log_fun) else print(err_info)
    return None


def parse_msg(data, log_fun=None):
    """Json类消息解析，如有需要可重写"""
    msg = json_parse(data, log_fun=log_fun)
    if (not msg) or (not isinstance(msg, dict)):
        return None, None, None, None
    try:
        cmd = int(msg.get('c'))
    except (ValueError, TypeError, SyntaxError):
        return None, None, None, None
    cmd_type, cmd_code = cmd // 1000, cmd % 1000
    return cmd_type, cmd_code, json_parse(msg.get('d')), msg.get('e')
