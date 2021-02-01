package ee.taltech.iti0202.datastructures;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class DataStructures {
    private Map<String, Integer> students = new HashMap<>();
    /**
     * Given String is a sentence with some words.
     * There are only single whitespace between every word and no punctuation marks.
     * Also there are no capital letters in input string.
     * <p>
     * Return the longest word from the input sentence.
     * <p>
     * If there are more than one word with the same length then return the word which comes alphabetically first.
     * <p>
     * Hints:
     * You can split words into an array using "str.split()"
     * Sorting list with the longest words can definitely help you to find the word which comes alphabetically first.
     *
     * @param sentence input String to find the longest words
     * @return the longest String from input
     */
    public static String findLongestWord(String sentence) {
        String[] strArray = sentence.split(" ");
        int counter = 0;
        int i = 0;
        for (i = 0; i < strArray.length; i++) {
            if (strArray[i].length() > counter) {
                counter = strArray[i].length();
            }
        }
        List<String> biggest = new ArrayList<>();
        int j = 0;
        for (j = 0; j < strArray.length; j++) {
            if (strArray[j].length() == counter) {
                biggest.add(strArray[j]);
            }
        }
        if (biggest.size() > 1) {
            List<String> sortedBiggest = biggest.stream().sorted().collect(Collectors.toList());
            return sortedBiggest.get(0);
        }
        return biggest.get(0);

    }

    /**
     * Classic count the words exercise.
     * <p>
     * From input count all the words and collect results to map.
     *
     * @param sentence array of strings, can't be null.
     * @return map containing all word to count mappings.
     */
    public static Map<String, Integer> wordCount(String[] sentence) {
        int i = 0;
        Map<String, Integer> ret = new HashMap<>();
        for (i = 0; i < sentence.length; i++) {
            if (!(ret.containsKey(sentence[i]))) {
                ret.putIfAbsent(sentence[i], 0);
                int j = 0;
                for (j = 0; j < sentence.length; j++) {
                    if (sentence[j].equals(sentence[i])) {
                        int increase = 1;
                        ret.put(sentence[i], ret.get(sentence[i]) + increase);
                    }
                }
            }
        }
        return ret;
    }

    /**
     * Loop over the given list of strings to build a resulting list of string like this:
     * when a string appears the 2nd, 4th, 6th, etc. time in the list, append the string to the result.
     * <p>
     * Return the empty list if no string appears a 2nd time.
     * <p>
     * Use map to count times that the string has appeared.
     *
     * @param words input list to filter
     * @return list of strings matching criteria
     */
    public static List<String> onlyEvenWords(List<String> words) {
        List<String> ret = new ArrayList<>();
        Map<String, Integer> counter = new HashMap<>();
        int i = 0;
        for (i = 0; i < words.size(); i++) {
            if (counter.containsKey(words.get(i))) {
                counter.put(words.get(i), counter.get(words.get(i)) + 1);
            } else {
                counter.putIfAbsent(words.get(i), 1);
            }
        }
        int minimum = 2;
        for (Map.Entry<String, Integer> entry : counter.entrySet()) {
            if (entry.getValue() >= minimum) {
                int j = 0;
                for (j = 0; j < Math.floor(entry.getValue() / minimum); j++) {
                    ret.add(entry.getKey());
                }
            }
        }
        return ret;
    }


    /**
     * Method to save student and student's grade(you should use a Map here).
     * Only add student if his/hers grade is in the range of 0-5.
     *
     * @param studentInfo String with a pattern (name:grade)
     */
    public void addStudent(String studentInfo) {
        String[] studentInfoSplit = studentInfo.split(":");
        int grade = Integer.parseInt(studentInfoSplit[1]);
        int maxGrade = 5;
        if (grade >= 0 && grade <= maxGrade) {
            students.putIfAbsent(studentInfoSplit[0], grade);
        }

    }

    /**
     * Method to get student's grade.
     * Return the student's grade by his/hers name.
     * You can assume that the user is already added(previous function with student's info already called).
     *
     * @param name String students name
     * @return int student's grade.
     */
    public int getStudentGrade(String name) {
        int returnIfNoSuchStudent = -1;
        return students.getOrDefault(name, returnIfNoSuchStudent);


    }

    /**
     * Main.
     * @param args Commend line arguments.
     */
    public static void main(String[] args) {
        DataStructures dataStructures = new DataStructures();
        dataStructures.addStudent("Ago:5");
        dataStructures.addStudent("Martin:0");
        dataStructures.addStudent("Margo:3");
        dataStructures.addStudent("Cheater:6");

        System.out.println(dataStructures.getStudentGrade("Ago")); // 5
        System.out.println(dataStructures.getStudentGrade("Martin")); // 0
        System.out.println(dataStructures.getStudentGrade("Margo")); // 3
        System.out.println(dataStructures.getStudentGrade("Cheater")); // -1

    }
}
