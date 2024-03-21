from promptflow import tool
from promptflow.connections import CustomConnection

import requests
import json

# @tool
# def prompt_compression_tool(connection: CustomConnection, input_text: str) -> str:
#     # Replace with your tool code.
#     # Usually connection contains configs to connect to an API.
#     # Use CustomConnection is a dict. You can use it like: connection.api_key, connection.api_base
#     # Not all tools need a connection. You can remove it if you don't need it.
#     return "Hello " + input_text

@tool
def prompt_compression_tool(prompt: str, compression_times: float=2) -> str:

    # Call LLMLingua API

    url = "http://20.94.240.12:43324/llmlingua"

    payload = json.dumps({
    "messages": [
        {
        "content": f"[{prompt}]"
        }
    ],
    "model": "llama-2-7b",
    "component_sp": "\n\n",
    "instrution_num": 0,
    "question_num": 0,
    "type": "ratio",
    "target": 1- 1./ compression_times,
    "use_sentence_level_filter": "False",
    "use_demonstrate_level_filter": "False",
    # turn off the following options for "Non-Teams Copilot"
    "keep_name": "False",
    "is_filter_id": "False",
    "keep_split": "False"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)

    return response['results']['compressed_prompt'][1:-1]

    # if response["code"] != "200":
    #     print("Error in calling prompt compression API.")
    #     print(response)
    #     return {}
    # else:
    #     return {
    #         'origin_tokens': response['results']['origin_tokens'],
    #         'compressed_tokens': response['results']['compressed_tokens'],
    #         'ratio': response['results']['ratio'],
    #         'compressed_prompt': response['results']['compressed_prompt'][1:-1],
    #     }