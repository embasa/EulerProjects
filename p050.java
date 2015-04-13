//Question is find the prime that consists of the longest sequence of primes that sum to it.
public class p050{
  public static void main(String[] args){
    int maxValue = 1000000;//contsraint of problem
    int[] primes = PrimeGen.getPrimes(maxValue); 
    int primeWithLongestRun = 0;
    int longestRun = 0;
    int currentRun = 0;
    int sum = 0;
    for(int e=0;e<primes.length;e++){
      int primeToTest = primes[e];
      for(int i=0;i<=e;i++){
        currentRun = 0;
        sum = primes[i];
        currentRun++;
        int j= i+1;
        while(j<=e && sum+primes[j]<=primeToTest){
          sum+=primes[j];
          currentRun++;
          j++;
        }
        if(sum == primeToTest){
          if(currentRun >=longestRun){
            primeWithLongestRun = primeToTest;
            longestRun = currentRun;
          }
        }
      }
    }
    System.out.println(primeWithLongestRun);
  }
}
