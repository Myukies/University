import java.util.ArrayList;
import java.util.List;

public class ListInterface {
    public static void main(String[] args) {
        // Creating a list
        List<String> myList = new ArrayList<>();

        // Adding elements to the list
        myList.add("Apple");
        myList.add("Banana");
        myList.add("Orange");

        // Accessing elements
        System.out.println("Elements in the list:");
        for (String element : myList) {
            System.out.println(element);
        }

        // Removing an element
        myList.remove("Banana");
        System.out.println("\nList after removing 'Banana': " + myList);

        // Checking if an element exists
        System.out.println("Does the list contain 'Apple'? " + myList.contains("Apple"));
    }
}
