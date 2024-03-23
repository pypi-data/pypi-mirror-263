# rust_requests
rust_requests is a blazing fast async/await HTTP client for Python written on Rust using reqwests.

* [Works 15% faster than `aiohttp` on average](./benchmarks)
* RAII approach without context managers
* Memory-efficient lazy JSON parser
* Fully-typed even being written on Rust

***

## Overview
```python title="Example"
import asyncio
import datetime

import rust_requests


async def main():
    client = rust_requests.Client(
        user_agent="rust_requests/1.0",
        headers={"X-Foo": "bar"},
        store_cookie=True
    )
    request = rust_requests.Request(
        "GET", "https://google.com/search",
        ),
        query={"q": "hi"},
        headers={"X-Bar": "foo"},
        timeout=datetime.timedelta(seconds=30),
    )
    response = await client.send(request)
    print(response.status)
    data = await response.json()
    data.show()


asyncio.run(main())
```
```

## Installlation
Currently the library is not published to PyPI, so the only way to install it is from GitHub:
```bash
python -m pip install -U https://github.com/cop-discord/rust_requests/archive/main.zip
```
