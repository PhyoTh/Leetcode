class Solution(object):
    def countBlackBlocks(self, m, n, coordinates):
        # optimized: only checking the potential blocks
        def get_valid_blocks(row, col):
            valid_blocks = []
            for x, y in [(row-1, col-1), (row-1, col), (row, col-1), (row, col)]:
                if 0 <= x < m-1 and 0 <= y < n-1:
                    valid_blocks.append((x,y))
            return valid_blocks

        blocks_map = {} # {(pivot row, pivot col): # of black cells}
        for row, col in coordinates:
            valid_blocks = get_valid_blocks(row, col)
            for x, y in valid_blocks:
                blocks_map[(x,y)] = blocks_map.get((x,y), 0) + 1
        
        result = [0] * 5
        counter = 0 # count num of blocks that has at least 1 black cell
        for black_cell_counter in blocks_map.values():
            result[black_cell_counter] += 1
            counter += 1
        result[0] = (m-1) * (n-1) - counter
        return result
            
        # un-optimized
    #     coordinates_set = set()
    #     for row, col in coordinates:
    #         coordinates_set.add((row, col))

    #     result = [0] * 5
    #     for row in range(m - 1):
    #         for col in range(n - 1):
    #             num_black_cells = self.containBlackCell(row, col, coordinates_set)
    #             result[num_black_cells] += 1
    #     return result
    
    # # sub-function that will be passed in to check one block
    # # return how many blackcells are there in this block
    # def containBlackCell(self, i, j, coordinates_set):
    #     black_cell_counter = 0
    #     for row, col in [[i, j], [i+1, j], [i, j+1], [i+1, j+1]]:
    #         if (row, col) in coordinates_set:
    #             black_cell_counter += 1
    #     return black_cell_counter