package baekjoon.levels.lv1.lv1_05_Addition;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //todo find the reason why it is a compile error. [v]
        // - I didn't put import in the submission.

        /*
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = a + b;
        System.out.println(c);
        */

        int a = scanner.nextInt();
        int b = scanner.nextInt();

        System.out.println(a+b);
        scanner.close();
    }
}
