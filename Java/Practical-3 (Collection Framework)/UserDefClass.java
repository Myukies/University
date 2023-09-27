import java.util.*;
class UserDefClass{
        public static void main(String args[]){
            LinkedList<Address> usr = new LinkedList<Address>();
            usr.add(new Address("Siddhant", "Manvelpada road", "Virar", "Maharashtra", "401305"));
            usr.add(new Address("Pratyush", "Global City", "Virar", "Maharashtra", "401303"));
            for(Address element : usr){
                System.out.println(element + "\n");
                System.out.println();
            }
        }
    }