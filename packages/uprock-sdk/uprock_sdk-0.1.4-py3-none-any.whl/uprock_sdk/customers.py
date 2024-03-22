import datetime
import enum
from typing import Optional, Set, List

import httpx
from pydantic import BaseModel, EmailStr, model_validator, Field

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


class BaseLabel(BaseModel):
    name: str
    value: Optional[str] = None

    namespace_id: int = Field(default_factory=lambda: GLOBAL_SETTINGS.NAMESPACE_ID)


class LabelAssignMode(str, enum.Enum):
    DO_NOTHING_ON_CONFLICT = enum.auto()
    REPLACE_ON_CONFLICT = enum.auto()


class LabelAssign(BaseModel):
    labels: List[BaseLabel]
    mode: LabelAssignMode = LabelAssignMode.DO_NOTHING_ON_CONFLICT


class LabelUnassign(BaseModel):
    labels: List[BaseLabel]


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


async def assign_labels(customer_id: int, labels: List[BaseLabel], replace: bool = False) -> CustomerRead:
    response = await CLIENT.post(
        f"/v1/internal/customers/{customer_id}/assign_labels",
        json=LabelAssign(
            labels=labels,
            mode=LabelAssignMode.REPLACE_ON_CONFLICT if replace else LabelAssignMode.DO_NOTHING_ON_CONFLICT,
        ).model_dump(),
    )
    response.raise_for_status()

    raw_customer_data = await response.json()
    return CustomerRead(**raw_customer_data)


async def unassign_labels(customer_id: int, labels: List[BaseLabel]) -> CustomerRead:
    response = await CLIENT.post(
        f"/v1/internal/customers/{customer_id}/unassign_labels", json=LabelUnassign(labels=labels).model_dump()
    )
    response.raise_for_status()

    raw_customer_data = await response.json()
    return CustomerRead(**raw_customer_data)
