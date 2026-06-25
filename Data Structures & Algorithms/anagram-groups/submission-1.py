class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            if str(sorted(s)) in ans:
                ans[str(sorted(s))].append(s)
            else:
                ans[str(sorted(s))] = [s]
                answer = []
        for an in ans:
            answer.append(ans[an])
        return answer


        