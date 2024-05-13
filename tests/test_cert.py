from brownie import Cert, accounts, reverts
cert = None

def test_deploy():
    global cert
    cert = Cert.deploy({'from': accounts[0], 'priority_fee': 10, 'max_fee': 1000000000})
    assert cert.tx.status == 1


def test_issue():
    trx = cert.issue(256, 'Raven', 'MBCC', 'S', '2031-01-01',
                     '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f', {'from': accounts[0], 'priority_fee': 10, 'max_fee': 1000000000})
    assert trx.events['Issued'].values() == [256, 'MBCC', '2031-01-01']


def test_read():
    certificate = cert.Certificates(256)
    assert certificate['name'] == 'Raven'
    assert certificate['course'] == 'MBCC'
    assert certificate['grade'] == 'S'
    assert certificate['date'] == '2031-01-01'
    assert certificate['document'] == '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f'


def test_revert():
    with reverts('Not Authorized'):
        trx = cert.issue(256, 'Enfer', 'MBCC', 'S', '2031-01-01',
                   '0x2f44454d59535449462f6e6578742d63657274696669636174652d646170702f', {'from': accounts[1], 'priority_fee': 10, 'max_fee': 1000000000})

