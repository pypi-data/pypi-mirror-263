# III API base

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

## Usage

```python
from pathlib import Path

from api_helper import FastAPI, success_response

app: FastAPI = FastAPI(base_folder=Path(__file__).parent)
# Optional to setup sentry
app.setup_sentry("sentry_dsn")


@app.get("/")
def home():
    return success_response("Hello, World!")


# Run the app
app.run("127.0.0.1", 5000)
```

## Build backend

hatch

- [version](https://hatch.pypa.io/1.9/version/)

```shell
hatch env create
hatch build
hatch publish -r test
```
