package ado.edu.pucmm.calculator;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        MainTest.CalculatorTestFact.class,
        MainTest.MiscellaneousTestFact.class,
})
public class MainTest {
    public static final String MAX_BINARY_INTEGER = "1111111111111111111111111111111";
    public static final int MAX_INTEGER = 2147483647;

    public static final String MID_BINARY_INTEGER = "0111111111111111111111111111111";
    public static final int MID_INTEGER = 1073741823;

    public static final String MIN_BINARY_INTEGER = "0000000000000000000000000000000";
    public static final int MIN_INTEGER = 0;

    public static class CalculatorTestFact{

        private Main.Calculator calculator;

        @Before
        public void setUp(){
            calculator = new Main.Calculator(0);
        }

        @After
        public void reset(){
            calculator.clear();
        }

        @Test
        public void sumMinValues() {
            int result0 = MIN_INTEGER + MID_INTEGER;
            int result1 = calculator.init(MIN_INTEGER).sum(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void sumMidValues() {
            int result0 = MID_INTEGER + MID_INTEGER;
            int result1 = calculator.init(MID_INTEGER).sum(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void sumMaxValues() {
            int result0 = MAX_INTEGER + MIN_INTEGER;
            int result1 = calculator.init(MAX_INTEGER).sum(MIN_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void subtractMinValues() {
            int result0 = MIN_INTEGER - MID_INTEGER;
            int result1 = calculator.init(MIN_INTEGER).subtraction(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void subtractMidValues() {
            int result0 = MID_INTEGER - MID_INTEGER;
            int result1 = calculator.init(MID_INTEGER).subtraction(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void subtractMaxValues() {
            int result0 = MAX_INTEGER - MIN_INTEGER;
            int result1 = calculator.init(MAX_INTEGER).subtraction(MIN_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void divisionMinValues() {
            int result0 = MIN_INTEGER / MID_INTEGER;
            int result1 = calculator.init(MIN_INTEGER).division(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void divisionMidValues() {
            int result0 = MID_INTEGER / MID_INTEGER;
            int result1 = calculator.init(MID_INTEGER).division(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void divisionMaxValues() {
            int result0 = MAX_INTEGER / MID_INTEGER;
            int result1 = calculator.init(MAX_INTEGER).division(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void multiplicationMinValues() {
            int result0 = MIN_INTEGER * MID_INTEGER;
            int result1 = calculator.init(MIN_INTEGER).multiplication(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void multiplicationMidValues() {
            int result0 = MID_INTEGER * MIN_INTEGER;
            int result1 = calculator.init(MID_INTEGER).multiplication(MIN_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void multiplicationMaxValues() {
            int result0 = MAX_INTEGER * MIN_INTEGER;
            int result1 = calculator.init(MAX_INTEGER).multiplication(MIN_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void orMinValues() {
            int result0 = MIN_INTEGER | MID_INTEGER;
            int result1 = calculator.init(MIN_INTEGER).or(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void orMidValues() {
            int result0 = MID_INTEGER | MID_INTEGER;
            int result1 = calculator.init(MID_INTEGER).or(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void orMaxValues() {
            int result0 = MAX_INTEGER | MIN_INTEGER;
            int result1 = calculator.init(MAX_INTEGER).or(MIN_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void andMinValues() {
            int result0 = MIN_INTEGER & MID_INTEGER;
            int result1 = calculator.init(MIN_INTEGER).and(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void andMidValues() {
            int result0 = MID_INTEGER & MID_INTEGER;
            int result1 = calculator.init(MID_INTEGER).and(MID_INTEGER).equal();
            assertEquals(result0, result1);
        }

        @Test
        public void andMaxValues() {
            int result0 = MAX_INTEGER & MIN_INTEGER;
            int result1 = calculator.init(MAX_INTEGER).and(MIN_INTEGER).equal();
            assertEquals(result0, result1);
        }
    }

    public static class MiscellaneousTestFact{
        @Test
        public void messageWithoutArgs() {
            String mjs = Main.execute();
            assertTrue("Must return default message", mjs.contains("Welcome"));
        }

        @Test
        public void messageWithArgs() {
            String mjs = Main.execute(MIN_BINARY_INTEGER, "+", MID_BINARY_INTEGER);
            assertTrue("Must return default message", mjs.contains("Thanks for using the calculator, result"));
        }

        @Test(expected = IllegalArgumentException.class)
        public void calculateBadFormatArgs() {
            Main.execute(MIN_BINARY_INTEGER, "+", "+", MID_BINARY_INTEGER);
        }

        @Test
        public void calculateGoodFormatArgs() {
            String mjs = Main.execute(MIN_BINARY_INTEGER, "-", MID_BINARY_INTEGER);
            String result = String.valueOf(MIN_INTEGER - MID_INTEGER);
            assertTrue(String.format("Must return result: %s, that contains: %s", mjs, result), mjs.contains(result));
        }

        @Test
        public void calculateChainArgs() {
            String mjs = Main.execute(MIN_BINARY_INTEGER, "and",
                    MID_BINARY_INTEGER, "or",
                    MID_BINARY_INTEGER, "/",
                    MID_BINARY_INTEGER, "*",
                    MID_BINARY_INTEGER
            );
            String result = String.valueOf((((MIN_INTEGER & MID_INTEGER) | MID_INTEGER) / MID_INTEGER) * MID_INTEGER);
            assertTrue(String.format("Must return result: %s, that contains: %s", mjs, result), mjs.contains(result));
        }

        @Test
        public void main() {
            PrintStream standardOut = System.out;
            ByteArrayOutputStream outputStreamCaptor = new ByteArrayOutputStream();
            System.setOut(new PrintStream(outputStreamCaptor));

            Main.main();
            assertTrue("Must return default message", outputStreamCaptor.toString().contains("Welcome"));

            System.setOut(standardOut);
        }
    }
}
