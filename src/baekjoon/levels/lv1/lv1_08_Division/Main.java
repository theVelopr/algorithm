package baekjoon.levels.lv1.lv1_08_Division;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextInt();
        double b = sc.nextInt();
        if (a > 0 && b < 10){
            double c = a/b;
            System.out.println(c);
        }
        sc.close();
    }
}
