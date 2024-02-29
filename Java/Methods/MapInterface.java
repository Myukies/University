import java.util.HashMap;
import java.util.Map;

public class MapInterface {
    public static void main(String[] args) {
        // Creating a map
        Map<Integer, String> myMap = new HashMap<>();

        // Adding key-value pairs to the map
        myMap.put(1, "Java");
        myMap.put(2, "Python");
        myMap.put(3, "C++");
        myMap.put(4, "JavaScript");

        // Accessing elements
        System.out.println("Elements in the map:");
        for (Map.Entry<Integer, String> entry : myMap.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }

        // Removing an element
        myMap.remove(3);
        System.out.println("\nMap after removing key '3': " + myMap);

        // Checking if a key exists
        System.out.println("Does the map contain key '2'? " + myMap.containsKey(2));

        // Checking if a value exists
        System.out.println("Does the map contain value 'Python'? " + myMap.containsValue("Python"));
    }
}
