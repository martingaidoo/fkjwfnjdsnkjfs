import greenfoot.*;

public class miMundo extends World
{
    private int timer;
    private int deadcar;
    private int timer2;
    
    public miMundo()
    {    
        super(1200, 500, 1); 
        timer = 0;
        timer2 = 0;
        addObject(new myCar(), 1000, 250);
        deadcar = 0;

    }
    
    public void act(){
        timer = timer+1;
        timer2 = timer2+1;
        prepare();
        eliminarMileuristasSiSeVan();
        eliminarBala();
    }
    
    private void prepare(){
        if (timer == 200){
            addObject(new mileurista(), 0, Greenfoot.getRandomNumber(450));
            timer = 0;
        }
        if (timer2 == 500){
            addObject(new tanque(), 0, Greenfoot.getRandomNumber(450));
            timer2 = 0;
        }
    }
    
    private void eliminarMileuristasSiSeVan(){
        java.util.List<mileurista> mileuristas = getObjects(mileurista.class);
        
        for (mileurista m : mileuristas) {
            if (m.getX() >= 1190) {
                removeObject(m);
            }
        }
    }
    
    private void eliminarBala(){
        java.util.List<Bullet> Bullet = getObjects(Bullet.class);
        
        for (Bullet m : Bullet) {
            if (m.getX() <= 10) {
                removeObject(m);
            }
        }
    }
}
