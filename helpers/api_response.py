from typing import Any, Callable, Optional
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
)

class APIResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    message: Optional[str] = None
    status_code: int

    @classmethod
    def success_response(cls, data: Any, message: str, status_code: int = HTTP_200_OK) -> JSONResponse:
        return JSONResponse(content={"success": True, "data": data, "message": message}, status_code=status_code)

    @classmethod
    def error_response(cls, message: str, status_code: int) -> JSONResponse:
        return JSONResponse(content={"success": False, "message": message}, status_code=status_code)

    @classmethod
    def handle_response(cls, fn: Callable, *args, **kwargs) -> JSONResponse:
        try:
            result = fn(*args, **kwargs)
            status_code = kwargs.get("status_code", HTTP_200_OK)
            
            return cls.success_response(data=result, message="Success", status_code=status_code)

        except HTTPException as e:
            return cls.error_response(message=e.detail, status_code=e.status_code)

        except Exception as e:
            return cls.error_response(message=str(e), status_code=HTTP_500_INTERNAL_SERVER_ERROR)
