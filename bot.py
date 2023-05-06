# import nonebot
# from nonebot import on_request, RequestSession
#
# if __name__ == "__main__":
#     nonebot.init()
#     nonebot.load_builtin_plugins()
#     nonebot.run(host='127.0.0.1', port=8080)

# 将函数注册为群请求处理器
# @on_request('group','add')
# async def _(session: RequestSession):
#     await session.approve()
#     return
# from cqhttp import CQHttp
#
# bot = CQHttp(api_root='http://127.0.0.1:5700/',
#              access_token='',
#              secret='')
#
# @bot.on_request('group','friend')
# async def handle_request(context):
#     return {'approve': True}  # 同意所有加群、加好友请求
#
#
# bot.run(host='127.0.0.1', port=8080)
import nonebot
from nonebot import on_request, RequestSession

#将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
    await session.approve()
    return

# @on_request('group','friend')
# async def handle_request(context):
#     return {'approve': True}

if __name__ == "__main__":
    nonebot.init()
    nonebot.load_builtin_plugins()
    nonebot.run(host='127.0.0.1', port=8080)
