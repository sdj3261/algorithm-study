class Solution {
    static int[][] arr;
    public int solution(int n, int w, int num) {
        arr = new int[n/w+1][w];
        int count = 1;

        for (int i = 0; i < arr.length; i++) {
            for(int j=0;j<arr[i].length;j++) {
                if (i % 2 == 0) {
                    arr[i][j] = count;
                } else {
                    arr[i][w-1-j] = count;
                }
                count++;
                if (count > n) {
                    break;
                }
            }
            //만약 카운팅이 너무커지면 break
            if (count > n) {
                break;
            }
        }

        int maxHeight = 0;
        int heightX = 0;
        int heightY = 0;
        for(int i=0; i<arr.length; i++) {
            for(int j=0;j<arr[i].length;j++) {
                //만약 찾으려는 숫자라면 height 카운팅
                if(arr[i][j] == num) {
                    heightX = j;
                    heightY = i;
                }
                //갱신한다.
                if(heightX == j && arr[i][j] != 0) {
                    maxHeight = Math.max(i+1,heightY);
                }
            }
        }

        for(int i=0; i<arr.length; i++) {
            for(int j=0;j<arr[i].length;j++) {
                //만약 찾으려는 숫자라면 height 카운팅
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println(heightY);
        System.out.println(maxHeight);
        return maxHeight-heightY;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(13,3,6));
    }
}