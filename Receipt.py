def printReceipt(cart,total):
    receipt = open('receipt.txt','w')
    receipt.write("You bought:\n")
    for i in cart:
        if len(i) == 4:
            receipt.write(i[0] + ' - $%.2f\n' %i[1])
        else:
            receipt.write(i[0] + ' - $%.2f\n' %i[2])
    receipt.write('\nYour total is: $%.2f\n' %total)
    receipt.write("\nThank you for shopping!")
    receipt.close()
    return
