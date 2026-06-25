class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arr = [1 if x == target else -1 for x in nums]

        pref = [0]
        s = 0
        for x in arr:
            s += x
            pref.append(s)

        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        m = len(vals)
        bit = [0] * (m + 1)

        def update(i):
            while i <= m:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0

        for p in pref:
            r = rank[p]
            ans += query(r - 1)   # count previous prefix sums < p
            update(r)

        return ans