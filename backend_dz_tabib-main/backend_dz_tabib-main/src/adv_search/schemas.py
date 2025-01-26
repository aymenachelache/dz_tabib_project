# src/adv_search/schemas.py

from typing import List, Dict, Optional
from pydantic import BaseModel

class SpecialiteResponse(BaseModel):
    specialities: Dict[int, str]

class AssuranceResponse(BaseModel):
    assurances: Dict[int, str]

class DoctorHomepage(BaseModel):
    id: Optional[int] = None
    firstname: Optional[str] = None
    familyname: Optional[str] = None
    specialite: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    photo: Optional[str] = None
    rating: Optional[float] = None

class AdvancedSearchRequest(BaseModel):
    specialite: Optional[str] = None
    localization: Optional[str] = None
    assurance: Optional[str] = None
    disponibilite: Optional[str] = None
    page: int = 1

class DoctorResponse(BaseModel):
    doctors: List[DoctorHomepage]

class AdvancedSearchResponse(BaseModel):
    specialities: Dict[int, str]
    assurances: Dict[int, str]
    days_of_week: List[str]
    doctors: List[DoctorHomepage]


