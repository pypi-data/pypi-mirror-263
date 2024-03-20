from datetime import datetime
from typing import Any, Dict, Union, Optional

import httpx

from .model import HonorInfo, HonorWinOrLooseDetail
from .constant import HEADERS, HONOR_API, HONOR_DETAIL_API


class Honor:
    __data: Dict[str, Optional[Union[HonorInfo, Dict[int, HonorWinOrLooseDetail], datetime]]] = {
        "HonorTotalInfo": None,
        "HonorDetailInfo": {},
        "update_time": datetime.now(),
    }

    def __init__(self, name: str):
        self.name = name

    async def get_honor_info(self) -> Optional[HonorWinOrLooseDetail]:
        return await self._get_honor_info()

    async def _get_honor_info(self) -> Optional[HonorWinOrLooseDetail]:
        time = datetime.now()
        if self._get_attr("HonorTotalInfo") and (time - self._get_attr("update_time")).days < 1:
            return await self._get_honor_win_or_loose_detail()
        honor_data = await self.aiopost(
            HONOR_API, data={"t": time.strftime("%Y-%m-%d"), "openId": "", "accessToken": ""}
        )
        self._set_attr("update_time", time)
        self._set_attr("HonorTotalInfo", HonorInfo.parse_obj(honor_data["data"]["result"]))
        return await self._get_honor_win_or_loose_detail()

    async def _get_honor_win_or_loose_detail(self) -> Optional[HonorWinOrLooseDetail]:
        honor_info: HonorInfo = self._get_attr("HonorTotalInfo")
        id = next((i.id for i in honor_info.rows if i.name == self.name), None)
        if id is None:
            return
        honor_detail: Dict[int, HonorWinOrLooseDetail] = self._get_attr("HonorDetailInfo")
        if id in honor_detail and (honor_detail[id].updateTime == datetime.now().strftime("%Y-%m-%d")):
            return honor_detail[id]
        detail_data = await self.aiopost(
            HONOR_DETAIL_API, data={"openId": "", "accessToken": "", "q": id}
        )
        detail_info = HonorWinOrLooseDetail.parse_obj(detail_data["data"]["cardInfo"])
        self._set_attr("HonorDetailInfo", {**honor_detail, id: detail_info})
        return detail_info

    async def aiopost(self, url: str, data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        async with httpx.AsyncClient(http2=True) as client:
            r = await client.post(url, headers=HEADERS, data=data, **kwargs)
            return r.json()

    def _get_attr(self, attr: str) -> Any:
        return self.__data.get(attr)

    def _set_attr(self, attr: str, value: Any):
        self.__data[attr] = value
