import datetime
from typing import Optional, Set

import httpx
from pydantic import BaseModel, EmailStr, model_validator

from uprock_sdk import GLOBAL_SETTINGS

CLIENT = httpx.AsyncClient(base_url=GLOBAL_SETTINGS.CORE_API_URL)


class BaseCustomer(BaseModel):
    telegram_id: Optional[int] = None
    email: Optional[EmailStr] = None
    email_verified: Optional[bool] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None

    labels: Optional[Set[str]] = None
    namespaces: Optional[Set[int]] = None

    @model_validator(mode="after")
    def telegram_id_or_email_required(self):
        if not self.telegram_id and not self.email:
            raise ValueError("Either telegram_id or email is required")
        return self


class CustomerRead(BaseCustomer):
    id: int

    updated_at: datetime.datetime
    created_at: datetime.datetime


async def create(dto: BaseCustomer) -> CustomerRead:
    customer_data = dto.model_dump()

    if GLOBAL_SETTINGS.NAMESPACE_ID is not None:
        if "namespaces" not in customer_data:
            customer_data["namespaces"] = [GLOBAL_SETTINGS.NAMESPACE_ID]
        else:
            customer_data["namespaces"].append(GLOBAL_SETTINGS.NAMESPACE_ID)

    response = await CLIENT.post("/v1/internal/customers", json=customer_data)
    response.raise_for_status()

    raw_customer_data = await response.json()
    return CustomerRead(**raw_customer_data)
