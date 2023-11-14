import java.util.*;
import java.awt.geom.*;

 
public class Simplex_modified {
  public static void main(String[] args) {
    /*Scanner input = new Scanner(System.in);
    System.out.println("Enter radius: ");
    int radius = input.nextInt();
    System.out.println(S_complex(radius));  */
    //birthDeath(); 
    System.out.println(S_complex(150));
    birthDeath();
  }
 
  public static List<List<Integer>> S_complex(int r) {
    List<Point2D> data = generateRandomData();
    List<List<Integer>> nodes = generateNodes(data, r);
    return nodes;
  }
 
  public static List<Point2D> generateRandomData() {
    List<Point2D> data = new ArrayList<>();
    Random rand = new Random();
    for (int i = 0; i < 10; i++) {
      double x = rand.nextInt(201) - 100;
      double y = rand.nextInt(201) - 100;
      data.add(new Point2D.Double(x, y));
    }
    return data;
  }
 
  public static List<List<Integer>> generateNodes(List<Point2D> data, int r) {
    List<List<Integer>> nodes = new ArrayList<>();
    for (int i = 0; i < 10; i++) {
      nodes.add(new ArrayList<>());
      nodes.get(i).add(i);
    }
 
    for (int i = 0; i < 9; i++) {
      for (int j = i + 1; j < 10; j++) {
        double dist = data.get(i).distance(data.get(j));
        if (dist <= r) {
          nodes.get(i).add(j);
          nodes.get(j).add(i);
        }
      }
    }
    return nodes;
  }

  public static void birthDeath() {
    List<Integer> radii = new ArrayList<>();
    for (int r=0; r<=201; r++) {
      if (S_complex(r) != S_complex(r+1)) {
        radii.add(r);
      }
    }
    System.out.println(radii);
  } 
  
}
