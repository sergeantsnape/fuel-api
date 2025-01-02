from abc import ABC, abstractmethod
from fastapi import HTTPException, status
from typing import Any

# abstract class to implement errors
class _BaseError(HTTPException,ABC):
    def __init__(self, **kwargs):
        super().__init__(self.get_status_code(), self.get_details(**kwargs))
    
    @abstractmethod
    def get_status_code(self) -> int:
        pass

    @abstractmethod
    def get_details(self,**kwargs) -> Any:
        pass

class ExternalSourceError(_BaseError):
    """error when failed to load the external url"""
    def get_status_code(self):
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    def get_details(self, **kwargs):
        return "Failed to fetch data from external source"
    
class CityNotFoundError(_BaseError):
    def get_status_code(self):
        return status.HTTP_404_NOT_FOUND
    def get_details(self, **kwargs):
        return f"City {kwargs['city']} not found"

class PriceNotFoundError(_BaseError):
    def get_status_code(self):
        return status.HTTP_404_NOT_FOUND
    def get_details(self, **kwargs):
        return f"Error fetching {kwargs['fuel']} price for {kwargs['city']}"
    
class UnexpectedError(_BaseError):
    def get_status_code(self):
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    def get_details(self, **kwargs):
        return "Encountered unexpected error"