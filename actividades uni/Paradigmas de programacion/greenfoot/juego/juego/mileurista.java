import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class mileurista extends myCar
{   private int speed;
    private int deadcar;
    private boolean elimina;
    
    public mileurista(){
    speed = Greenfoot.getRandomNumber(5)+1;
    }
    public void act()
    {
        setLocation(getX()+speed, getY());        
        checkCollision2();
        girar();
    }
        
    public void girar(){
        
        if (speed==3){
            turn(3);
        }
        if (deadcar==15){
            speed=speed+100 ;
        }
    }
    
    public void checkCollision() 
    {
        mileurista a = (mileurista) getOneIntersectingObject(mileurista.class);

        if (a != null) {
            getWorld().addObject(new Explosion(), getX(), getY());
            getWorld().removeObject(this);
        }
    }
    public void checkCollision2() 
    {
        Bullet a = (Bullet) getOneIntersectingObject(Bullet.class);
        if (a != null) {
            getWorld().addObject(new Explosion(), getX(), getY());
            getWorld().removeObject(a); // Elimina la instancia de Bullet que colisionó
            getWorld().removeObject(this); // Elimina la instancia actual

        }
    }
    

        // Add your action code here.
}