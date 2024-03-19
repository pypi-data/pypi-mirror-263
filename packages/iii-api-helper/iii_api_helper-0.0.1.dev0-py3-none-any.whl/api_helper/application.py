from logging import Logger
from logging import getLogger
from pathlib import Path

import uvicorn
from fastapi import FastAPI as FastAPIBase
from starlette.middleware import Middleware
from typing_extensions import Any
from typing_extensions import Self

from . import config
from .config import _LoggerBuilder
from .errors import FastAPIError
from .middlewares import LogRequestMiddleware
from .sentry import sentry_init

logger: Logger = getLogger(__name__)


class FastAPI(FastAPIBase):
    def __init__(
        self: Self,
        *,
        base_folder: Path,
        **extra: Any,
    ) -> None:
        """

        Args:
            base_folder:
            **extra:
        """
        if not base_folder.exists():
            msg: str = "The base folder does not exist. Please provide a valid base folder."
            raise FastAPIError(msg)

        options: dict[str, Any] = {}
        for key in extra:
            if key.startswith("logging_"):
                options[key.replace("logging_", "")] = extra.pop(key)

        _logger: _LoggerBuilder = _LoggerBuilder(base_folder, **options)
        _logger.setup()

        self.LOGGING_CONFIG: dict[str, Any] = _logger.config

        middlewares: list[Middleware] = extra.pop("middleware", [])
        middlewares.append(
            Middleware(LogRequestMiddleware),  # type: ignore
        )

        if config.is_debug():
            super().__init__(
                debug=True,
                title=config.get("APP_NAME"),
                middleware=middlewares,
                **extra,
            )
        else:
            # Pop sensitive urls
            docs_url: str = extra.pop("docs_url", "")
            redoc_url: str = extra.pop("redoc_url", "")
            openapi_url: str = extra.pop("openapi_url", "")

            super().__init__(
                title=config.get("APP_NAME"),
                middleware=middlewares,
                docs_url=docs_url,
                redoc_url=redoc_url,
                openapi_url=openapi_url,
                **extra,
            )

    def run(self: Self, host: str, port: int, app: str | None = None, **kwargs: Any) -> None:  # pragma: no cover
        uvicorn.run(
            app or self,
            host=host,
            port=port,
            log_config=self.LOGGING_CONFIG,
            **kwargs,
        )

    setup_sentry = sentry_init
