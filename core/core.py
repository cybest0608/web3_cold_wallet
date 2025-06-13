import asyncio
from aptos_sdk.account import Account
from aptos_sdk.async_client import FaucetClient, RestClient
from aptos_sdk.transactions import EntryFunction, TransactionPayload, TransactionArgument, RawTransaction
from aptos_sdk.bcs import Serializer
import time
 
# Network configuration
NODE_URL = "https://fullnode.devnet.aptoslabs.com/v1"
FAUCET_URL = "https://faucet.devnet.aptoslabs.com"
 
async def main():
    # Initialize the clients
    rest_client = RestClient(NODE_URL)
    faucet_client = FaucetClient(FAUCET_URL, rest_client)
    
    print("Connected to Aptos devnet")
 
    # Generate two accounts
    alice = Account.generate()
    bob = Account.generate()
    
    print("=== Addresses ===")
    print(f"Alice's address: {alice.address()}")
        # More code will go here
        # Fund the accounts with test APT from the devnet faucet
    print("\n=== Funding accounts ===")
    alice_amount = 100_000_000  # 1 APT = 100,000,000 octas
    
    await faucet_client.fund_account(alice.address(), alice_amount)

    print("Accounts funded successfully")
    
    # Check initial balances
    alice_balance = await rest_client.account_balance(alice.address())

    
    print("\n=== Initial Balances ===")
    print(f"Alice: {alice_balance} octas")
    
    
if __name__ == "__main__":
    asyncio.run(main())