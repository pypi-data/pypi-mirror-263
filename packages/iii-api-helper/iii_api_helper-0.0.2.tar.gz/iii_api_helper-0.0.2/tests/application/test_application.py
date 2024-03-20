from pathlib import Path

import pytest

from api_helper import FastAPI
from api_helper.errors import FastAPIError


def test_fastapi_basefolder_not_exist() -> None:
    with pytest.raises(FastAPIError) as error:
        FastAPI(base_folder=Path("not_exist"))

    assert error.match("^The base folder does not exist.*$")
