class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        # construct flights map and cost lookup
        from collections import defaultdict
        flights_cost = {}
        flights_map = defaultdict(set)
        for from_city, to_city, cost in flights:
            flights_cost[(from_city, to_city)] = cost
            flights_map[from_city].add(to_city)
        
        import heapq
        explore = [(0, src, k+1)] # (accumulated_cost, city, stops remaining)
        cost_map = {(src, k+1): 0} # city : accumulated cost

        while len(explore) != 0:
            current_cost, current_city, current_stop = heapq.heappop(explore)
            if current_city == dst:
                return current_cost
            if current_stop == 0: # no more stops left
                continue

            neighbor_cities_set = flights_map[current_city]
            for neighbor_city in neighbor_cities_set:
                new_cost = current_cost + flights_cost[(current_city, neighbor_city)]
                new_state = (neighbor_city, current_stop - 1)

                if new_cost < cost_map.get(new_state, float('inf')):
                    cost_map[new_state] = new_cost
                    heappush(explore, (new_cost, neighbor_city, current_stop-1))

        return -1