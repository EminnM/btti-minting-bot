from web3 import Web3
from hexbytes import HexBytes
import pwinput
import time
private_key = pwinput.pwinput("Enter your private key:")


rpc_link = 'https://rpc.bittorrentchain.io/' # btt

no_to_mint = int(input("Enter the tx amount:"))

hex_data = "0x646174613a2c7b2270223a226274742d3230222c226f70223a226d696e74222c227469636b223a2262747469222c22616d74223a2231303030227d"

price_factor = 1

w3 = Web3(Web3.HTTPProvider(rpc_link))
if not w3.is_connected():
    raise ConnectionError("Failed to connect to node")

for i in range(no_to_mint):
    print(f"The inscription being engraved is: {i+1}")
    sender_account = w3.eth.account.from_key(private_key)
    sender_address = sender_account.address
    chain_id = w3.eth.chain_id
    gas_price = w3.eth.gas_price

    transaction = {
        'to': sender_address,
        'value': 0,  # Value is 0 ETH
        'gas': 100000,
        'gasPrice': int(gas_price*price_factor),
        'nonce': w3.eth.get_transaction_count(sender_address),
        'data': hex_data,
        'chainId': chain_id
    }

    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    tx_hash = txn_receipt.transactionHash.hex()

    print(f"The inscription {i+1} is completed, transaction hash is {tx_hash}.")
    time.sleep(10)
