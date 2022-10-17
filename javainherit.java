class You{
    private int a;
    You(){
        a = 5;
    }
}

class Friend extends You{
    void change(){
        a = 10; //private field access
    }
    void disp(){
        System.out.println(a);
    }
}

class javainherit{
    public static void main(String[] args){
        Friend f = new Friend();
        f.change();
        f.disp();
    }
}