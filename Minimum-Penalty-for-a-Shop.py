class Solution(object):
    '''
    N Y Y Y Y N N Y
    '''
    def bestClosingTime(self, customers):
        from collections import Counter
        count_customers = Counter(customers)
        total_penalty = count_customers["Y"] # number of Y's if we were to close on day 0
        min_penalty = (total_penalty, 0) # (penalty, close_hour)

        close_hour = 1
        while close_hour <= len(customers):
            # if we were to close the next hour, and customer doesn't come current hour
            if customers[close_hour-1] == "Y": 
                total_penalty -= 1
            if customers[close_hour-1] == "N": 
                total_penalty += 1
            close_hour += 1

            if total_penalty < min_penalty[0]:
                min_penalty = (total_penalty, close_hour-1)
        return min_penalty[1]

        # not optimized (O(n*n))
        '''
        min_penalty = (float('inf'), 0)

        close_hour = 0
        while close_hour <= len(customers):
            total_penalty = 0
            for hour, customer in enumerate(customers):
                if hour < close_hour: # before close
                    if customer == "N":
                        total_penalty += 1
                else: # after close
                    if customer == "Y":
                        total_penalty += 1
            if total_penalty < min_penalty[0]:
                min_penalty = (total_penalty, close_hour)
            close_hour += 1
        return min_penalty[1]
        '''