mvn package
mvn assembly:assembly
echo "#! /usr/bin/env java -jar" > calculator
cat target/calculator-1.0-jar-with-dependencies.jar >> calculator
chmod +x calculator