import json
from data import RAW_PRODUCT_DATA
from logic import define_competitor_data
from agents import AgentFactory

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Generated: {filename}")

def run_orchestrator():
    print("Starting LangChain Agentic Pipeline...")
    
    competitor_data = define_competitor_data()
    
    faq_agent = AgentFactory.get_faq_chain()
    product_agent = AgentFactory.get_product_page_chain()
    comparison_agent = AgentFactory.get_comparison_chain()
    
    
    print("... Agent 1: Generating FAQs")
    faq_result = faq_agent.invoke({"product_data": RAW_PRODUCT_DATA})
    save_json("faq.json", faq_result)
    
    print("... Agent 2: Generating Product Page")
    product_result = product_agent.invoke({"product_data": RAW_PRODUCT_DATA})
    save_json("product_page.json", product_result)
    
    print("... Agent 3: Generating Comparison")
    comparison_result = comparison_agent.invoke({
        "product_a": RAW_PRODUCT_DATA,
        "product_b": competitor_data
    })
    save_json("comparison_page.json", comparison_result)
    
    print("🎉 Pipeline Complete. All requirements met using LangChain.")

if __name__ == "__main__":
    run_orchestrator()