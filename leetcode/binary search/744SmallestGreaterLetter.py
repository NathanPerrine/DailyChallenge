def nextGreatestLetter(letters: list[str], target: str) -> str:
        l, r = 0, len(letters) -1

        while (l < r -1):
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid
            elif letters[mid] > target:
                r = mid
        
        if letters[l] > target:
            return letters[l]
        else:
            if letters[r] > target:
                return letters[r]
            else:
                return letters[0]

l = ["c","f","j"]
t = "a"
print(nextGreatestLetter(l, t))