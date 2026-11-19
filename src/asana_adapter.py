"""Minimal Asana read-only adapter. No write functions are implemented in v1."""
from __future__ import annotations
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


class AsanaReadOnlyClient:
    def __init__(self, access_token: str, base_url: str = "https://app.asana.com/api/1.0"):
        if not access_token:
            raise ValueError("ASANA_ACCESS_TOKEN must be configured")
        self.access_token = access_token
        self.base_url = base_url.rstrip("/")

    def get(self, path: str) -> dict:
        if not path.startswith("/") or ".." in path or "?" in path:
            raise ValueError("Path must be a trusted relative API path")
        request = Request(
            self.base_url + path,
            headers={"Authorization": f"Bearer {self.access_token}", "Accept": "application/json"},
            method="GET",
        )
        try:
            with urlopen(request, timeout=15) as response:
                return json.load(response)
        except (HTTPError, URLError) as error:
            raise RuntimeError(f"Asana read failed ({type(error).__name__}); check scopes, network, rate limits") from None

    def project_sections(self, project_gid: str) -> dict:
        if not project_gid.isdecimal():
            raise ValueError("Project GID must be numeric")
        return self.get(f"/projects/{project_gid}/sections")
