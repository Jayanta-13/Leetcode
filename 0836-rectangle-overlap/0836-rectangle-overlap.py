class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Unpack coordinates
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        # Two rectangles overlap if they overlap on both X and Y axes
        x_overlap = min(x2, x4) > max(x1, x3)
        y_overlap = min(y2, y4) > max(y1, y3)
        
        return x_overlap and y_overlap
        