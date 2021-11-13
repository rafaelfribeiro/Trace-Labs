from flask import render_template, Blueprint, request, flash, redirect
from web3 import Web3
from views import INFURA_URL, MINERS, get_ethereum_price, get_bitcoin_price
import time, json, requests

ethereum_bp = Blueprint('ethereum', __name__)

w3 = Web3(Web3.HTTPProvider(INFURA_URL))



@ethereum_bp.route('/')
def home():
    eth = w3.eth

    ethereum_price = get_ethereum_price()
    bitcoin_price = get_bitcoin_price()


    latest_blocks = []
    for block_number in range(eth.block_number, eth.block_number-10, -1):
        block = eth.get_block(block_number)
        latest_blocks.append(block)

    latest_transactions = []
    for tx in latest_blocks[-1]['transactions'][-10:]:
        transaction = eth.get_transaction(tx)
        latest_transactions.append(transaction)

    current_time = time.time()
    return render_template('home.html', 
        miners=MINERS,
        current_time=current_time, 
        eth=eth, 
        ethereum_price=ethereum_price,
        bitcoin_price=bitcoin_price,
        latest_blocks=latest_blocks,
        latest_transactions=latest_transactions
        )

def history(address):
    return json.loads(requests.get(
        f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=999999999&sort=asc&apikey=EAVWKU25TNZCW9GCX4B6FIASNWU2D9CBK6"
    ).text)

@ethereum_bp.route("/address")
def address():
    address = request.args.get('address')

    ethereum_price = get_ethereum_price()
    
    try:
        address = w3.toChecksumAddress(address)
    except:
        flash('Invalid address', 'danger')
        return redirect('/')

    balance = w3.eth.get_balance(address)

    teste = w3.eth.filter({'address': address, })

    balance = w3.fromWei(balance, 'ether')
    try_time_stamp = history(address)
    from datetime import datetime
    try:
        for item in try_time_stamp['result']:
            item['timeStamp'] = datetime.utcfromtimestamp(int(item['timeStamp'])).strftime('%d/%m/%Y %H:%M:%S')
    except Exception as e:
        flash('An error occurred while formatting timestamp!', 'danger')
        return redirect('/')
    
    return render_template('address.html', ethereum_price=ethereum_price, address=address, balance=balance,history=try_time_stamp)

@ethereum_bp.route("/block/<block_number>")
def block(block_number):
    block = w3.eth.get_block(int(block_number))
    
    return render_template('block.html', block=block, ethereum_price=get_ethereum_price())

@ethereum_bp.route('/transaction/<hash>')
def transaction(hash):
    tx = w3.eth.get_transaction(hash)
    value = w3.fromWei(tx.value, 'ether')
    receipt = w3.eth.get_transaction_receipt(hash)
    ethereum_price = get_ethereum_price()

    gas_price = w3.fromWei(tx.gasPrice, 'ether')

    return render_template('transaction.html', tx=tx, value=value, receipt=receipt, gas_price=gas_price, ethereum_price=ethereum_price)

    