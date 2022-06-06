# import Web3 class from web3 module
from turtle import pen
from web3 import Web3
# Setting node endpoint value
CHAINSTACK_NODE_ENDPOINT = '<NODE_ENDPOINT>'

# Setting account addressess
# you can copy the account addresses from metamask]

FROM_ACCOUNT = "<FROM_ACCOUNT_ADDRESS>"
TO_ACCOUNT = "<TO_ACCOUNT_ADDRESS>"

# Setting the user private key
SENDER_PRIVATEKEY = "<SENDER_PRIVATE_KEY>"

# Connect to the node
w3 = Web3(Web3.HTTPProvider(CHAINSTACK_NODE_ENDPOINT))


# Setting the value for chainID
CHAIN_ID = w3.eth.chain_id


currentAccountNonce = w3.eth.getTransactionCount(FROM_ACCOUNT)
pendingTransactionDetail = w3.eth.get_transaction(
    '<Pending_Transaction_Hash_Hex>')

# getting the nonce value
pendingTransactionNonce = pendingTransactionDetail['nonce']
# get the sender's address
pendingTransactionSender = pendingTransactionDetail['from']
# check if the transaction has a higher nonce value
if(pendingTransactionSender == FROM_ACCOUNT and currentAccountNonce < pendingTransactionNonce):
    for nonce in range(currentAccountNonce, pendingTransactionNonce):
        # you can dynamically set the MAX_PRIORITY_FEE and MAX_FEE_PER_GAS values by
        # modifying the gas_estimate.py script and returning the values corresponding to your priority
        MAX_PRIORITY_FEE = 0
        MAX_FEE_PER_GAS = 0

        transaction = {
            'nonce': nonce,
            'to': '<Account-Address>',
            'value': 0,
            'gas': 2100000,  # maximum gas that can be used for the transaction execution
            'maxFeePerGas': w3.toWei(MAX_FEE_PER_GAS, 'gwei'),
            'maxPriorityFeePerGas': w3.toWei(MAX_PRIORITY_FEE, 'gwei'),
            'chainId': CHAIN_ID
        }
        # signing the transaction using the sender's private key
        signedTransaction = w3.eth.account.sign_transaction(
            transaction, SENDER_PRIVATEKEY)
        # sending the signed transaction,
        transactionHash = w3.eth.send_raw_transaction(
            signedTransaction.rawTransaction)
        transactionHashHex = w3.toHex(transactionHash)
        transactionReceipt = w3.eth.wait_for_transaction_receipt(
            transactionHashHex)