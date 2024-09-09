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

Install `uv`, an extremely fast Python package and project manager

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install Brownie

```sh
uv add eth-brownie
```

Compile the contract

```sh
uv run brownie compile
```

Run a blockchain simulation (foundry/hardhat) on port **8545**.

Test the contract

```sh
uv run brownie test
```

Deploy the contract

```sh
uv run brownie run deploy.py
```
