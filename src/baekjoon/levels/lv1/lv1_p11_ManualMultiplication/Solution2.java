package baekjoon.levels.lv1.lv1_p11_ManualMultiplication;

import java.util.Scanner;

public class Solution2 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();

        sc.close();

        System.out.println("Solution 2");
        System.out.println(A * (B % 10) + " (B % 10) equals to " + (B % 10));
        System.out.println(A * (B % 100/10)  + " (B % 100 / 10) equals to " + (B % 100/10));
        System.out.println(A * (B/100));
        System.out.println(A * B);
    }
}
