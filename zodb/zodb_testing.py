#zodb_testing.py

import sys
sys.path.append(r'C:\Users\mwhitten\brgusers\Python\testing\zodb')
import account

import BTrees.OOBTree
import ZODB, ZODB.FileStorage
import transaction

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

root.accounts = BTrees.OOBTree.BTree()
root.accounts['account-1'] = account.Account()
root.accounts['account-1'].deposit(50.0)

transaction.commit()
