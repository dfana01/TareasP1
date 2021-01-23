package ado.edu.pucmm.calculator;

public class Calculator {

    enum Operator {
        sum("+"),
        multiplication("*"),
        subtraction("-"),
        division("/"),
        and("and"),
        or("or");

        private final String text;

        Operator(final String text) {
            this.text = text;
        }

        @Override
        public String toString() {
            return text;
        }
    }
    private int result;

    public Calculator(int n){
        result = n;
    }

    public Calculator(){
        result = 0;
    }

    public Calculator sum(int n){
        result = result + n;
        return this;
    }

    public Calculator multiplication(int n){
        result = result * n;
        return this;
    }

    public Calculator subtraction(int n){
        result = result - n;
        return this;
    }

    public Calculator division(int n){
        result = result / n;
        return this;
    }

    public Calculator and(int n){
        result = result & n;
        return this;
    }

    public Calculator or(int n){
        result = result | n;
        return this;
    }

    public int equal(){
        return result;
    }

    public void reset(){
        result = 0;
    }

    public void reset(int n){
        result = n;
    }
}
