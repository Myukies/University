import java.util.HashSet;
import java.util.Set;

public class SetInterface {
    public static void main(String[] args) {
        // Creating a set
        Set<String> mySet = new HashSet<>();

        // Adding elements to the set
        mySet.add("Red");
        mySet.add("Green");
        mySet.add("Blue");
        mySet.add("Red"); // Duplicate element

        // Accessing elements
        System.out.println("Elements in the set:");
        for (String element : mySet) {
            System.out.println(element);
        }

        // Removing an element
        mySet.remove("Green");
        System.out.println("\nSet after removing 'Green': " + mySet);

        // Checking if an element exists
        System.out.println("Does the set contain 'Red'? " + mySet.contains("Red"));
    }
}
