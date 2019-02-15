import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Random;

public class randomFlag {
    
    public void generateRandomFlag(String flag){
        int seed = sTi("Thi")-sTi("CTF");
        Random r = new Random(seed);
        char c;
        String randomFlag = "";
        
        for(int i=0; i<flag.length(); i++){
            c = flag.charAt(i);
            if(Character.isLowerCase(c)){
                randomFlag += iTc(cTi(c) + 2*cTi('e') - (r.nextInt(5)*2-3) - cTi('b') - cTi('h'));
            }
            else if(Character.isUpperCase(c)){
                randomFlag += iTc(cTi(c) + cTi('F')/2 + (r.nextInt(5)*(-2)+3) - 3*cTi('A') + cTi('F') + cTi('Z'));
            }
            else if(Character.isDigit(c)){
                randomFlag += iTc(cTi(c) + cTi('Z') - (r.nextInt(10)+5) - cTi('0'));
            }
            else{
                randomFlag += c;
            }
        }
        System.out.println(randomFlag);
    }
    
    public int sTi(String s){
        int result=0;
        for(int i=0; i<s.length(); i++){
            result += Character.getNumericValue(s.charAt(i));
        }
        return result;
    }
    
    public int cTi(char c){
        return (int)c;
    }
    
    public char iTc(int i){
        return (char)(i);
    }    
    
    @SuppressWarnings("resource")
    public static void main(String[] args) {
      randomFlag rF = new randomFlag();
      String flag="";
      
      //Read the text file on the server to get the flag. 
      try {
          flag = (new BufferedReader(new FileReader("Flag.txt"))).readLine();
      } catch (IOException e) {
          e.printStackTrace();
      }

      rF.generateRandomFlag(flag);
    }

}
