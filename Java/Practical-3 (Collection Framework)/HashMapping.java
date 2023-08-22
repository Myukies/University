import java.util.*;
class HashMapping{
    public static void main(String agrs[]){
        HashMap<String, Double> hm = new HashMap<String, Double>();
        hm.put("Siddhant", (620.3));
        hm.put("Pratyush", (299.00));
        hm.put("Atharva", (1920.99));
        hm.put("Tanishka", (89.21));
        hm.put("Sharavni", (1000.29));

        Set<Map.Entry<String, Double>> set = hm.entrySet();
        for(Map.Entry<String, Double> me:set){
            System.out.println(me.getKey() + ": ");
            System.out.println(me.getValue());
        }
 
        System.out.println();
        Double balance = hm.get("Siddhant");
        hm.put("Siddhant", balance = 1200.00);

        System.out.println("Siddhant's new balance: " + hm.get("Siddhant"));
    }
}