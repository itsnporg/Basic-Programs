import java.util.Scanner;
import java.util.Random;

class PasswordGenerator {

    public static void main(String args[]) {
        String upChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; //All Uppercase Characters.
        String lowChars = "abcdefghijklmnopqrstuvwxyz";//All Lowercase Characters.
        String nums = "1234567890"; //All Numbers.
        String symbols = "!@#$%^&*()_., <>?/"; //All Symbols.

        String passChars = (upChars + lowChars + symbols + nums); //Concatenating all the above characters.

        System.out.print("Your Password is: " + String.valueOf(generate(passChars))); //Displaying the generated password.
    }

    static char[] generate(String passChars) {
        Random rand = new Random();
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the length of your password: ");
        int length = sc.nextInt(); //Taking the length of password from the user.

        if(length < 5) {
            length = 5; //Assigning default length incase the length of password is too short.
            System.out.println("Length too short. Default length set to 5");
        }
        
        char pwd[] = new char[length];

        for(int i = 0; i < length; i++) {
            //Generates random numbers between 0 to the pwd length. Character at that index is inserted at ith index of the pwd array.
            pwd[i] = passChars.charAt(rand.nextInt(passChars.length()));
        }

        sc.close();
        return pwd;
    }

}