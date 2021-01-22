import java.lang.System.*;

public class Main {
    static class Calculator {
        public String helloWorld(){
            return "Hello world!";
        }
    }

    public static void main(String...args){
        Calculator calculator = new Calculator();
        System.out.println(calculator.helloWorld());
    }
}