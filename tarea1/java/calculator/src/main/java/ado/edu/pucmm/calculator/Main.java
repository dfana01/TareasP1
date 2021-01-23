package ado.edu.pucmm.calculator;

import static ado.edu.pucmm.calculator.Main.Operator.sum;
import static ado.edu.pucmm.calculator.Main.Operator.multiplication;
import static ado.edu.pucmm.calculator.Main.Operator.subtraction;
import static ado.edu.pucmm.calculator.Main.Operator.division;
import static ado.edu.pucmm.calculator.Main.Operator.and;
import static ado.edu.pucmm.calculator.Main.Operator.or;

public class Main {

    public static void main(String...args){
        System.out.println(execute(args));
    }

    public static String execute(String...args){
        return args.length == 0 ? "Welcome to the calculator, with this CLI util you can do: \n" +
                "- sum (+) \n" +
                "- subtraction (-) \n" +
                "- multiplication (*) \n" +
                "- division (/) \n" +
                "- and (and) \n" +
                "- or (or) \n\n" +
                "Format: calculator <binary-number> <+ | - | * | / | or | and> <binary-number> [<+ | - | * | / | and | or> <binary-number>] \n\n" +
                "Author: <Dante Fana Badia>dfana@dfb.com.do" :
                String.format("Thanks for using the calculator, result: %f", calculate(args));
    }

    public static float calculate(String...args){
        try{
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
        } catch (Exception e){
            throw new IllegalArgumentException("Malformat exception please check if your input complies the format \n" +
                    "Format: calculator <binary-number> <+ | - | * | / | and | or> <binary-number> [<+ | - | * | / | and | or> <binary-number>] ");
        }
    }

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
        private float result;

        public Calculator(float n){
            result = n;
        }

        public Calculator sum(float n){
            result = result + n;
            return this;
        }

        public Calculator multiplication(float n){
            result = result * n;
            return this;
        }

        public Calculator subtraction(float n){
            result = result - n;
            return this;
        }

        public Calculator division(float n){
            result = result / n;
            return this;
        }

        public Calculator and(float n){
            result = (float) (Math.round(result) & Math.round(n));
            return this;
        }

        public Calculator or(float n){
            result = (float) (Math.round(result) | Math.round(n));
            return this;
        }

        public Calculator init(float n) {
            result = n;
            return this;
        }

        public float equal(){
            return result;
        }

        public void clear() {
            result = 0;
        }
    }
}
