class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_remain = [[0] * self.k for _ in range(4 * self.n)]
        self._build(nums, 0, 0, self.n - 1)

    def _merge(self, left_idx: int, right_idx: int, node: int):
        # Merge product
        self.tree_prod[node] = (self.tree_prod[left_idx] * self.tree_prod[right_idx]) % self.k

        # Merge remain counts
        # 1. Take all prefix products contained in left child
        for r in range(self.k):
            self.tree_remain[node][r] = self.tree_remain[left_idx][r]

        # 2. Add prefix products extending into right child
        l_prod = self.tree_prod[left_idx]
        for r in range(self.k):
            count = self.tree_remain[right_idx][r]
            if count > 0:
                new_rem = (l_prod * r) % self.k
                self.tree_remain[node][new_rem] += count

    def _build(self, nums: List[int], node: int, l: int, r: int):
        if l == r:
            rem = nums[l] % self.k
            self.tree_prod[node] = rem
            self.tree_remain[node][rem] = 1
            return

        mid = (l + r) // 2
        self._build(nums, 2 * node + 1, l, mid)
        self._build(nums, 2 * node + 2, mid + 1, r)
        self._merge(2 * node + 1, 2 * node + 2, node)

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            rem = val % self.k
            self.tree_prod[node] = rem
            self.tree_remain[node] = [0] * self.k
            self.tree_remain[node][rem] = 1
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node + 1, l, mid, idx, val)
        else:
            self.update(2 * node + 2, mid + 1, r, idx, val)
            
        self._merge(2 * node + 1, 2 * node + 2, node)

    def query(self, node: int, l: int, r: int, ql: int, qr: int):
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_remain[node]

        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * node + 1, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * node + 2, mid + 1, r, ql, qr)

        left_prod, left_remain = self.query(2 * node + 1, l, mid, ql, qr)
        right_prod, right_remain = self.query(2 * node + 2, mid + 1, r, ql, qr)

        res_prod = (left_prod * right_prod) % self.k
        res_remain = list(left_remain)

        for r_rem in range(self.k):
            count = right_remain[r_rem]
            if count > 0:
                new_rem = (left_prod * r_rem) % self.k
                res_remain[new_rem] += count

        return res_prod, res_remain


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        st = SegmentTree(nums, k)
        res = []

        for idx, val, start, target_x in queries:
            st.update(0, 0, n - 1, idx, val)
            _, remain_counts = st.query(0, 0, n - 1, start, n - 1)
            res.append(remain_counts[target_x])

        return res
        