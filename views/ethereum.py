from flask import render_template, Blueprint, request, flash, redirect
from web3 import Web3
from views import INFURA_URL, MINERS, get_ethereum_price, get_bitcoin_price
import time, json, requests, re

ethereum_bp = Blueprint('ethereum', __name__)

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def history(address, block):
    return json.loads(requests.get(
        f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock={block}&endblock=999999999&sort=asc&apikey=EAVWKU25TNZCW9GCX4B6FIASNWU2D9CBK6"
    ).text)

@ethereum_bp.route("/address")
def address():
    address = request.args.get('address')
    block = request.args.get('block') if request.args.get('block') != '' and re.match(r'^([\s\d]+)$', request.args.get('block')) else 0

    ethereum_price = get_ethereum_price()
    bitcoin_price = get_bitcoin_price()
    
    try:
        address = w3.toChecksumAddress(address)
    except:
        flash('Invalid address', 'danger')
        return redirect('/')

    balance = w3.eth.get_balance(address)

    balance = w3.fromWei(balance, 'ether')
    try_time_stamp = history(address, block)
    from datetime import datetime
    try:
        for item in try_time_stamp['result']:
            item['timeStamp'] = datetime.utcfromtimestamp(int(item['timeStamp'])).strftime('%d/%m/%Y %H:%M:%S')
    except Exception as e:
        flash('An error occurred while formatting timestamp!', 'danger')
        return redirect('/')
    
    return render_template('ethereum/address.html', 
                        ethereum_price=ethereum_price, 
                        bitcoin_price=bitcoin_price,
                        address=address, 
                        balance=balance,
                        history=try_time_stamp)

@ethereum_bp.route("/block/<block_number>")
def block(block_number):
    block = w3.eth.get_block(int(block_number))
    return render_template('ethereum/block.html', block=block, ethereum_price=get_ethereum_price(), bitcoin_price=get_bitcoin_price())

@ethereum_bp.route('/transaction/<hash>')
def transaction(hash):
    tx = w3.eth.get_transaction(hash)
    value = w3.fromWei(tx.value, 'ether')
    receipt = w3.eth.get_transaction_receipt(hash)
    ethereum_price = get_ethereum_price()
    bitcoin_price = get_bitcoin_price()

    gas_price = w3.fromWei(tx.gasPrice, 'ether')

    return render_template('ethereum/transaction.html', 
                            tx=tx, 
                            value=value, 
                            receipt=receipt, 
                            gas_price=gas_price, 
                            ethereum_price=ethereum_price, 
                            bitcoin_price=bitcoin_price)

    