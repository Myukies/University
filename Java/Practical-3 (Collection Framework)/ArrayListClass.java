import java.util.*;
class ArrayListClass{
    public static void main(String args[]){
        ArrayList<String> al = new ArrayList<String>();
        System.out.println("Initial size of Array List: " + al.size());
        al.add("A");    
        al.add("B");    
        al.add("C");    
        al.add("D");    
        al.add("E");    
        al.add("F");    
        al.add("G");    
        al.add(1, "H2");   
        System.out.println("Size of Array List after additions: " + al.size()); 
        System.out.println("Contents of Array List" + al);
        al.remove("B");
        al.remove("4");
        System.out.println("Size of Array List after deletion: " + al.size());
        System.out.println("Contents of Array list: " + al);
    }
}