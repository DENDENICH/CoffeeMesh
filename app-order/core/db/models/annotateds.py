import uuid

from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import mapped_column


def generate_uuid():
    return str(uuid.uuid4())


intpk = Annotated[
    str, 
    mapped_column(
        String,
        primary_key=True,
        default=generate_uuid   
    )
]
