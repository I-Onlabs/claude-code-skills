---
name: python-best-practices
description: Use when writing Python code. Enforces modern Python 3.11+ patterns, comprehensive type hints, async patterns, and production-ready code quality standards.
---

# Python Best Practices

## When This Skill Activates
- Writing any Python code
- Reviewing Python code
- Setting up Python projects
- Questions about Python patterns

## Modern Python Patterns (3.11+)

### Type Hints Everywhere

```python
# Modern union syntax (3.10+)
def process(value: str | None) -> dict[str, int]:
    ...

# NOT the old way
from typing import Optional, Dict
def process(value: Optional[str]) -> Dict[str, int]:  # Don't do this
    ...
```

### Match Statements (3.10+)

```python
# Modern pattern matching
match response.status_code:
    case 200:
        return response.json()
    case 404:
        raise NotFoundError()
    case 500:
        raise ServerError()
    case _:
        raise UnexpectedError(response.status_code)

# NOT if/elif chains for this
if response.status_code == 200:  # Don't do this for case analysis
    ...
```

### Data Classes & Pydantic

```python
# For simple data containers
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

# For validation & serialization
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int = 0
```

## Async Patterns

### Use async for I/O

```python
# Good - async for I/O operations
async def fetch_data(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# Bad - sync in async context
def fetch_data(url: str) -> dict:  # Blocks event loop
    return requests.get(url).json()
```

### Concurrent Operations

```python
# Run multiple async operations concurrently
async def fetch_all(urls: list[str]) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```

### Context Managers

```python
# Async context managers for resources
async with aiofiles.open("file.txt") as f:
    content = await f.read()

# Async generators
async def stream_data():
    async for chunk in response.content:
        yield process(chunk)
```

## Code Quality Tools

### Type Checking

```bash
# Use mypy or pyright
mypy src/ --strict
pyright src/
```

### Linting

```bash
# Use ruff (fast, comprehensive)
ruff check .
ruff format .

# Or black + isort + flake8
black .
isort .
flake8 .
```

### Pre-commit Config

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.0
    hooks:
      - id: mypy
```

## Project Structure

```
project/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── models.py
│       ├── services.py
│       └── api/
│           ├── __init__.py
│           └── routes.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_services.py
├── pyproject.toml
├── README.md
└── .pre-commit-config.yaml
```

## Testing with Pytest

```python
import pytest
from unittest.mock import AsyncMock

# Fixtures
@pytest.fixture
def user_service():
    return UserService(db=MockDB())

# Async tests
@pytest.mark.asyncio
async def test_create_user(user_service):
    user = await user_service.create(UserCreate(name="Test"))
    assert user.name == "Test"

# Parametrized tests
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
])
def test_uppercase(input, expected):
    assert input.upper() == expected

# Mocking
async def test_external_api(mocker):
    mock_fetch = mocker.patch("module.fetch", new_callable=AsyncMock)
    mock_fetch.return_value = {"data": "test"}
    result = await process_data()
    assert result == {"data": "test"}
```

## Dependency Management

```toml
# pyproject.toml
[project]
name = "mypackage"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.100.0",
    "pydantic>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
]
```

## Common Anti-Patterns

| Don't | Do |
|-------|-----|
| `from typing import Optional` | `str \| None` |
| `Dict[str, Any]` | `dict[str, Any]` |
| Bare `except:` | `except Exception:` |
| `== None` | `is None` |
| Mutable default args | `field(default_factory=list)` |

## Docstrings

```python
def calculate_total(
    items: list[Item],
    discount: float = 0.0,
) -> float:
    """Calculate the total price with optional discount.

    Args:
        items: List of items to sum.
        discount: Percentage discount (0.0 to 1.0).

    Returns:
        Total price after discount.

    Raises:
        ValueError: If discount is not between 0 and 1.
    """
    ...
```
