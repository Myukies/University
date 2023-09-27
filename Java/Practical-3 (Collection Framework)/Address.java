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
}

