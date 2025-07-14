import java.io.*;
import java.util.*;

public class Solution {

    public static int getOptimalTeamSize(List<Integer> lowerSkill, List<Integer> higherSkill) {
        int n = lowerSkill.size();
        int left = 0, right = n;
        int answer = 0;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (canFormTeam(mid, lowerSkill, higherSkill)) {
                answer = mid;
                left = mid + 1;  // Try a larger team
            } else {
                right = mid - 1; // Try smaller team
            }
        }

        return answer;
    }

    private static boolean canFormTeam(int k, List<Integer> lowerSkill, List<Integer> higherSkill) {
        int count = 0;
        int n = lowerSkill.size();

        for (int i = 0; i < n; i++) {
            int lowerLimit = lowerSkill.get(i);
            int higherLimit = higherSkill.get(i);

            // Count is current position in team (people with lower skill)
            // Remaining in team = k - count - 1
            if (lowerLimit >= count && higherLimit >= (k - count - 1)) {
                count++;
            }

            if (count == k) return true;
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        // Read input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<Integer> lowerSkill = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            lowerSkill.add(Integer.parseInt(br.readLine()));
        }

        List<Integer> higherSkill = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            higherSkill.add(Integer.parseInt(br.readLine()));
        }

        int result = getOptimalTeamSize(lowerSkill, higherSkill);
        System.out.println(result);
    }
}
