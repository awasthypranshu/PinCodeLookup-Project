from fastapi import FastAPI
from exceptions import (PinCodeNotFound,PinCodeError,pincode_not_found_handler,invalid_pincode_handler)
from model import *
from data import pincodes
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Pincode Lookup API"}

app.add_exception_handler(PinCodeNotFound,pincode_not_found_handler)
app.add_exception_handler(PinCodeError,invalid_pincode_handler)

@app.get("/pincode/{code}")
def get_pincode(code:str):
    for point in pincodes:
        if point == code:
            return pincodes[point]
    raise PinCodeNotFound(code)



@app.post("/pincode/bulk",response_model=BulkRes)
def get_pincodes(req:BulkReq):
    found:list = []
    missing = []
    res = []
    for code in req.pincodes:
        if code in pincodes:
            found.append(code)
            res.append(pincodes[code])
        else:
            missing.append(code)
    return BulkRes(
        status="success",
        found=len(found),
        not_found = len(missing),
        missing=missing,
        results=res
    )

    
        