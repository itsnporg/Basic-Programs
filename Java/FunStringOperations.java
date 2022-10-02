    /**
    * A collection of fun string operation methods written in Java  
    * Author: jeslyw 
    */ 

    /**
    * Takes any string as an argument and returns the given string in reverse   
    */ 
    
    void wordReversal(String inputString) {
        String[] arrayOfStrings = inputString.split(" ");
        String[] newArrayOfStrings = new String[arrayOfStrings.length];
        for (int i = 0; i < newArrayOfStrings.length; i++) {
            newArrayOfStrings[i] = arrayOfStrings[(arrayOfStrings.length - 1) - i];
        }
        String reversedString = "";
        for (int i = 0; i < newArrayOfStrings.length; i++) {
            reversedString = reversedString + newArrayOfStrings[i] + " ";
        }
        System.out.println(reversedString);
    }

    /**
    * Takes any string and a numerical (n-th) position as arguments and returns the exact 
    * word at that position     
    * n = an integer starting from 1 
    */ 

    void returnNthWord(String string, int n) {
        String[] arrayStrings = string.split(" ");
        if (n > arrayStrings.length){
            throw new ArrayIndexOutOfBoundsException("index greater than number of words");
        }
        System.out.println(arrayStrings[n-1]);

    }

    /**
    * Takes any two strings as arguments and checks if both strings are anagrams of each other
    * Returns true or false
    */

    boolean isAnagram(String string1, String string2){
        if (string1.length() != string2.length()){
            return false;
        }
        int counter = 0;
        for (int i = 0; i < string1.length(); i++) {
            for (int j = 0; j < string2.length(); j++){
                if (string2.charAt(j) == string1.charAt(i)){
                    counter++;
                    break;
                }
            }
        }
        if (counter == string1.length()){ return true;}
        return false;
    }