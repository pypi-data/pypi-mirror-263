import os
from typing import List

from fastapi import APIRouter, HTTPException, Query
from fastapi import UploadFile, File, HTTPException, Form, APIRouter

import auto_artifacts.server.api_keys as api_keys
from auto_artifacts.server.config import PATH_ARTIFACTS
from auto_artifacts.server.log import get_logger

router = APIRouter()

logger = get_logger(__name__)

def list_files_recursively(path: str) -> List[str]:
    """Recursively lists all files in the given directory."""
    files_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

@router.get("/files")
async def list_files(api_key: str = Query(None, description="API Key for accessing private files")):

    if "list" not in api_keys.keys[api_key]["access"]:
        return "unauthorized access"

    # Get paths
    if not os.path.exists(PATH_ARTIFACTS):
        raise HTTPException(status_code=404, detail="Directory not found")
    paths = list_files_recursively(PATH_ARTIFACTS)

    # Parse paths
    remote_paths = []
    for path in paths:
        remote_path = path.split("artifacts/")[1]
        if api_keys.validate(remote_path):
            if api_keys.auth(api_key, remote_path):
                remote_paths.append(remote_path)

    return remote_paths
