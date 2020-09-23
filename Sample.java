//Practice question for java

class Emp{
    int eid , age;
    static String ceo;
    
    
}
class A extends Emp{
    string name;
    public void show(){
        System.out.println("Eid" + ":"+ eid + "age: " + age + "Ceo :" + ceo + " Name " + name );
    }
}
class Sample {
    public static void main(String args[]){
        A obj = new A();
        obj.eid = 123;
        obj.age = 23;
        obj.name = "eep";
        A.ceo = "Makita";

        obj.show();
    }
}