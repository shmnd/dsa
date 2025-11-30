class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        max_diagonal_sq = 0
        max_area_for_longest_diag = 0
        
        for length, width in dimensions:
            
            current_diagonal_sq = length * length + width * width
            
            current_area = length * width
            
            
            if current_diagonal_sq > max_diagonal_sq:
                max_diagonal_sq = current_diagonal_sq
                max_area_for_longest_diag = current_area
                
            elif current_diagonal_sq == max_diagonal_sq:
                if current_area > max_area_for_longest_diag:
                    max_area_for_longest_diag = current_area
                    
        return max_area_for_longest_diag

                



        
        