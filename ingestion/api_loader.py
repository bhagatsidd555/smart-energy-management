"""
API CSV / JSON Loader (FINAL – Production Ready)
-----------------------------------------------
- Supports JSON API (your case)
- Supports CSV API
- API key OPTIONAL (local APIs supported)
"""

import io
import requests
import pandas as pd


class APILoaderError(Exception):
    pass


def load_csv_from_api(api_url: str, api_key: str | None = None) -> pd.DataFrame:
    """
    Load data from API.
    Supports:
    - JSON response with { status, data }
    - Raw CSV response
    """

    if not api_url:
        raise APILoaderError("API URL is missing")

    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        response = requests.get(
            api_url,
            headers=headers,
            timeout=30
        )
        response.raise_for_status()

    except Exception as e:
        raise APILoaderError(f"API request failed: {e}")

    # -------------------------------------------------
    # JSON RESPONSE (your API)
    # -------------------------------------------------
    content_type = response.headers.get("content-type", "").lower()

    if "application/json" in content_type:
        payload = response.json()

        if "data" not in payload or not payload["data"]:
            raise APILoaderError("API returned empty JSON data")

        df = pd.DataFrame(payload["data"])
        return df

    # -------------------------------------------------
    # CSV RESPONSE
    # -------------------------------------------------
    csv_text = response.text.strip()

    if not csv_text:
        raise APILoaderError("API returned empty CSV data")

    return pd.read_csv(io.StringIO(csv_text))
