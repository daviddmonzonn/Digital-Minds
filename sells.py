MIT License

Copyright (c) 2024 Digital Minds

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


# This function analyzes a list of sales to provide a detailed summary.
def analyze_sales(sales):
    # Initialize an empty dictionary to summarize sales data
    sales_summary = {}
    # Variable to keep track of total income from all sales
    total_incomes = 0
    # Iterate through each sale in the provided sales list
    for sale in sales:
        # Extract product name, quantity sold, and unit price from the sale
        product = sale["product"]
        quantity = sale["quantity"]
        unit_price = sale["unit_price"]
        # Calculate the income generated by this sale
        product_incomes = quantity * unit_price
        # If the product is not yet in the sales summary, add it with default values
        if product not in sales_summary:
            sales_summary[product] = {"quantity": 0, "income": 0}
        # Update the total quantity and income for this product in the sales summary
        sales_summary[product]["quantity"] += quantity
        sales_summary[product]["income"] += product_incomes
        # Add the income from this sale to the total incomes
        total_incomes += product_incomes
    # Variables to determine the best-selling product (based on quantity sold)
    best_selling_product = None
    max_quantity = 0
    
    # Iterate through the sales summary to find the product with the highest quantity sold
    for product, data in sales_summary.items():
        if data["quantity"] > max_quantity:
            max_quantity = data["quantity"]
            best_selling_product = product
    # Return the sales summary, total income, and the best-selling product
    return sales_summary, total_incomes, best_selling_product


if __name__ == "__main__":
  summary, total_income, best_seller = analyze_sales(sales)
  print("Sales summary:")
  for product, data in summary.items():
    print(f"- {product}: {data['quantity']} units solds, the total income is: {data['income']:.2f}")
  print(f"\nBest selling product: {best_seller}")
  print(f"\nTotal income: {total_income:.2f}")
