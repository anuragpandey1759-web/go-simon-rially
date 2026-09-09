class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only one row or rows are greater than string length
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        direction = 1  # 1 means moving down, -1 means moving up

        for char in s:
            rows[current_row] += char

            # Change direction at the top or bottom row
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        # Join all rows together
        return "".join(rows)