import java.util.*;

public class TDA_Matrix {
public static void main(String[] args) {
  // Dimension of the matrix
  int m = 8;
  int n = 8;
  
  Random rand = new Random();
  double[][] M = new double [m][n];
  for (int i=0; i < m; i++) {
    for (int j=0; j< n; j++) {
      M[i][j] = rand.nextInt(2);
    }
  }
  //print_matrix(M, m, n);
  System.out.println("Pivot array: " + pivot(M, m, n));
  //print_matrix(reduced(M, m, n), m, n);
  reduced(M, m, n);
  System.out.println("Pivot array of the reduced matrix: " + pivot(M, m, n));
  System.out.println("Barcodes: " + barcode(M, m, n));
  
}
public static List<Integer> pivot(double[][] M, int m, int n) {
  List<Integer> piv = new ArrayList<>();
  for (int j=0; j< n; j++) {
    piv.add(0);
  }
  for (int j=0; j< n; j++) {
    for (int i=0; i< m; i++) {
      if (M[i][j] != 0) {
        piv.set(j, i+1);
      }
    }
  }
  return piv;
}

public static void print_matrix(double [][] M, int m, int n) {
  for (int i=0; i< m; i++) {
    for (int j=0;j< n;j++) {
      System.out.print(M[i][j]);
      System.out.print("  ");
    }
    System.out.println(" ");
  }
}

/* 
 public static void print_pivot(double [][] M) {
  System.out.print("[");
    for (int j=0; j<10; j++) {
      System.out.print(pivot(M)[j]);
      System.out.print(" ");
    }
    System.out.print("]");
} 
*/
    
 
// Reducing the matrix with rightward column operations
public static double[][] reduced(double[][] M, int m, int n) {
  for (int j=0; j< n; j++) {
    for (int k=0; k< j; k++) {
      if (pivot(M, m, n).get(j) == pivot(M, m, n).get(k) & pivot(M, m, n).get(j) != 0) {
        int p = pivot(M, m, n).get(j);
        for (int i=0; i< m; i++) {
          M[i][j] = -M[p-1][j] / M[p-1][k] * M[i][k] + M[i][j];
        }
        reduced(M, m, n);
      }
    }
  }
  return M;
}
//Creating barcodes as a list of intervals 
public static List<String> barcode(double[][] M, int m, int n) {
  double[][] x = reduced(M, m, n);
  List<Integer> p = pivot(x, m, n);
  List<String> barc = new ArrayList<>();
  for (int k=0; k < n; k++) {
    int temp = pivot(x,m,n).get(k);
    if (temp != 0 & temp < k + 1 ) {
      barc.add("[" + temp + " , " + (k+1) + ")");
    }
    if (temp == 0 & pivot(x,m,n).contains(temp) == false) {
      barc.add("[" + (k+1) + " , " + Double.POSITIVE_INFINITY + ")");
    }
  }
  return barc;
}

        
}
