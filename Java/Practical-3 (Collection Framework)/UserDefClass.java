import java.util.*;
class Address{
    private String code;
    private String name;
    private String street;
    private String city;
    private String state;

    Address(String a, String b, String c, String d, String e){
        name = a;
        street = b;
        city = c;
        state = d;
        code = e;
    }

    public String toString(){
        return name + "\n" + street + "\n" + city + ", " + state + " " + code;
    }

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
}