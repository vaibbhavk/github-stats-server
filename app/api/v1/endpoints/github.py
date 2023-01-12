import httpx

from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas import user, repo

router = APIRouter()

@router.get("/user/", response_model= user.User)
def get_user(username: str ) -> user.User:
    """
    Get a GitHub user by username.
    Arguments:
    username: query parameter
    Returns:
    GitHub user
    """
    try:
        r = httpx.get(f'https://api.github.com/users/{username}')
        if(r.status_code == 200):
            return r.json()
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=f'{exc.response.json()["message"]}')

@router.get("/repos/", response_model= List[repo.Repo])
def get_all_public_repos(username: str ) -> List[repo.Repo]:
    """
    Get all public repos of a user by username, from GitHub.
    Arguments:
    username: query parameter
    Returns:
    list of repos of a GitHub user
    """
    try:
        r = httpx.get(f'https://api.github.com/users/{username}/repos')
        if(r.status_code == 200):
            return r.json()
        r.raise_for_status()
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=f'{exc.response.json()["message"]}')