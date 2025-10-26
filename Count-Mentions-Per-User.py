class Solution:
    from typing import Union
    from collections import defaultdict, deque

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mention_counts = [0] * numberOfUsers
        inactivity_log = defaultdict(set) # {start_timestamp_of_inactivity (key): set()}
        mention_queue = deque()

        for event in events:
            event_type, timestamp, id_string = event[0], event[1], event[2]

            if event_type == "MESSAGE":
                if id_string == "ALL":
                    self.count_up(mention_counts, set())
                else:
                    mention_queue.append(event)

            elif event_type == "OFFLINE":
                inactivity_log[timestamp].add(int(id_string))
        
        while mention_queue:
            _ , timestamp, id_string = mention_queue.popleft()

            inactive_users = set()
            self.populate_inactive(timestamp, inactive_users, inactivity_log)

            if id_string == "HERE":
                self.count_up(mention_counts, inactive_users)
            else:
                mentions_string = id_string.split(" ")
                for user_id in mentions_string:
                    get_id = int(user_id[2:])
                    mention_counts[get_id] += 1

        return mention_counts
    
    def count_up(self, mention_counts: list[int], inactive_users: set[int]):
        for user_id in range(len(mention_counts)):
            if user_id in inactive_users:
                continue
            mention_counts[user_id] += 1
    
    def populate_inactive(self, timestamp: str, inactive_users: set, inactivity_log: defaultdict(set)):
        for start_inactive, user_ids in inactivity_log.items():
                if int(start_inactive) <= int(timestamp) < int(start_inactive) + 60:
                    for user_id in user_ids:
                        inactive_users.add(user_id)