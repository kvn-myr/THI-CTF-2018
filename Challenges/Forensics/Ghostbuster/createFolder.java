import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.Random;

public class createFolder{
    String alphabet = new String("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
    String result = new String();
    Random r = new Random();
    int anzahlAlphabet = alphabet.length();
    
    public String randomString(){
        result="";
        for(int i=0; i<10; i++){
            result = result + alphabet.charAt(r.nextInt(anzahlAlphabet));
        }
        return result;
    }
    
    public static void main(String[] args) {
    createFolder folder = new createFolder();
    String path = new String("F:\\");
    int anzahlFolder = 100;
    int hiddenFileNr = new Random().nextInt(anzahlFolder-1);
    PrintWriter writer;
    
    for(int j=0; j< anzahlFolder; j++){
        File f = new File(path+folder.randomString());
        int subfolders = new Random().nextInt(10);
        for(int i=0; i<subfolders; i++){
            f = new File(f.getPath()+"\\"+folder.randomString());
            if(!f.exists()){
                f.mkdirs();
            }
            else{
                while(!f.exists()){
                    f = new File(f.getPath()+"\\"+folder.randomString());
                }
                f.mkdirs();    
            }
            if(j!=hiddenFileNr || i!=subfolders-1){
                try {
                    writer = new PrintWriter(f.getPath()+"\\9.txt", "UTF-8");
                    writer.println("Empty");
                    writer.close();
                } catch (FileNotFoundException | UnsupportedEncodingException e) {
                    e.printStackTrace();
                }
            }
            else{
                Process p;
                try {
                    writer = new PrintWriter(f.getPath()+"\\6.txt", "UTF-8");
                    writer.println("Oh no. Something went wrong. My PDF cover has been deleted!!"+"\n Maybe the sheep dog can help with the magnifying glass.");
                    writer.close();
                    p = Runtime.getRuntime().exec("attrib +h " + f.getPath()+"\\6.txt");
                    p.waitFor();
                    System.out.println(f.getPath());
                } catch (InterruptedException | IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    }
}
