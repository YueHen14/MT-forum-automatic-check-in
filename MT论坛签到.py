import requests
 
def send_signin_request(base_url, plugin_path, query_params, custom_headers=None, custom_cookies=None):
    """
    发送签到请求
 
    :param base_url: 基础URL,例如 'https://bbs.binmt.cc'
    :param plugin_path: 插件路径,例如 '/plugin.php'
    :param query_params: 查询参数,例如 {'id': 'k_misign:sign', 'operation': 'qiandao', 'formhash': 'dbae5059', 'format': 'empty', 'inajax': '1', 'ajaxtarget': ''}
    :param custom_headers: 自定义请求头,字典格式
    :param custom_cookies: 自定义Cookie,字典格式
    :return: 响应对象
    """
    url = f"{base_url}{plugin_path}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": f"{base_url}/k_misign-sign.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Dnt": "1",
        "Sec-Gpc": "1",
        "Priority": "u=1, i",
        "Connection": "close",
    }
    if custom_headers:
        headers.update(custom_headers)
     
    response = requests.get(url, headers=headers, params=query_params, cookies=custom_cookies)
    return response
 
# 使用示例
base_url = "https://bbs.binmt.cc"
plugin_path = "/plugin.php"
query_params = {
    "id": "k_misign:sign",
    "operation": "qiandao",
    "formhash": "c0b96911",
    "format": "empty",
    "inajax": "1",
    "ajaxtarget": ""
}
custom_cookies = {
    "cQWy_2132_saltkey": "dZVcBcv1",
    "cQWy_2132_auth": "4b30X5yexdH5WvsJDuOOGA9y5Fa4fIYzaZ6%2BuwPta56KxmW1LymXcriMKgMd6GduAti8FY4FLnwhXIiyX8u5PilmB38"
}
 
response = send_signin_request(base_url, plugin_path, query_params, custom_cookies=custom_cookies)
 
# 输出响应
print(response.status_code)
print(response.text)
input("输入按键退出命令")