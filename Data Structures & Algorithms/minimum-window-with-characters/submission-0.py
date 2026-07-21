class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        
        for char in t:
            freq[char]+=1
        track = defaultdict(int)
        i=0
        j=0
        start =-1
        end=-1
        min_len=len(s)
        
        while j<len(s):
            
            if freq[s[j]] > 0:
                track[s[j]]+=1

            while i<j and (freq[s[i]]==0 or track[s[i]]>freq[s[i]]):
                if track[s[i]]>freq[s[i]]:
                    track[s[i]]-=1
                i+=1

            
            if all([ track[char]>=freq[char] for char in freq ]):
                if j-i+1<= min_len:
                    start=i
                    end=j
                    min_len = j-i+1
            j+=1

        if start ==-1:
            return ""
        return s[start:end+1]
        