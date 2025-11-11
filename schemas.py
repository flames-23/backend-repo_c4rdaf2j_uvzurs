"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal

# Example schemas (you can keep or replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# TALaiNT Labz – Contact Inquiry schema
# Collection name: "contactinquiry" (class name lowercased)
class ContactInquiry(BaseModel):
    """
    Stores contact form submissions from organizations interested in
    AI/ML/Data Science recruitment services.
    """
    name: str = Field(..., min_length=2, description="Contact person full name")
    email: EmailStr = Field(..., description="Business email")
    phone: Optional[str] = Field(None, description="Phone number")
    company: Optional[str] = Field(None, description="Company name")
    job_title: Optional[str] = Field(None, description="Role/title of the contact")
    hiring_need: Literal[
        "single_hire",
        "multiple_hires",
        "contract",
        "contract_to_hire",
        "unsure"
    ] = Field("unsure", description="Type of hiring engagement")
    timeframe: Literal["immediate", "1-3_months", "3+_months", "unsure"] = Field("unsure")
    budget_range: Optional[str] = Field(None, description="Optional budget guidance")
    preferred_contact: Literal["email", "phone"] = Field("email")
    message: Optional[str] = Field(None, description="Additional context or role details")
    consent_marketing: bool = Field(False, description="Consent to receive updates")
    source: Optional[str] = Field(None, description="How they heard about us")

# Add more schemas below if needed
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
