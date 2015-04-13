import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class PrimeGen{
  public static int[] getPrimes(int range){
    boolean[] nums = new boolean[range +1];
    Arrays.fill(nums,true);
    nums[0] = false;
    nums[1] = false;
    List<Integer> primes = new ArrayList<Integer>();
    for(int i=2;i*i<=range;i++){
      if(nums[i]){
        for(int j=i;i*j<=range;j++){
          nums[i*j] = false;
        }
      }
    }
    for(int i=0;i<=range;i++){
      if(nums[i]){
        primes.add(i);
      }
    }

    int[] arrayOfPrimes = new int[primes.size()]; 

    for(int i=0;i<primes.size();i++){
      arrayOfPrimes[i] = primes.get(i);
    }
    return arrayOfPrimes; 
  }
}
