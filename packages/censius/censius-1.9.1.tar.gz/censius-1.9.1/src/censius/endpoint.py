
""" This file was generated automatically using `generate.py` in "PROD" mode, do not edit it manually.
	Generated at: 2024-03-19 06:32:47 UTC """

CENSIUS_ENDPOINT = ["https://gateway.censius.ai/"]


def get_gateway_url():
    return f"{CENSIUS_ENDPOINT[0]}/api/sdkapi"

def get_gateway_llm_url():
    return f"{CENSIUS_ENDPOINT[0]}/api/llm"
