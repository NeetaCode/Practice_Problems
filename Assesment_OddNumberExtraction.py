public class GreatestOddNumberFinder {

    public static void main(String[] args) {
        String input = "mkf43kd1cmk32k1mv123";
        System.out.println("Input: " + input);
        int result = findGreatestOddNumber(input);
        System.out.println("Greatest odd number: " + result);
    }

    public static int findGreatestOddNumber(String input) {
        int maxOdd = -1;
        StringBuilder number = new StringBuilder();

        for (char c : input.toCharArray()) {
            if (Character.isDigit(c)) {
                number.append(c);
            } else {
                if (number.length() > 0) {
                    int value = Integer.parseInt(number.toString());
                    if (value % 2 == 1 && value > maxOdd) {
                        maxOdd = value;
                    }
                    number.setLength(0); // clear for next number
                }
            }
        }

        // Check if the string ends with a number
        if (number.length() > 0) {
            int value = Integer.parseInt(number.toString());
            if (value % 2 == 1 && value > maxOdd) {
                maxOdd = value;
            }
        }

        return maxOdd;
    }
}
