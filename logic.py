def format_product_data(raw_data: str) -> str:
    """Cleans and formats the raw product data string."""
    return raw_data.strip()

def extract_key_specs(raw_data: str) -> str:
    """Extracts just the technical specs (Concentration, Price) for the AI to focus on."""
    lines = raw_data.split('\n')
    specs = [line for line in lines if "Concentration" in line or "Price" in line]
    return "\n".join(specs)

def define_competitor_data():
    """Returns the structured data for the fictional competitor."""
    return """
    Product Name: DullBeGone Serum
    Concentration: 5% Vitamin C
    Skin Type: All Skin Types
    Key Ingredients: Vitamin C, Aloe Vera
    Benefits: Hydration, Mild Brightening
    Price: ₹499
    """