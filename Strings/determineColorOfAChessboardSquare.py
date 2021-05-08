class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if int(coordinates[1])%2==(ord(coordinates[0])-ord('a'))%2:
            return True
        else:
            return False