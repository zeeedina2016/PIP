sale_amount = 0
ans = True

while ans > 0:
    sale_amount = float(input("Enter Sale amount: $ "))
    #If the sale amount is greater than 4000 discount price is 40
    if sale_amount > 4000:
        sale2 = sale_amount * 0.40
        sale_amount = (sale_amount - sale2)
            
    #if the sale amount is between 2000 and 4000, discount price is 30
    elif sale_amount > 2000 and sale_amount < 4000:
        sale2 = sale_amount * 0.30
        sale_amount = (sale_amount - sale2)
            
    #if the sale amount is between 1000 and 2000, discount price is 20
    elif sale_amount > 1000 and sale_amount < 2000:
        sale2 = sale_amount * 0.20
        sale_amount = (sale_amount - sale2)
            
    #if the sale amount is lower than 1000, discount price is 10
    else:
        sale_amount < 1000
        sale2 = sale_amount * 0.10
        sale_amount = (sale_amount - sale2)
        

        
    #print your discounted sale amount
    print("Your discounted sale amount is $",sale_amount)
