# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 19:54:15 2022

@author: John
"""
import sys
from web3 import Web3

if len(sys.argv) < 2:
    raise ValueError('Please provide arguments')
    
pkey_list = sys.argv[1]
to_addy = sys.argv[2]

print(type(to_addy))
#######################################################################################################
rpc = 'https://mainnet.infura.io/v3/81e29f26b36d418fb1c01cc9f4ca0e95'
web3 = Web3(Web3.HTTPProvider(rpc))


def sendEth (pkey,to) :
    origin = web3.eth.account.privateKeyToAccount(pkey).address
    nonce = web3.eth.getTransactionCount(origin)
    
    balance = web3.eth.getBalance(origin)
    if balance > 2*21000*web3.eth.gas_price :
        #build a transaction in a dictionary
        tx = {
        'nonce': nonce,
        'to': to,
        'value': (balance - 2*21000*web3.eth.gas_price),
        'gas': 21000,
        'gasPrice': web3.eth.gas_price
        }
        
        signed_tx = web3.eth.account.sign_transaction(tx, pkey)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(web3.toHex(tx_hash))
    else:
        print('low eth in wallet')

###############################################################################################

with open(pkey_list,'r') as pkeys :
    for pkey in pkeys :
        pkey=pkey.strip()
        sendEth(pkey, to_addy)