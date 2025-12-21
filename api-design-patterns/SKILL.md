---
name: api-design-patterns
description: Use when creating REST APIs, FastAPI endpoints, GraphQL schemas, or designing API architecture. Provides patterns for models, services, routers, and comprehensive testing.
---

# API Design Patterns

## When This Skill Activates
- Creating new API endpoints
- Designing REST or GraphQL APIs
- Building FastAPI/Flask/Express services
- Questions about API architecture
- CRUD operation implementation

## The 5-Layer Pattern

Every API endpoint should have these layers:

```
┌─────────────────────────────┐
│  1. MODELS (Data Shapes)    │  Pydantic/TypeScript interfaces
├─────────────────────────────┤
│  2. SERVICE (Business Logic)│  CRUD operations, validation
├─────────────────────────────┤
│  3. ROUTER (HTTP Layer)     │  Endpoints, status codes
├─────────────────────────────┤
│  4. TESTS (Quality)         │  Unit + integration tests
├─────────────────────────────┤
│  5. DOCS (OpenAPI)          │  Auto-generated from types
└─────────────────────────────┘
```

## Model Patterns (Pydantic)

```python
from pydantic import BaseModel
from datetime import datetime

# Base - shared fields
class UserBase(BaseModel):
    email: str
    name: str

# Create - for POST requests
class UserCreate(UserBase):
    password: str

# Update - for PATCH requests (all optional)
class UserUpdate(BaseModel):
    email: str | None = None
    name: str | None = None
    password: str | None = None

# Response - what API returns
class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
```

## Service Layer Pattern

```python
class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def create(self, data: UserCreate) -> User:
        user = User(**data.model_dump())
        self.db.add(user)
        await self.db.commit()
        return user

    async def get(self, id: int) -> User | None:
        return await self.db.get(User, id)

    async def list(self, skip: int = 0, limit: int = 100) -> list[User]:
        return await self.db.execute(
            select(User).offset(skip).limit(limit)
        )

    async def update(self, id: int, data: UserUpdate) -> User | None:
        user = await self.get(id)
        if user:
            for key, value in data.model_dump(exclude_unset=True).items():
                setattr(user, key, value)
            await self.db.commit()
        return user

    async def delete(self, id: int) -> bool:
        user = await self.get(id)
        if user:
            await self.db.delete(user)
            await self.db.commit()
            return True
        return False
```

## Router Pattern (FastAPI)

```python
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(data: UserCreate, service: UserService = Depends()):
    return await service.create(data)

@router.get("/{id}", response_model=UserResponse)
async def get_user(id: int, service: UserService = Depends()):
    user = await service.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[UserResponse])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    service: UserService = Depends()
):
    return await service.list(skip, limit)

@router.patch("/{id}", response_model=UserResponse)
async def update_user(id: int, data: UserUpdate, service: UserService = Depends()):
    user = await service.update(id, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, service: UserService = Depends()):
    if not await service.delete(id):
        raise HTTPException(status_code=404, detail="User not found")
```

## REST Conventions

| Operation | Method | Path | Status |
|-----------|--------|------|--------|
| Create | POST | /users | 201 |
| Read one | GET | /users/{id} | 200 |
| Read all | GET | /users | 200 |
| Update | PATCH | /users/{id} | 200 |
| Replace | PUT | /users/{id} | 200 |
| Delete | DELETE | /users/{id} | 204 |

## Pagination Pattern

```python
class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int
    per_page: int
    pages: int

@router.get("/", response_model=PaginatedResponse[UserResponse])
async def list_users(page: int = 1, per_page: int = 20):
    ...
```

## Error Handling

```python
from fastapi import HTTPException

# Standard error responses
raise HTTPException(status_code=400, detail="Bad request")
raise HTTPException(status_code=401, detail="Unauthorized")
raise HTTPException(status_code=403, detail="Forbidden")
raise HTTPException(status_code=404, detail="Not found")
raise HTTPException(status_code=422, detail="Validation error")
raise HTTPException(status_code=500, detail="Internal server error")
```

## Integration

- Works with `/fastapi-endpoint` command
- Delegates complex work to `backend-developer` agent
- Follows `python-best-practices` skill for code quality
