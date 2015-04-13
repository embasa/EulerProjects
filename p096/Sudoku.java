import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Sudoku{ private static int[][] grid = new int[9][9];
  public Sudoku(){
    //why am i empty? WHO KNOWS!! The mystery.
  }
  private static char[] game = new char[98];
  private  class Position{
    int i=0;
    int j=0;
    Position(){}
    Position(int i,int j){
      this.i = i;
      this.j = j;
    }  
  }
  private Position p = new Position();
  public void findNextCellToFill(int i,int j){
    for(int x=i;x<9;x++){ 
      for(int y=j;y<9;y++){ 
        if(grid[x][y] == 0){
          p.i = x;
          p.j = y;
        }
      }
    }
    
    for(int x=0;x<9;x++){
      for(int y=0;y<9;y++){
        if(grid[x][y] == 0){
          p.i = x;
          p.j = y;
        }
      }
    }
    p.i = -1;
    p.j = -1;
  }

  public boolean isValid(int i,int j,int e){
    boolean valid = true;  
    //test if e is in row i
    for(int y=0;y<9;y++){
      if(grid[i][y] == e){
        return false;
      }
    }

    //test if e is in column j
    for(int x=0;x<9;x++){
      if(grid[x][j] == e){
        return false;
      }
    }

    //test if e is in corresponding box
    int cornerX= 3*(i/3);
    int cornerY= 3*(j/3);
    for(int x=cornerX;x<cornerX+3;x++){
      for(int y=cornerY;y<cornerY+3;y++){
        if(grid[x][y] == e){
          return false;
        }
      }
    }
    return true;
  }

  public boolean solveSudoku(int i,int j){
    //if no cell found to fill puzzle is solved    
    findNextCellToFill(i,j);
    int I = p.i;
    int J = p.j;
    if(I == -1){
      return true;
    }
    for(int e=1;e<10;e++){
      if(isValid(I,J,e)){
        grid[I][J]=e;
        if(solveSudoku(I,J)){
          return true;
        }
        grid[I][J] = 0;
      }
    }
    return false;
  }

  public void loadGameToGrid(){
    int i = 0;
    int j = 0;
    for(int k=8;k<97;k++){
      if (j/9==1){
        j=0;
        i++;
      }else{
        grid[i][j] = game[k]-'0'; 
        j++;
      }
    }
  }

  public void print(){
    for( int i =0;i<9;i++){
      for(int j=0;j<9;j++){
        System.out.print(grid[i][j]); 
        System.out.print(' ');
      }
      System.out.println();
    }
    System.out.println("--------------------------------------");
  }

  public String mainLoop() throws FileNotFoundException, IOException{
    int count = 0;
    try(BufferedReader br = new BufferedReader(new FileReader("p096_sudoku.txt"))){
      while(br.read(game,0,98) != -1){
        loadGameToGrid(); 
        if(solveSudoku(0,0)){
          count++;
        }
      }
    }	
    System.out.println(":" + count);
    return "";
    
  }
}
