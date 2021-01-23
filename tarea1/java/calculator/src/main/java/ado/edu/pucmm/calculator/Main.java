package ado.edu.pucmm.calculator;

import static ado.edu.pucmm.calculator.Calculator.Operator.or;
import static ado.edu.pucmm.calculator.Calculator.Operator.multiplication;
import static ado.edu.pucmm.calculator.Calculator.Operator.sum;
import static ado.edu.pucmm.calculator.Calculator.Operator.division;
import static ado.edu.pucmm.calculator.Calculator.Operator.subtraction;
import static ado.edu.pucmm.calculator.Calculator.Operator.and;

public class Main {
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
