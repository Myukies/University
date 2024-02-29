class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String toJson() {
        return "{\"name\":\"" + this.name + "\",\"age\":" + this.age + "}";
    }

    public static Student fromJson(String jsonString) {
        String name = jsonString.split("\"name\":\"")[1].split("\",")[0];
        int age = Integer.parseInt(jsonString.split("\"age\":")[1].split("}")[0]);
        return new Student(name, age);
    }
}

public class JSONExample {
    public static void main(String[] args) {
        Student student1 = new Student("John", 20);
        String json1 = student1.toJson();
        System.out.println("Encoded JSON: " + json1);

        String jsonString = "{\"name\":\"Alice\",\"age\":22}";
        Student student2 = Student.fromJson(jsonString);
        System.out.println("Decoded Student: Name=" + student2.getName() + ", Age=" + student2.getAge());
    }
}
