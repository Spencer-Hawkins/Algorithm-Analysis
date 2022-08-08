public class steelRod{
    
    
    public static int steelRods(int n, int[] P){
        int currMax;
        int totalMax=Integer.MinValue;
        int maxValueCut;
        int nCopy;
        int[] ps;
        
    
        for(int i=0; i<p.length; i++){
            currMax=Integer.MinValue;
            nCopy=n
            ps = new P.subArray(0,i);
    
            while(nCopy>0){
            for(int j=0; j<=i; j++){
                if(p[j]>maxValueCut){
                     maxValueCut=j;
                }
            }
            //need to modulo nCopy to decrement it and increase currMin
            currMax=(nCopy/j)*P[j];
            nCopy=nCopy%j;
            }
          if(currMax > totalMax){
              totalMax=currMax;
          }
          
        }
    
    return totalMax;
    }
    




    public static int steelRods(int n, int[] P){
        int currMax;
        int totalMax=Integer.MinValue;
        int maxValueCut;
        int nCopy;
        int[] ps;
        
        //find the leftmostCut
        //I choose the last solution P[n-1], the current one P[n], or the last one plus the next available cut P[j]+P[i]
        //
    
    return totalMax;
    }
}

public static void main(String []Args){
    int n = 5;
    int []p = new int{1, 2, 3, 4, 5};
    System.out.println(steelRods(n, p));
}
