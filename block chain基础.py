# {"index":""
# "timetape":""
# "transactions"：
# {
#    "senders":""
#    "recipent":""
#    "amount":""
#
# }
# "proof_work":""
# "previous_hash":""
# }
from time import time
import hashlib
import json
class blockchain:
    def __init__(self):
        self.chain = []  #前面的字典中的所有键值对,存放每一个区块
        self.current_transaction = [] #保存"transactions"中的交易信息
    def new_block(self,proof_work,previous_hash):
        block = {
            "index":len(self.chain)+1,
            "timetamp":time(),
            "transactions":self.current_transaction,
            "proof_work":proof_work,
            "previous_hash":previous_hash or hash(self.last_block) or hash(self.chain[-1])
        }
        self.chain.append(block)
        self.current_transaction = []
    def new_transaction(self,senders,recipents,amount):
        self.current_transaction.append(
            {
                "senders":senders,
                "recipents":recipents,
                "amount":amount
            }
        )
        return self.last_block['index']+1
    @staticmethod
    def hash(block):
        block_string = json.dumps(block)
        hashlib.sha224(block)
    @property
    def last_block(self):
        pass



