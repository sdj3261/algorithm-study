//기존 풀이 -- O(n2)

// class Solution {
//     public int maxProfit(int[] prices) {
//         int ret = 0;
//
//         for(int i=0; i<prices.length-1; i++) {
//             for(int j=i+1; j<prices.length; j++) {
//                 ret = Math.min(prices[i]-prices[j], ret);
//             }
//         }
//         if(ret >= 0) {
//             ret = 0;
//         }
//         return -ret;
//     }
// }

//O(n)으로 바꿔보자

class Solution {
    public int maxProfit(int[] prices) {
        int ret = 0;
        int minPrice = Integer.MAX_VALUE;
        if(prices.length == 1) {
            return 0;
        }

        for(int p : prices) {
            if(p < minPrice) {
                minPrice = p;
            } else {
                ret = Math.max(ret, p - minPrice)
            }
        }
    }
}