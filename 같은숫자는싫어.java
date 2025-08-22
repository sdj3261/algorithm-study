public class Solution {
    public int[] solution(int []arr) {
                int idx = 0;
                int len = arr.length;

                ArrayDeque<Integer> stack = new ArrayDeque<>();
                while (idx < len) {
                    if(!stack.isEmpty() && arr[idx] == stack.getLast()) {
                        idx++;
                        continue;
                    }
                    stack.addLast(arr[idx++]); ;
                }
                return stack.stream().mapToInt(Integer::intValue).toArray();
    }
}//d