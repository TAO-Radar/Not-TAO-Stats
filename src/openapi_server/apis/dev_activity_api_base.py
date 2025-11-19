# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.dev_activity_history_response import DevActivityHistoryResponse
from openapi_server.models.dev_activity_latest_order import DevActivityLatestOrder
from openapi_server.models.dev_activity_latest_response import DevActivityLatestResponse
from openapi_server.security_api import get_token_api_key

class BaseDevActivityApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDevActivityApi.subclasses = BaseDevActivityApi.subclasses + (cls,)
    async def get_dev_activity_history(
        self,
        netuid: Annotated[Optional[StrictStr], Field(description="CSV of netuids (e.g. 1,2,3)")],
        date_start: Annotated[Optional[StrictStr], Field(description="Start date inclusive (YYYY-MM-DD)")],
        date_end: Annotated[Optional[StrictStr], Field(description="End date inclusive (YYYY-MM-DD)")],
    ) -> DevActivityHistoryResponse:
        ...


    async def get_dev_activity_latest(
        self,
        netuid: Optional[StrictStr],
        days_since_last_event_max: Optional[int],
        order: Optional[DevActivityLatestOrder],
        page: Optional[int],
        limit: Optional[int],
    ) -> DevActivityLatestResponse:
        ...
