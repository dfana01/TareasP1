package ado.edu.pucmm.calculator;

import static ado.edu.pucmm.calculator.Main.Operator.sum;
import static ado.edu.pucmm.calculator.Main.Operator.multiplication;
import static ado.edu.pucmm.calculator.Main.Operator.subtraction;
import static ado.edu.pucmm.calculator.Main.Operator.division;
import static ado.edu.pucmm.calculator.Main.Operator.and;
import static ado.edu.pucmm.calculator.Main.Operator.or;

public class Main {
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
    public static class Calculator {
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

    public static void main(String...args){
        String output = args.length == 0 ? "Welcome to the calculator, with this CLI util you can do: \n" +
                "- sum (+) \n" +
                "- subtraction (-) \n" +
                "- multiplication (*) \n" +
                "- division (/) \n" +
                "- and (**) \n" +
                "- or (**) \n" +
                "** Logical operator \n" +
                "Format: calculator <binary-number> <+ | - | * | / | and | or> <binary-number> [<+ | - | * | / | and | or> <binary-number>] \n" +
                "Author: <Dante Fana Badia>dfana@dfb.com.do" :
                String.format("Thanks for using the calculator, result: %.2f", calculate(args));
        System.out.println(output);
    }

    public static float calculate(String...args){
        Calculator calculator = new Calculator(Integer.parseInt(args[0], 2));
        for (int i = 1; i < args.length; i++) {
            if (i % 2 != 0) {
                String o = args[i];
                int n = Integer.parseInt(args[i+1], 2);
                if (or.toString().equals(o))
                    calculator.or(n);
                else if(and.toString().equals(o))
                    calculator.and(n);
                else if(sum.toString().equals(o))
                    calculator.sum(n);
                else if(subtraction.toString().equals(o))
                    calculator.subtraction(n);
                else if(multiplication.toString().equals(o))
                    calculator.multiplication(n);
                else if(division.toString().equals(o))
                    calculator.division(n);
                i++;
            }
        }
        return calculator.equal();
    }
}
