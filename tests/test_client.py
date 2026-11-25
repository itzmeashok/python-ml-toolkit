from unittest.mock import patch, MagicMock

import pytest

from llm_client.client import OllamaClient


@pytest.fixture
def client():
    return OllamaClient()


@patch("llm_client.client.httpx.post")
def test_chat_returns_content(mock_post, client):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "message": {"content": "An API is a contract..."}
    }
    mock_response.raise_for_status = MagicMock()
    mock_post.return_value = mock_response

    result = client.chat("You are an engineer.", "Explain APIs", temperature=0.6)

    assert result == "An API is a contract..."
    mock_post.assert_called_once()
    call_kwargs = mock_post.call_args
    assert call_kwargs.kwargs["json"]["options"]["temperature"] == 0.6
    assert call_kwargs.kwargs["json"]["model"] == "llama3.2:3b"
    assert call_kwargs.kwargs["json"]["messages"][0]["role"] == "system"

@patch("llm_client.client.httpx.post")
def test_chat_raises_on_error(mock_post, client):
    import httpx
    mock_post.side_effect = httpx.HTTPStatusError(
        "Server Error", request=MagicMock(), response=MagicMock(status_code=500)
    )

    with pytest.raises(httpx.HTTPStatusError):
        client.chat("sys", "user")   
