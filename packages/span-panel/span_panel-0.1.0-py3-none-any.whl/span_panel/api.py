from __future__ import annotations

import logging
from typing import Any, TypeVar, cast

import aiohttp
from aiohttp import client_exceptions
import orjson
from pydantic import BaseModel
from yarl import URL

from span_panel.client import models as d
from span_panel.exceptions import BadRequestError, NotAuthorizedError, SpanError

_LOGGER = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class SpanClient:
    """SPAN Panel API Client."""

    _host: str
    _url: URL
    _token: str | None
    _headers: dict[str, str] | None
    _session: aiohttp.ClientSession | None

    def __init__(
        self,
        *,
        host: str,
        token: str | None = None,
        session: aiohttp.ClientSession | None = None,
    ) -> None:
        self._host = host
        self._url = URL(f"{host}/api/v1")
        self._token = token
        self._session = session
        self._headers = None
        if self._token:
            self._headers = {
                "Authorization": f"Bearer {self._token}",
            }

    async def get_session(self) -> aiohttp.ClientSession:
        """Gets or creates current client session"""

        if self._session is None or self._session.closed:
            if self._session is not None and self._session.closed:
                _LOGGER.debug("Session was closed, creating a new one")
            # need unsafe to access httponly cookies
            self._session = aiohttp.ClientSession(
                cookie_jar=aiohttp.CookieJar(unsafe=True),
            )

        return self._session

    async def close_session(self) -> None:
        """Closing and delets client session"""

        if self._session is not None:
            await self._session.close()
            self._session = None

    async def request(
        self,
        method: str,
        url: str,
        *,
        raise_exception: bool = True,
        **kwargs: Any,
    ) -> aiohttp.ClientResponse:
        """Make a request to SPAN Panel.

        Response is _not_ closed and must still be closed and finalized.
        """

        request_url = self._url.joinpath(url.lstrip("/"))
        headers = kwargs.get("headers") or self._headers
        _LOGGER.warning("Request url: %s", request_url)
        session = await self.get_session()

        for attempt in range(2):
            try:
                req_context = session.request(
                    method,
                    request_url,
                    headers=headers,
                    **kwargs,
                )
                response = await req_context.__aenter__()  # noqa: PLC2801

                if response.status != 200 and raise_exception:
                    text = await response.text()
                    if response.status in {401, 403}:
                        raise NotAuthorizedError(text)
                    if response.status >= 400 and response.status < 500:
                        raise BadRequestError(text)
                    raise SpanError(text)

                return response
            except aiohttp.ServerDisconnectedError as err:
                # If the server disconnected, try again
                # since HTTP/1.1 allows the server to disconnect
                # at any time
                if attempt == 0:
                    continue
                raise SpanError(
                    f"Error requesting data from {self._host}: {err}",
                ) from err
            except client_exceptions.ClientError as err:
                raise SpanError(
                    f"Error requesting data from {self._host}: {err}",
                ) from err

        # should never happen
        raise SpanError(f"Error requesting data from {self._host}")

    async def api_request_raw(
        self,
        url: str,
        *,
        method: str = "get",
        raise_exception: bool = True,
        **kwargs: Any,
    ) -> bytes | None:
        """Get API response from SPAN Panel."""

        response = await self.request(
            method,
            url,
            raise_exception=raise_exception,
            **kwargs,
        )
        try:
            data: bytes | None = await response.read()
            response.release()
            return data
        except Exception:
            # make sure response is released
            response.release()
            # re-raise exception
            raise

    async def api_request_json(
        self,
        url: str,
        *,
        method: str = "get",
        raise_exception: bool = True,
        **kwargs: Any,
    ) -> list[Any] | dict[str, Any] | None:
        """Get API response from SPAN Panel."""

        data = await self.api_request_raw(
            url,
            method=method,
            raise_exception=raise_exception,
            **kwargs,
        )
        if data is not None:
            return cast(list[Any] | dict[str, Any], orjson.loads(data))
        return None

    async def api_response_klass(
        self,
        klass: type[T],
        url: str,
        *,
        method: str = "get",
        raise_exception: bool = True,
        **kwargs: Any,
    ) -> T:
        """Get API response with given data schema."""

        response = await self.api_request_json(
            url,
            method=method,
            raise_exception=raise_exception,
            **kwargs,
        )
        if isinstance(response, dict):
            return klass(**response)
        if response:
            raise SpanError("Unexpected list response: %s", url)
        raise SpanError("Unexpected empty response: %s", url)

    async def generate_token(
        self,
        *,
        name: str,
        description: str | None = None,
    ) -> d.AuthOut:
        """Generate JWT Token for auth."""

        data = d.AuthIn(name=name, description=description)
        return await self.api_response_klass(
            d.AuthOut,
            "auth/register",
            method="post",
            json=data.dict(),
        )

    async def get_storage_nice_to_have_threshold(self) -> d.NiceToHaveThreshold:
        """Get Nice to have thresholds (low, high)."""

        return await self.api_response_klass(
            d.NiceToHaveThreshold,
            "storage/nice-to-have-thresh",
        )

    async def set_storage_nice_to_have_threshold(
        self,
        *,
        low: int,
        high: int,
    ) -> d.NiceToHaveThreshold:
        """Set Nice to have thresholds (low, high)."""

        data = d.NiceToHaveThreshold(
            nice_to_have_threshold_low_soe=d.StateOfEnergy(percentage=low),
            nice_to_have_threshold_high_soe=d.StateOfEnergy(percentage=high),
        )
        return await self.api_response_klass(
            d.NiceToHaveThreshold,
            "storage/nice-to-have-thresh",
            method="post",
            json=data.dict(),
        )

    async def get_storage_level(self) -> d.BatteryStorage:
        """Get storage state of energy levels."""

        return await self.api_response_klass(
            d.BatteryStorage,
            "storage/soe",
        )

    async def get_circuits(self) -> d.CircuitsOut:
        """Get panel circuits."""

        return await self.api_response_klass(
            d.CircuitsOut,
            "circuits",
        )

    async def get_circuit(self, circuit_id: str) -> d.Circuit:
        """Get specific panel circuit."""

        return await self.api_response_klass(
            d.Circuit,
            f"circuits/{circuit_id}",
        )

    async def get_panel_meter(self) -> d.PanelMeter:
        """Get panel meter."""

        return await self.api_response_klass(
            d.PanelMeter,
            "panel/meter",
        )

    async def get_panel_power(self) -> d.PanelPower:
        """Get panel power."""

        return await self.api_response_klass(
            d.PanelPower,
            "panel/power",
        )

    async def get_islanding_state(self) -> d.IslandingState:
        """Get panel islanding state."""

        return await self.api_response_klass(
            d.IslandingState,
            "islanding-state",
        )

    async def get_main_relay_state(self) -> d.RelayStateOut:
        """Get main relay state."""

        return await self.api_response_klass(
            d.RelayStateOut,
            "panel/grid",
        )

    async def get_panel(self) -> d.PanelState:
        """Get panel state."""

        return await self.api_response_klass(
            d.PanelState,
            "panel",
        )

    async def get_system_status(self) -> d.StatusOut:
        """Get system status."""

        return await self.api_response_klass(
            d.StatusOut,
            "status",
        )
