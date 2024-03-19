# III API base

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

## Usage

### Config

> The later config will override the previous one.

This table shows the predefined environment variables.

| Keyword  | Description                             |
|----------|-----------------------------------------|
| `DEBUG`  | To set the logging as `DEBUG` state.    |
| `RELOAD` | To auto reload the FastAPI application. |

```python
from pathlib import Path

from api_helper.config import load_config

# Load config
load_config(Path(__file__).parent / ".env")

# Load default config in the directory (.env)
load_config(Path(__file__).parent)
```

### FastAPI example

> To config the FastAPI by env, read the [Config](#config) section.

```python
from pathlib import Path

from api_helper import FastAPI, success_response

app: FastAPI = FastAPI(base_folder=Path(__file__).parent)
# Optional to setup sentry
app.setup_sentry("sentry_dsn")


@app.get("/")
def home():
    return success_response("Hello, World!")


# Start the app and enjoy
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
