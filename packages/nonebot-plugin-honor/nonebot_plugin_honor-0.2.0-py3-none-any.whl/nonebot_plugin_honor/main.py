from nonebot.params import CommandArg
from nonebot import logger, require, on_command
from nonebot.adapters import Bot, Event, Message

from .draw import draw
from .utils import Honor

require("nonebot_plugin_saa")
from nonebot_plugin_saa import Text, Image, MessageFactory  # noqa: E402

honor = on_command("honor", priority=5, block=True, aliases={"查胜率", "英雄胜率"})


@honor.handle()
async def _(ev: Event, bot: Bot, arg: Message = CommandArg()):  # noqa: B008
    honor_name = arg.extract_plain_text().strip()
    wrong_msg_builder = MessageFactory([Text("数据获取失败，请输入英雄全名")])
    honor_info = Honor(honor_name)
    try:
        info = await honor_info.get_honor_info()
        if info:
            msg = MessageFactory(
                [
                    Text(f"{honor_name}的胜率如下，数据来自苏苏的荣耀助手\n更新时间：{info.updateTime}"),
                    Image(draw(info, honor_name)),
                ]
            )
            await msg.send()
        else:
            await wrong_msg_builder.send()
    except Exception as e:
        logger.opt(colors=True).exception(f"获取荣耀胜率失败：{e}")
        await wrong_msg_builder.send()
    finally:
        await honor.finish()
