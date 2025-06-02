import time

def create_transaction(sender_id, receiver_id, amount, accounts, blockchain):
    if sender_id not in accounts or receiver_id not in accounts:
        return {"error": "Invalid account ID"}

    sender = accounts[sender_id]
    receiver = accounts[receiver_id]

    if not sender.withdraw(amount):
        return {"error": "Insufficient funds"}

    receiver.deposit(amount)

    txn = {
        "sender": sender_id,
        "receiver": receiver_id,
        "amount": amount,
        "timestamp": time.time()
    }

    blockchain.add_block([txn])
    return {"status": "Transaction successful", "transaction": txn}
