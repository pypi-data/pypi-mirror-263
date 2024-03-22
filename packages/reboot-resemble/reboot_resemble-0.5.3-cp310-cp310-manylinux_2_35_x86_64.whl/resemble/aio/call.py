from dataclasses import dataclass
from resemble.aio.types import GrpcMetadata
from typing import Optional


@dataclass(kw_only=True, frozen=True)
class Options:
    """Options for RPCs."""
    idempotency_key: Optional[str] = None
    idempotency_alias: Optional[str] = None
    metadata: Optional[GrpcMetadata] = None
    bearer_token: Optional[str] = None

    def __post_init__(self):
        if (
            self.idempotency_key is not None and
            self.idempotency_alias is not None
        ):
            raise TypeError(
                "options: only one of 'idempotency_key' or 'idempotency_alias' "
                "should be set"
            )
