import java.io.*;
import java.util.*;

class sw {
    public static void main(String[] args) {
        // File to read
        String fileName = "poem.txt";

        // Using try-with-resources to ensure the file is properly closed
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            System.out.println("Reading content from '" + fileName + "':");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.err.println("An error occurred while reading the file: " + e.getMessage());
        }
    }
}
