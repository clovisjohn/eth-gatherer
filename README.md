# eth-gatherer
A script to bulk send eth from multiple wallets to one

## Requirements
* Python 3+
* web3.py
* rpc url


## Installation
```
git clone https://github.com/clovisjohn/eth-gatherer.git
```


## Usage
You can run this script by using `main.py pkeys_file recipient rpc`

### Arguments
- pkeys_file: the file containing the private keys of the wallets you want to send from, one private key per line. Example file provided in the repo


- recipient: the ethereum address where you want to gather eth

- rpc: the url of the rpc you wanna use.
  
               
### Example
The execution of the next line will transfer to 0xB32E1E554901127d9734C58193fB44777482F258 all eth from the wallets whose private keys are in pkeys.txt
```
main.py pkeys.txt 0xB32E1E554901127d9734C58193fB44777482F258 https://mainnet.infura.io/v3/<infura-id>
```

## Colab workflow
```
!git clone https://github.com/clovisjohn/eth-gatherer.git
!pip install web3
!python /content/eth-gatherer/main.py pkeys_file recipient rpc
