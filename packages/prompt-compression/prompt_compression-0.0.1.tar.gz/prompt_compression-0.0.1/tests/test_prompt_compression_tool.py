import pytest
import unittest

from promptflow.connections import CustomConnection
from prompt_compression.tools.prompt_compression_tool import prompt_compression_tool


# @pytest.fixture
# def my_custom_connection() -> CustomConnection:
#     my_custom_connection = CustomConnection(
#         {
#             "api-key" : "my-api-key",
#             "api-secret" : "my-api-secret",
#             "api-url" : "my-api-url"
#         }
#     )
#     return my_custom_connection


# class TestTool:
#     def test_prompt_compression_tool(self, my_custom_connection):
#         result = prompt_compression_tool(my_custom_connection, input_text="Microsoft")
#         assert result == "Hello Microsoft"

class TestTool:
    def test_prompt_compression_tool(self):
        original_prompt = "Confirm that the tool YAML files are included in your custom tool package. You can add the YAML files to MANIFEST.in and include the package data in setup.py. Alternatively, you can test your tool package using the script below to ensure that you've packaged your tool YAML files and configured the package tool entry point correctly."
        compressed_prompt = prompt_compression_tool(prompt=original_prompt)
        print("compressed prompt: ", compressed_prompt)
        assert len(compressed_prompt) < len(original_prompt)


# Run the unit tests
if __name__ == "__main__":
    unittest.main()