package ee.taltech.iti0202.idcode;

import java.util.ArrayList;
import java.util.List;

public class IdCode {

    private final String idCodeValue;

    enum Gender {
        MALE, FEMALE
    }

    /**
     * Method returns the id code.
     *
     * @return id code.
     */
    public String getIdCodeValue() {
        return idCodeValue;
    }

    public IdCode(String idCodeValue) {
        this.idCodeValue = idCodeValue;
    }

    /**
     * Check if the id code is valid or not.
     *
     * @return boolean describing whether or not the id code was correct.
     */
    public boolean isCorrect() {
        if (!(isControlNumberCorrect() && isDayNumberCorrect() && isGenderNumberCorrect() && isYearNumberCorrect())){
            throw new IllegalArgumentException();
        } else {
            return true;
        }
    }

    /**
     * Get all information about id code.
     *
     * @return String containing information.
     */
    public String getInformation() {
        String gender = getGender().toString();
        return "This is a " + gender + " born on " + idCodeValue.substring(5, 7) + "." + idCodeValue.substring(3, 5)
                + "." + getFullYear() + " in " + getBirthPlace();
    }

    /**
     * Get gender enum.
     *
     * @return enum describing person's gender
     */
    public Gender getGender() {
        List<Character> men = new ArrayList<>(){{
            add('1');
            add('3');
            add('5');
        }};
        List<Character> women = new ArrayList<>(){{
            add('2');
            add('4');
            add('6');
        }};
        if (men.contains(idCodeValue.charAt(0))){
            return Gender.MALE;
        } else {
            return Gender.FEMALE;
        }


    }

    /**
     * Get person's birth location.
     *
     * @return String with the person's birth place.
     */
    public String getBirthPlace() {
        int numbers = Integer.parseInt(idCodeValue.substring(7, 10));
        String place = "unknown";
        if (0 < numbers && numbers <= 10) {
            place = "Kuressaare";
        } else if (11 <= numbers && numbers <= 20) {
            place = "Tartu";
        } else if (21 <= numbers && numbers <= 220) {
            place = "Tallinn";
        } else if (221 <= numbers && numbers <= 270) {
            place = "Kohtla-Järve";
        } else if (271 <= numbers && numbers <= 370) {
            place = "Tartu";
        } else if (371 <= numbers && numbers <= 420) {
            place = "Narva";
        } else if (421 <= numbers && numbers <= 470) {
            place = "Pärnu";
        } else if (471 <= numbers && numbers <= 490) {
            place = "Tallinn";
        } else if (491 <= numbers && numbers <= 520) {
            place = "Paide";
        } else if (521 <= numbers && numbers <= 570) {
            place = "Rakvere";
        } else if (571 <= numbers && numbers <= 600) {
            place = "Valga";
        } else if (601 <= numbers && numbers <= 650) {
            place = "Viljandi";
        } else if (651 <= numbers && numbers <= 710) {
            place = "Võru";
        } else if (710 <= numbers || numbers == 0) {
            place = "unknown";
        }
        return place;
    }

    /**
     * Get the year that the person was born in.
     *
     * @return int with person's birth year.
     */
    public int getFullYear() {
        String year = "";
        if (idCodeValue.charAt(0) == '1' || idCodeValue.charAt(0) == '2'){
            year = year + "18";
        } else if (idCodeValue.charAt(0) == '3' || idCodeValue.charAt(0) == '4'){
            year = year + "19";
        } else if (idCodeValue.charAt(0) == '5' || idCodeValue.charAt(0) == '6'){
            year = year + "20";
        }
        year = year + idCodeValue.charAt(1) + idCodeValue.charAt(2);
        int ret = Integer.parseInt(year);
        return ret;
    }

    /**
     * Check if gender number is correct.
     *
     * @return boolean describing whether the gender number is correct.
     */
    private boolean isGenderNumberCorrect() {
        List<Integer> correct = new ArrayList<>(){{
            add(1);
            add(2);
            add(3);
            add(4);
            add(5);
            add(6);
        }};
        int gennum = idCodeValue.charAt(0);
        return correct.contains(gennum);
    }

    /**
     * Check if the year number is correct.
     *
     * @return boolean describing whether the year number is correct.
     */
    private boolean isYearNumberCorrect() {
        int year = Integer.parseInt(idCodeValue.substring(1, 3));
        return 0 <= year && year < 100;
    }

    /**
     * Check if the month number is correct.
     *
     * @return boolean describing whether the month number is correct.
     */
    private boolean isMonthNumberCorrect() {
        int month = Integer.parseInt(idCodeValue.substring(3, 5));
        return 0 < month && month < 13;
    }

    /**
     * Check if the day number is correct.
     *
     * @return boolean describing whether the day number is correct.
     */
    private boolean isDayNumberCorrect() {
        List<Integer> shorter_months = new ArrayList<Integer>(){{
            add(4);
            add(6);
            add(9);
            add(11);
        }};
        List<Integer> longer_months = new ArrayList<Integer>(){{
            add(1);
            add(3);
            add(5);
            add(7);
            add(8);
            add(10);
            add(12);
        }};
        int month = Integer.parseInt(idCodeValue.substring(3, 5));
        int day = Integer.parseInt(idCodeValue.substring(5, 7));
        if (month == 2 && isLeapYear(getFullYear()) && 0 < day && day <= 29){
            return true;
        } else if (month == 2 && !isLeapYear(getFullYear()) && 0 < day && day <= 28){
            return true;
        } else if (shorter_months.contains(month) && 0 < day && day <= 30){
            return true;
        } else if (longer_months.contains(month) && 0 < day && day <= 31){
            return true;
        } else {
            return false;
        }

    }

    /**
     * Check if the control number is correct.
     *
     * @return boolean describing whether the control number is correct.
     */
    private boolean isControlNumberCorrect() {
        String range = "123456789123456789";
        int counter = 0;
        for (int i = 0;i <= idCodeValue.length() - 1; i++) {
            int num1 = range.charAt(i);
            int num2 = idCodeValue.charAt(i);
            counter = counter += (num1 * num2);
        }
        int result = counter % 11;
        int controlnum = 0;
        if (result != 10) {
            controlnum = result;
        }
        int actual_controlnum = idCodeValue.charAt(idCodeValue.length() - 1);
        return actual_controlnum == controlnum;
    }

    /**
     * Check if the given year is a leap year.
     *
     * @param fullYear
     * @return boolean describing whether the given year is a leap year.
     */
    private boolean isLeapYear(int fullYear) {
        if ((fullYear % 4 == 0) && !(fullYear % 100 == 0)){
            return true;
        } else return fullYear % 400 == 0;
    }

    /**
     * Run tests.
     * @param args info.
     */
    public static void main(String[] args) {
        IdCode validMaleIdCode = new IdCode("37605030299");
        System.out.println(validMaleIdCode.isCorrect());
        System.out.println(validMaleIdCode.getInformation());
        System.out.println(validMaleIdCode.getGender());
        System.out.println(validMaleIdCode.getBirthPlace());
        System.out.println(validMaleIdCode.getFullYear());
        System.out.println(validMaleIdCode.isGenderNumberCorrect());
        System.out.println(validMaleIdCode.isYearNumberCorrect());
        System.out.println(validMaleIdCode.isMonthNumberCorrect());
        System.out.println(validMaleIdCode.isDayNumberCorrect());
        System.out.println(validMaleIdCode.isControlNumberCorrect());
        System.out.println(validMaleIdCode.isLeapYear(validMaleIdCode.getFullYear()));
    }

}