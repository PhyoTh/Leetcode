class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vector = vec
        self.cur_row = 0
        self.cur_col = -1
        self.advance_next()
    
    def advance_next(self):
        while self.cur_row < len(self.vector) and len(self.vector[self.cur_row]) == 0:
            self.cur_row += 1
            self.cur_col = -1

    def next(self) -> int:
        # edge cases        
        self.cur_col += 1

        if self.cur_col == len(self.vector[self.cur_row]):
            self.cur_row += 1
            self.advance_next()
            self.cur_col = 0

        return self.vector[self.cur_row][self.cur_col]

    def hasNext(self) -> bool:
        if self.cur_row < len(self.vector):
            if self.cur_col + 1 < len(self.vector[self.cur_row]):
                return True
            
            r = self.cur_row + 1
            while r < len(self.vector) and len(self.vector[r]) == 0:
                r += 1
            return r < len(self.vector)
        return False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()