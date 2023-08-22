import java.util.*;
class Treeset {
    public static void main(String args[]){
        TreeSet<String> hs = new TreeSet<String>();
        hs.add("Hello");
        hs.add("this");
        hs.add("is");
        hs.add("a");
        hs.add("Tree");
        hs.add("Set");
        System.out.println(hs);
            for(String s:hs){
                System.out.println(s);
            }
    }
}