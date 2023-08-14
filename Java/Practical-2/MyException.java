class MyException extends Exception {
    private int detail;
    MyException(int a) {
        detail = a;
    }
    public String toString() {
        return "My exception[" + detail + "]";
    }
    static class UserException{
        static void compute(int a) throws MyException {
            System.out.println("Called compute(" + a + ")");
            if (a > 10)
                throw new MyException(a);
            System.out.println("Normal exit");
        }
    }
    public static void main(String[] args) {
        try {
            UserException.compute(1);
            UserException.compute(20);
        } catch (MyException e) {
            System.out.println("Caught" + e);
        } finally {
            System.out.println("Finally block");
        }
    }
}
