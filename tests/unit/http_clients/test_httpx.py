from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest

from crawlee import Request
from crawlee.errors import ProxyError
from crawlee.http_clients import HttpxHttpClient
from crawlee.statistics import Statistics

if TYPE_CHECKING:
    from crawlee.proxy_configuration import ProxyInfo


@pytest.fixture
def http_client() -> HttpxHttpClient:
    return HttpxHttpClient()


@pytest.mark.skipif(os.name == 'nt', reason='Skipped on Windows')
async def test_proxy(
    http_client: HttpxHttpClient,
    proxy: ProxyInfo,
    httpbin: str,
) -> None:
    url = f'{httpbin}/status/222'
    request = Request.from_url(url)

    async with Statistics() as statistics:
        result = await http_client.crawl(request, proxy_info=proxy, statistics=statistics)

    assert result.http_response.status_code == 222


@pytest.mark.skipif(os.name == 'nt', reason='Skipped on Windows')
async def test_proxy_disabled(
    http_client: HttpxHttpClient,
    disabled_proxy: ProxyInfo,
    httpbin: str,
) -> None:
    url = f'{httpbin}/status/222'
    request = Request.from_url(url)

    with pytest.raises(ProxyError):
        async with Statistics() as statistics:
            await http_client.crawl(request, proxy_info=disabled_proxy, statistics=statistics)


@pytest.mark.skipif(os.name == 'nt', reason='Skipped on Windows')
async def test_send_request_with_proxy(
    http_client: HttpxHttpClient,
    proxy: ProxyInfo,
    httpbin: str,
) -> None:
    url = f'{httpbin}/status/222'

    response = await http_client.send_request(url, proxy_info=proxy)
    assert response.status_code == 222  # 222 - authentication successful


@pytest.mark.skipif(os.name == 'nt', reason='Skipped on Windows')
async def test_send_request_with_proxy_disabled(
    http_client: HttpxHttpClient,
    disabled_proxy: ProxyInfo,
    httpbin: str,
) -> None:
    url = f'{httpbin}/status/222'

    with pytest.raises(ProxyError):
        await http_client.send_request(url, proxy_info=disabled_proxy)
