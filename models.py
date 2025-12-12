from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional

class FAQItem(BaseModel):
    question: str = Field(description="The question asked by the user")
    answer: str = Field(description="The answer to the question")
    category: str = Field(description="Category like Usage, Safety, etc.")

class FAQPage(BaseModel):
    page_title: str = Field(description="Title of the FAQ page")
    faqs: List[FAQItem] = Field(description="List of at least 5 FAQ items")

class ProductPage(BaseModel):
    header: str = Field(description="Product Name")
    description: str = Field(description="SEO-optimized product description")
    key_benefits: List[str] = Field(description="List of key benefits")
    specifications: dict = Field(description="Key specs like concentration, price, etc.")

class ComparisonPoint(BaseModel):
    feature: str = Field(description=" The feature being compared (e.g., Price)")
    product_a_value: str = Field(description="Value for GlowBoost")
    product_b_value: str = Field(description="Value for the competitor")

class ComparisonPage(BaseModel):
    title: str = Field(description="Comparison Page Title")
    product_a: str = Field(description="Name of Product A")
    product_b: str = Field(description="Name of Product B")
    comparison_table: List[ComparisonPoint] = Field(description="List of comparison points")