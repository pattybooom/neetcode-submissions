class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += s + "|"
        return enc + str(len(strs))



    def decode(self, s: str) -> List[str]:
        
        dec = s.split("|")
        if dec[len(dec) -1] == 0:
            return []
        dec.pop()
        return dec
