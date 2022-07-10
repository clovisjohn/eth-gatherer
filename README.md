# eth-gatherer
A script to bulk send eth from multiples wallets to one

## Requirement
* Python 3+
* web3 python library
* rpc url


## Installation
```
git clone https://github.com/clovisjohn/eth-gatherer.git
```

Add your infura project id in variables.py

## Usage
You can run this script by using `main.py pkeys_file recipient rpc`

### Arguments
- pkeys_file: the file containing the pkeys of the wallets you want to send from, one wallet per line. Example file provided in the repo


- recipient: the ethereum to send where you want to gather eth

- rpc: the url of the rpc you wanna use. Ex: https://mainnet.infura.io/v3/<infura-id>
  
               
### Example

```
main.py pkeys.txt 0xA5d31a3Ed981eC2fC2b10987Be0dD04Dfc6b8c38 https://mainnet.infura.io/v3/<infura-id>
```

## Colab workflow
```
!git clone https://github.com/clovisjohn/eth-gatherer.git
!pip install web3
!python /content/crypto-gatherer/main.py pkeys_file recipient rpc
