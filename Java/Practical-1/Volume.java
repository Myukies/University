public class Volume{
    double v;
    double volume(double r){
        v = (4/3.0)*(22/7.0)*r*r*r;
        return v;
    }
    double volume(double r, double h){
        v = (22/7.0)*r*r*h;
        return v;
    }
    double volume(double l, double b, double h){
        v = l*b*h;
        return v;
    }
    public static void main(String args[]){
        Volume obj = new Volume();
        System.out.println("Spehere Volume = " + obj.volume(10));
        System.out.println("Cylinder Volume = " + obj.volume(2,5,10));
        System.out.println("Cubiod Volume = " + obj.volume(3.5,3.3, 4));
    }
}