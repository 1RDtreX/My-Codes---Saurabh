import java.io.*;
import java.util.*;

class sq
{
public static void main(String []args)throws IOException
{
Scanner sc= new Scanner(System.in);
System.out.println("Enter the word to be write : ");
String content=sc.nextLine();
FileWriter writer=new FileWriter("poem.txt");
writer.write(content);

}



}