import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from models import FAQPage, ProductPage, ComparisonPage

GOOGLE_API_KEY = "AIzaSyAd-EkzA7qzQEPPDveAlXjAQjP9PzQSd0Y"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

class AgentFactory:
    """
    Creates LangChain 'Chains' (Agents) for specific tasks.
    Each chain has a specific Prompt and a specific Pydantic Parser.
    """
    
    @staticmethod
    def get_faq_chain():
        
        parser = JsonOutputParser(pydantic_object=FAQPage)
        
        prompt = PromptTemplate(
            template="""
            You are an expert content strategist.
            Based on the following product data, generate a comprehensive FAQ page.
            
            PRODUCT DATA:
            {product_data}
            
            REQUIREMENTS:
            - Generate at least 5 questions.
            - Categorize them (Usage, Safety, etc.).
            - Output must be valid JSON matching the following schema.
            
            {format_instructions}
            """,
            input_variables=["product_data"],
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        
        return prompt | llm | parser

    @staticmethod
    def get_product_page_chain():
        parser = JsonOutputParser(pydantic_object=ProductPage)
        prompt = PromptTemplate(
            template="""
            You are a senior copywriter. Write a compelling product page for this item.
            
            PRODUCT DATA:
            {product_data}
            
            REQUIREMENTS:
            - Write a catchy header.
            - Write an SEO-friendly description.
            - Extract key benefits and specifications.
            
            {format_instructions}
            """,
            input_variables=["product_data"],
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        return prompt | llm | parser

    @staticmethod
    def get_comparison_chain():
        parser = JsonOutputParser(pydantic_object=ComparisonPage)
        prompt = PromptTemplate(
            template="""
            You are a product analyst. Compare these two products objectively.
            
            PRODUCT A (Our Product):
            {product_a}
            
            PRODUCT B (Competitor):
            {product_b}
            
            REQUIREMENTS:
            - Identify key differences in Price, Concentration, and Ingredients.
            - Output strictly in JSON format.
            
            {format_instructions}
            """,
            input_variables=["product_a", "product_b"],
            partial_variables={"format_instructions": parser.get_format_instructions()}
        )
        return prompt | llm | parser
    