"""JWT management"""

import requests

import os

from dartmouth_auth.definitions import ENV_NAMES, JWT_URL


def get_jwt(dartmouth_api_key: str = None, jwt_url: str = None) -> str | None:
    f"""Obtain a JSON Web Token

    Args:
        dartmouth_api_key (str, optional): A Dartmouth API key. If set to None, will try to use environment variable {ENV_NAMES['dartmouth_api_key']}. Defaults to None.
        jwt_url (str, optional): The URL of the endpoint returning the JWT. If set to None, defaults to {JWT_URL}. Defaults to None.

    Raises:
        ValueError: No API key is provided and no environment variable {ENV_NAMES['dartmouth_api_key']} can be found.

    Returns:
        str | None: A JWT if the API key was valid, else None.
    """
    if jwt_url is None:
        jwt_url = JWT_URL
    if dartmouth_api_key is None:
        dartmouth_api_key = os.getenv(ENV_NAMES["dartmouth_api_key"])
    if dartmouth_api_key:
        r = requests.post(
            url=jwt_url,
            headers={"Authorization": dartmouth_api_key},
        )
        jwt = r.json()
        return jwt["jwt"]
    raise ValueError(
        f"Dartmouth API key not provided as argument or defined as environment variable {ENV_NAMES['dartmouth_api_key']}."
    )


if __name__ == "__main__":
    print(get_jwt())
