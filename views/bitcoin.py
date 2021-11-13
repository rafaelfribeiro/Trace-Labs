from flask import render_template, Blueprint, request, redirect, flash
from web3 import Web3
from views import INFURA_URL, MINERS, get_ethereum_price, get_bitcoin_price
import codecs,time, re, requests, json
from hashlib import sha256
from blockcypher import get_address_details, from_base_unit

bitcoin_bp = Blueprint('bitcoin', __name__)

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

@bitcoin_bp.route('/bitcoin/address')
def bitcoin():
    address = request.args.get('address')
    block = request.args.get('block') if request.args.get('block') != '' and re.match(r'^([\s\d]+)$', request.args.get('block')) else 0

    ethereum_price = get_ethereum_price()
    bitcoin_price = get_bitcoin_price()

    


    address_info = get_address_details(address)
    balance = from_base_unit(address_info['balance'], 'btc')

    return render_template('bitcoin/address.html', 
                        ethereum_price=ethereum_price, 
                        bitcoin_price=bitcoin_price,
                        address=address, 
                        address_info=address_info,
                        balance=balance)
                        
# def get_balance(address):
#     return json.loads(requests.get(
#         f"https://api.blockcypher.com/v1/btc/main/addrs/{address}"
#     ).text)

