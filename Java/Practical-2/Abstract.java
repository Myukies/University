abstract class GraphicObject{
  int x, y;
  void moveTo(int newX, int newY){
    x = newX;
    y = newY;
  }
  abstract void draw();
  abstract void resize();
}
class Circle extends GraphicObject{
  public void draw(){
    System.out.println("Draw Circle");
  }
  public void resize(){
    System.out.println("Resize Circle");
  }
}
class Rectangle extends GraphicObject{
  public void draw(){
    System.out.println("Draw Rectangle");
  }
  public void resize(){
    System.out.println("Resize Rectangle");
  }
}
class Abstract{
  public static void main(String[] args){
    Circle obj1 = new Circle();
      obj1.draw();
      obj1.resize();
    Rectangle obj2 = new Rectangle();
      obj2.draw();
      obj2.resize();
  }
}
