# Brownie-Vyper-Example

Example project to compile/test/deploy smart contracts written in Vyper using Brownie.

## 🛠 Built With

<div align="left">
<a href="https://docs.python.org/3/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/DEMYSTIF/DEMYSTIF/main/assets/icons/python.svg" width="36" height="36" alt="Python" /></a>
<a href="https://eth-brownie.readthedocs.io/en/stable/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/DEMYSTIF/DEMYSTIF/main/assets/icons/ethereum.svg" width="36" height="36" alt="Ethereum" /></a>
<a href="https://docs.vyperlang.org/en/stable/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/DEMYSTIF/DEMYSTIF/main/assets/icons/vyper.svg" width="36" height="36" alt="Vyper" /></a>
</div>

## ⚙️ Run Locally

Clone the repository

```bash
git clone https://github.com/DEMYSTIF/brownie-vyper-example
cd brownie-vyper-example
```

Install pipx

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Install Brownie using pipx

```bash
pipx install eth-brownie
```

Compile the contract

```bash
brownie compile
```

Test the contract

```bash
brownie test
```

Deploy the contract

```bash
brownie run deploy.py
```
