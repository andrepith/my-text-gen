# TinyLlama FastAPI

This is a FastAPI service for TinyLlama-1.1B-Chat-v1.0 served via Hugging Face Spaces using Docker.

## Endpoint

POST `/api/chat`

```json
{
  "prompt": "Tell me a story."
}
