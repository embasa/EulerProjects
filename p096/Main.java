import java.io.FileNotFoundException;
import java.io.IOException;
public class Main{
  public static void main(String[] args)throws FileNotFoundException, IOException{
    Sudoku s = new Sudoku();
    s.mainLoop();
  }
}
