from flask import render_template, Blueprint, request, redirect
from web3 import Web3
from views import INFURA_URL, MINERS, get_ethereum_price, get_bitcoin_price
import time

home_bp = Blueprint('home', __name__)

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

@home_bp.route('/')
def home():
    eth = w3.eth

    ethereum_price = get_ethereum_price()
    bitcoin_price = get_bitcoin_price()


    latest_blocks = []
    for block_number in range(eth.block_number, eth.block_number-5, -1):
        block = eth.get_block(block_number)
        latest_blocks.append(block)

    latest_transactions = []
    for tx in latest_blocks[-1]['transactions'][-5:]:
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