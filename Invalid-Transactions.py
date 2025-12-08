1class Solution:
2    def invalidTransactions(self, transactions: List[str]) -> List[str]:
3        # name -> list[ (timestamp, city, transaction_index) ]
4        from collections import defaultdict
5        history = defaultdict(list)
6        invalid_transactions = []
7        invalid_idTracker = set()
8
9        for index, transaction in enumerate(transactions):
10            name, timestamp, amount, city = transaction.split(',')
11            
12            if int(amount) > 1000 and index not in invalid_idTracker:
13                invalid_transactions.append(transaction)
14                invalid_idTracker.add(index)
15
16            if name in history:
17                for prev_timestamp, prev_city, prev_index in history[name]:
18                    if prev_city != city and int(prev_timestamp) - 60 <= int(timestamp) <= int(prev_timestamp) + 60:
19                        if prev_index not in invalid_idTracker:
20                            invalid_transactions.append(transactions[prev_index])
21                            invalid_idTracker.add(prev_index)
22                        if index not in invalid_idTracker:
23                            invalid_transactions.append(transaction)
24                            invalid_idTracker.add(index)
25
26            history[name].append((timestamp, city, index))
27        
28        return invalid_transactions