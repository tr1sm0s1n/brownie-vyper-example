import pytest
from brownie import Cert, accounts, reverts

@pytest.fixture
def cert():
    return Cert.deploy({'from': accounts[0], 'priority_fee': 10, 'max_fee': 1000000000})

def test_deploy(cert):
    assert cert.tx.status == 1


def test_issue(cert):
    trx = cert.issue(256, 'Raven', 'Arcane', 'S', '2031-01-01',
                     '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f', {'from': accounts[0], 'priority_fee': 10, 'max_fee': 1000000000})
    assert trx.events['Issued'].values() == [256, 'Arcane', '2031-01-01']


def test_read(cert):
    cert.issue(512, 'Serpent', 'Umbra', 'S', '2031-01-02',
                     '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f', {'from': accounts[0], 'priority_fee': 10, 'max_fee': 1000000000})
    certificate = cert.Certificates(512)
    assert certificate['name'] == 'Serpent'
    assert certificate['course'] == 'Umbra'
    assert certificate['grade'] == 'S'
    assert certificate['date'] == '2031-01-02'
    assert certificate['document'] == '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f'


def test_revert(cert):
    with reverts('Not Authorized'):
        trx = cert.issue(1024, 'Enfer', 'Catalyst', 'S', '2031-01-03',
                   '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f', {'from': accounts[1], 'priority_fee': 10, 'max_fee': 1000000000})
