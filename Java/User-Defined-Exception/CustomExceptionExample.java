// Main class
public class CustomExceptionExample {
    // Method to validate age
    static void validateAge(int age) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("Age must be 18 or above.");
        }
        System.out.println("Valid age: " + age);
    }

    // Main method
    public static void main(String[] args) {
        try {
            // Testing with valid and invalid ages
            validateAge(20); // Valid age
            validateAge(25); // Invalid age, will raise exception
        } catch (InvalidAgeException e) {
            // Handling the custom exception
            System.out.println("Caught exception: " + e.getMessage());
        }
    }
}
