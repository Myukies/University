public class Main {
    String language;
    Main(){
        this.language = "Java";
    }
    Main(String language){
        this.language = language;
    }
    public void getName(){
        System.out.println("Programming Langugage: "+this.language);
    }
    public static void main(String[]args){
        Main obj1 = new Main();
        Main obj2 = new Main("Python");

        obj1.getName();
        obj2.getName();

    }
}
