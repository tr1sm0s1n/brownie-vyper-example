# Brownie-Vyper-Example

Example project to compile/test/deploy smart contracts written in Vyper using Brownie.

## 🛠 Built With

[![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)](https://www.python.org/)
[![Vyper Badge](https://img.shields.io/badge/Vyper-3C3C3D?logo=ethereum&logoColor=fff&style=for-the-badge)](https://docs.vyperlang.org/en/stable/)
[![Brownie Badge](https://img.shields.io/badge/Brownie-3C3C3D?logo=ethereum&logoColor=fff&style=for-the-badge)](https://eth-brownie.readthedocs.io/en/stable/)

## ⚙️ Run Locally

Clone the repository

```sh
git clone https://github.com/tr1sm0s1n/brownie-vyper-example
cd brownie-vyper-example
```

Create a virtual environment

```sh
python3 -m venv venv
```

Activate the environment

> For Linux

```sh
source ./venv/bin/activate
```

> For Windows PowerShell

```sh
.\venv\Scripts\Activate.ps1
```

Install Brownie

```sh
pip install eth-brownie
```

Compile the contract

```sh
brownie compile
```
Run a blockchain simulation (foundry/hardhat) on port **8545**.

Test the contract

```sh
brownie test
```

Deploy the contract

```sh
brownie run deploy_cert.py
```
