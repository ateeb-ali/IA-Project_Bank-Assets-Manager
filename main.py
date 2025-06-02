import json
import os
from blockchain import Blockchain, Block
from bank_asset_manager import BankAccount
from transactions import create_transaction

ACCOUNTS_FILE = "accounts.json"
BLOCKCHAIN_FILE = "blockchain.json"

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump({k: v.to_dict() for k, v in accounts.items()}, f, indent=4)

def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, "r") as f:
        data = json.load(f)
        return {k: BankAccount.from_dict(v) for k, v in data.items()}

def save_blockchain(blockchain):
    with open(BLOCKCHAIN_FILE, "w") as f:
        json.dump([vars(block) for block in blockchain.chain], f, indent=4)

def load_blockchain():
    if not os.path.exists(BLOCKCHAIN_FILE):
        return Blockchain()
    with open(BLOCKCHAIN_FILE, "r") as f:
        data = json.load(f)
        bc = Blockchain()
        bc.chain = []
        for block_data in data:
            block = Block(
                block_data["index"],
                block_data["previous_hash"],
                block_data["transactions"]
            )
            block.timestamp = block_data["timestamp"]
            block.nonce = block_data["nonce"]
            block.hash = block_data["hash"]
            bc.chain.append(block)
        return bc

# Load or initialize data
accounts = load_accounts()
if not accounts:
    accounts = {
        "1": BankAccount("1", "Abdullah", 1000),
        "2": BankAccount("2", "Asif", 500)
    }

blockchain = load_blockchain()

def main():
    while True:
        print("\n1. View Accounts\n2. Transfer Asset\n3. Mine Block\n4. View Blockchain\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            for acc in accounts.values():
                print(acc.to_dict())

        elif choice == '2':
            s = input("Sender ID: ")
            r = input("Receiver ID: ")
            try:
                amt = float(input("Amount: "))
            except ValueError:
                print("Invalid amount. Must be a number.")
                continue

            result = create_transaction(s, r, amt, accounts, blockchain)
            print("Transaction Result:", result)
            save_accounts(accounts)
            save_blockchain(blockchain)

        elif choice == '3':
            index = blockchain.mine()
            print(f"Block {index} mined.")
            save_blockchain(blockchain)

        elif choice == '4':
            for block in blockchain.chain:
                print(vars(block))

        elif choice == '5':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
