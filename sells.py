MIT License

Copyright (c) [2024] [DigitalMinds]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


sales = [
  {"product": "Socks", "quantity": 5, "unit_price": 15.99},
  {"product": "Pants", "quantity": 3, "unit_price": 36.50},
  {"product": "Shirt", "quantity": 6, "unit_price": 15.99},
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
    sales_summary[product]["income"] += product_incomes
    total_incomes += product_incomes
  best_selling_product = None
  max_quantity = 0
  for product, data in sales_summary.items():
    if data["quantity"] > max_quantity:
      max_quantity = data["quantity"]
      best_selling_product = product
  return sales_summary, total_incomes, best_selling_product

if __name__ == "__main__":
  summary, total_income, best_seller = analyze_sales(sales)
  print("Sales summary:")
  for product, data in summary.items():
    print(f"- {product}: {data['quantity']} units solds, the total income is: {data['income']:.2f}")
  print(f"\nBest selling product: {best_seller}")
  print(f"\nTotal income: {total_income:.2f}")
