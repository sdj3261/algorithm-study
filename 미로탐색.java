package algorithm.미로탐색;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Scanner;

public class Miro {
  static int[][] visited;
  static int[][] arr;
  static int[] dy = {-1,0,1,0};
  static int[] dx = {0,1,0,-1};


  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] input = br.readLine().split(" ");
    int n = Integer.parseInt(input[0]);
    int m = Integer.parseInt(input[1]);
    visited = new int[n][m];
    arr = new int[n][m];
    for (int i = 0; i < n; i++) {
      String temp = br.readLine();
      //arr에 담기
      for (int j = 0; j < m; j++) {
        arr[i][j] = temp.charAt(j) - '0';
      }
    }
    bfs(0, 0);
    System.out.println(visited[n - 1][m - 1]);
  }

  public static void bfs(int y, int x) {
    ArrayDeque<Point> queue = new ArrayDeque<>();
    queue.offerFirst((new Point(y,x)));
    visited[y][x] = 1;

    while (!queue.isEmpty()) {
      Point point = queue.pop();
      int py = point.y;
      int px = point.x;
      for(int k = 0; k < 4; k++) {
        int ny = py + dy[k];
        int nx = px + dx[k];

        if(ny < 0 || ny >= arr.length || nx < 0 || nx >= arr[0].length) {
          continue;
        }
        if(visited[ny][nx] > 0) {
          continue;
        }
        if(arr[ny][nx] == 0) {
          continue;
        }
        if(arr[ny][nx] == 1) {
          queue.offerFirst(new Point(ny, nx));
          visited[ny][nx] = visited[py][px] + 1;
        }
      }
    }
  }

  static class Point {
    public int y;
    public int x;
    public Point(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

}
