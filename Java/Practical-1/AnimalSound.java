public class AnimalSound {
    class Animal {
        public void animalSound() {
            System.out.println("The animal makes a sound");
        }
    }

    class Pig extends Animal {
        public void animalSound() {
            System.out.println("The pig says: wee wee");
        }
    }

    class Dog extends Animal {
        public void animalSound() {
            System.out.println("The dog says: bow bow");
        }
    }

    public static void main(String[] args) {
        AnimalSound animalSound = new AnimalSound(); // Create an instance of the outer class
        AnimalSound.Pig obj1 = animalSound.new Pig();
        obj1.animalSound();
        AnimalSound.Dog obj2 = animalSound.new Dog();
        obj2.animalSound();
    }
}
