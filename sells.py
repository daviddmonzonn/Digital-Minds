sales = [
  {"product": "Shirt", "quantity": 2, "unit_price": 15.99},
  {"product": "Pants", "quantity": 1, "unit_price": 36.50},
  {"product": "Shirt", "quantity": 4, "unit_price": 15.99},
  {"product": "Shoes", "quantity": 2, "unit_price": 78.00}
]

def analyze_sales(sales):
  sales_summary = {}
  total_incomes = 0
  for sale in sales:
    product = sale["product"]
    quantity = sale["quantity"]
    unit_price = sale["unit_price"]
    product_incomes = quantity * unit_price
    if product not in sales_summary:
      sales_summary[product] = {"quantity": 0, "income": 0}
    sales_summary[product]["quantity"] += quantity
    sales_summary[product]["income"] += product_income
    total_incomes += product_incomes
  best_selling_product = None
  max_quantity = 0
  for product, data in sales_summary.items():
    if data["quantity"] > max_quantity:
      max_quantity = data["quantity"]
      best_selling_product = product


if __name__ == "__main__":
  analyze_sales(sales)
  
