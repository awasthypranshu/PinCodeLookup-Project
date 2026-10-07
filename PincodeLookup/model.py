from pydantic import BaseModel,field_validator
class PincodeReq(BaseModel):
    pincode:str
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls,v:str):
        if not v.isdigit() or len(v) != 6:
            raise ValueError("Pincode must be a 6-digit number")
        return v

class LocationRes(BaseModel):
    pincode:str
    city:str
    state:str
    district:str
    
class BulkReq(BaseModel):
    pincodes:list[str]
    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls,v:list[str]):
        if not v:
            raise ValueError("Pincodes list cannot be empty")
        return v

class BulkRes(BaseModel):
    status:str = "success"
    found:int
    not_found:list[str]
    results : list[LocationRes]
    missing : list[str]


