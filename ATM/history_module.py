
transactions = []

def transaction_history():
    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)
    return        
