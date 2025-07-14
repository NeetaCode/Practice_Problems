import java.util.*;

public class Solution {

    public static int calculateTotalPrefix(String sequence, int k) {
        int countValid = 0;
        long count1s = 0;
        long count10s = 0;

        for (int i = 0; i < sequence.length(); i++) {
            char ch = sequence.charAt(i);

            if (ch == '1') {
                count1s++;
            } else if (ch == '0') {
                count10s += count1s;
            }

            if (count10s > k) {
                break;
            }

            if (count10s == k) {
                countValid++;
            } else if (count1s > 0 && (k - count10s) % count1s == 0) {
                countValid++;
            }
        }

        return countValid;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String sequence = scanner.nextLine().trim();
        int k = scanner.nextInt();
        scanner.close();

        System.out.println(calculateTotalPrefix(sequence, k));
    }
}
