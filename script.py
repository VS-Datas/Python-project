lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
print (lovely_loveseat_description)
lovely_loveseat_price = 254.00
print (lovely_loveseat_price)


stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
print (stylish_settee_description)
stylish_settee_price = 180.50
print (stylish_settee_price)


luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15
print (luxurious_lamp_price)


sales_tax = .088
print (sales_tax)

customer_one_total = 0
print (customer_one_total)

customer_one_itemization = ""
print (customer_one_itemization)

customer_one_total += 254.00
print (customer_one_total)

customer_one_itemization += lovely_loveseat_description
print (customer_one_itemization)

customer_one_total += 52.15
print (customer_one_total)

customer_one_itemization += luxurious_lamp_description
print (customer_one_itemization)

customer_one_tax = customer_one_total * sales_tax
print (customer_one_tax)

customer_one_total = customer_one_tax * sales_tax
print (customer_one_total)
customer_one_total += customer_one_tax

#Print the receipe
print ("Customer One Items:")
print (customer_one_itemization)

print ("Customer One Total:")
print (customer_one_total)










