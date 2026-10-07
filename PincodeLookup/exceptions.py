from fastapi.responses import JSONResponse
from fastapi import Request

class PinCodeNotFound(Exception):
    def __init__(self,pincode:str):
        self.pincode = pincode

class PinCodeError(Exception):
    def __init__(self,pincode:str,reason:str):
        self.pincode = pincode
        self.reason = reason

async def pincode_not_found_handler(request:Request,exc:PinCodeNotFound):
    return JSONResponse(
        status_code = 404,
        content = {
            "error": "pincode not found",
            "pincode": exc.pincode
        }
    )

async def invalid_pincode_handler(request:Request,exc:PinCodeError):
    return JSONResponse(
        status_code = 400,
        content = {
            "error": "pincode is invalid",
            "pincode": exc.pincode,
            "reason": exc.reason
        }
    )