1struct Node {
2    short min, max, lazy;
3    Node():min(SHRT_MAX), max(SHRT_MIN), lazy(0) {}
4    Node(int x): min(x), max(x), lazy(0) {}
5};
6
7class SegmentTree {
8public:
9    vector<Node> segTree;
10    unsigned n;
11
12    SegmentTree(vector<int>& arr) {
13        n=arr.size();
14        // 1-indexed segment tree
15        segTree.assign(n<<2, Node());
16        buildTree(1, 0, n-1, arr);
17    }
18
19    // Pulls values from children up to the parent
20    void pull(int i) {
21        segTree[i].min=min(segTree[2*i].min, segTree[2*i+1].min);
22        segTree[i].max=max(segTree[2*i].max, segTree[2*i+1].max);
23    }
24
25    void buildTree(int i, int l, int r, vector<int>& arr) {
26        if (l==r) {
27            segTree[i]=Node(arr[l]);
28            return;
29        }
30        int m=(l+r)>>1;
31        buildTree(2*i, l, m, arr);
32        buildTree(2*i+1, m+1, r, arr);
33        pull(i);
34    }
35
36    void apply(int i, int l, int r) {
37        if (segTree[i].lazy==0) return;
38        segTree[i].min+=segTree[i].lazy;
39        segTree[i].max+=segTree[i].lazy;
40        if (l<r) {
41            segTree[2*i].lazy+=segTree[i].lazy;
42            segTree[2*i+1].lazy+=segTree[i].lazy;
43        }
44        segTree[i].lazy=0;
45    }
46
47    void updateRange(int start, int end, int i, int l, int r, int val) {
48        apply(i, l, r);
49        if (l>end || r<start) return;
50
51        if (l>=start && r<=end) {
52            segTree[i].lazy+= val;
53            apply(i, l, r);
54            return;
55        }
56
57        int m=(l+r)>>1;
58        updateRange(start, end, 2*i, l, m, val);
59        updateRange(start, end, 2*i+1, m+1, r, val);
60        pull(i);
61    }
62
63    int findLast0(int i, int l, int r) {
64        apply(i, l, r);
65        // if 0 isn't within [min, max], no 0
66        if (segTree[i].min>0|| segTree[i].max<0) return -1;
67
68        if (l==r) return l;
69
70        int m=(l+r)>>1;
71        // To find the index for the last 0, 
72        // search the right child first
73        int right=findLast0(2*i+1, m+1, r);
74        if (right!=-1) return right;
75        return findLast0(2*i, l, m);
76    }
77};
78
79constexpr int N=1e5+1;
80bitset<N> seen=0;
81class Solution {
82public:
83    static int longestBalanced0(vector<int>& nums) {
84        const int n=nums.size();
85        int len=0;
86        for(int l=0; l<n; l++){
87            if (l>n-len) break;// len cannot be longer
88            int diff=0;
89            for(int r=l; r<n; r++){
90                const int x=nums[r];
91                if (!seen[x]) {diff+=(1-(x&1)*2), seen[x]=1; }
92                if (diff==0)
93                    len=max(len, r-l+1);
94            }
95            for(int i=l; i<n; i++) seen[nums[i]]=0;
96        }
97        return len;
98    }
99    static int longestBalanced(vector<int>& nums) {
100        const int n=nums.size();
101        if (n<=2000) return longestBalanced0(nums);
102
103        const int M=*max_element(nums.begin(), nums.end());
104        vector<int> last(M+1, n);
105        vector<int> nextPos(n, n);
106        for (int i=n-1; i>= 0; i--) {
107            const int x=nums[i];
108            nextPos[i]=last[x];
109            last[x]=i;
110        }
111
112        // Compute prefix sums 
113        vector<int> prefix(n);
114        int sum=0;
115        for (int i=0; i<n; i++) {
116            const int x=nums[i];
117            if (!seen[x]) {
118                sum+=(x&1)?1:-1;
119                seen[x]=1;
120            }
121            prefix[i]=sum;
122        }
123        // reset for the next testcase
124        for(int i=0; i<n; i++) seen[nums[i]]=0;
125
126        SegmentTree seg(prefix);
127        
128        int ans=seg.findLast0(1, 0, n-1)+1;
129
130        for (int i=0; i<n-1; i++) {
131            int r=nextPos[i]-1;
132            // Only update if the range is valid
133            if (i+1<=r) {
134                int val=(nums[i] & 1)?-1:1;
135                seg.updateRange(i+1, r, 1, 0, n-1, val);
136            }
137
138            // Only search if a better answer is possible
139            if (i+ans+1<n) {// this check saves half of time
140                int right=seg.findLast0(1, 0, n-1);
141                if (right!=-1) 
142                    ans=max(ans, right-i);
143            }
144        }
145        return ans;
146    }
147};
148auto init = []() {
149    ios::sync_with_stdio(0);
150    cin.tie(0);
151    cout.tie(0);
152    return 'c';
153}();