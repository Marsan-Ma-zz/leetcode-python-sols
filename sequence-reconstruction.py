# https://leetcode.com/problems/sequence-reconstruction/

# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

# Example 1:

# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]

# Output:
# false

# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
# Example 2:

# Input:
# org: [1,2,3], seqs: [[1,2]]

# Output:
# false

# Explanation:
# The reconstructed sequence can only be [1,2].
# Example 3:

# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

# Output:
# true

# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
# Example 4:

# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

# Output:
# true


from collections import defaultdict

class Solution(object):


    # another solution, only verify all consecutive seqence
    def sequenceReconstruction(self, org, seqs):
        index = {num: i for i, num in enumerate([None] + org)}
        pairs = set(zip([None] + org, org))
        for seq in seqs:
            for a, b in zip([None] + seq, seq):
                if index[a] >= index.get(b, 0):
                    return False
                pairs.discard((a, b))
        return not pairs
        

    # topological sort with only 1 sol check
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        
        # [Examples]
        # org: [1,2,3], seqs: [[1,2],[1,3]] => False
        # org: [1,2,3], seqs: [[1,2]] => False
        # org: [1,2,3], seqs: [[1,2],[1,3],[2,3]] => True
        # org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]] => True
        
        # [Ideas]
        # 1. topological sort, but allow 1 solition only
        # 2. construct graph with defaultdict => reconstruct 
        
        suc, pre = defaultdict(set), defaultdict(set)
        for seq in seqs:
            for n1, n2 in zip(seq, seq[1:]):
                suc[n1].add(n2)
                pre[n2].add(n1)
                
        all_1 = set(org)
        all_2 = set([j for k in seqs for j in k])
        if all_1 != all_2: return False
    
        free = list(all_1 - set(pre))
        # print(free, suc, pre)
        
        sol = []
        while free:
            if len(free) > 1: return False
            n = free.pop()
            sol.append(n)
            for s in suc[n]:
                pre[s].remove(n)
                if not pre[s]:
                    free.append(s)
        # print("cmp:", sol, org)     
        return sol == org
    
    
    def test(self):
        cases = [
            # ("", ""),
            # ([1], []),
            # ([1,2,3], [[1,2],[1,3]]),
            # ([1,2,3], [[1,2]]),
            ([1,2,3], [[1,2],[1,3],[2,3]]),
            # ([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]]),
        ]
        for org, seqs in cases:
            print(org, seqs, self.sequenceReconstruction(org, seqs))
            
            
# Solution().test()