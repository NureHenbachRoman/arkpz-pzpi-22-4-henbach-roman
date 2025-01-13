from enum import Enum


class UserRole(Enum):
    CUSTOMER = 'Customer'
    OWNER = 'Owner'
    MANAGER = 'Manager'
    ADMIN = 'Admin'
    DB_ADMIN = 'DbAdmin'
