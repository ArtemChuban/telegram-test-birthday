FROM ghcr.io/astral-sh/uv:python3.11-alpine AS builder
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-editable --no-dev

FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder --chown=app:app /app/.venv ./.venv
COPY . .
EXPOSE 8000
