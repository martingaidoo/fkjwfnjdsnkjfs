import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class myCar here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class myCar extends Actor
{
    /**
     * Act - do whatever the myCar wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    private int shotsFired; 
    private int gunReloadTime; 
    private int reloadDelayCount; 
    
    public myCar(){
        gunReloadTime = 100;
        reloadDelayCount = 0; 
        shotsFired = 0;
    }
    
    public void act()
    {
        checkKeyPress();
        checkCollision();
        reloadDelayCount++;
        // Add your action code here.
    }
    
    public void checkKeyPress()
    {
        if (Greenfoot.isKeyDown("up")) 
        {
            setLocation(getX(), getY()-8);
        }
        
        if (Greenfoot.isKeyDown("down")) 
        {
            setLocation(getX(), getY()+8);
        }
        if(Greenfoot.isKeyDown("space")) {
            fire();
        }    
    }

    
    
    public void fire() {
        if (reloadDelayCount >= gunReloadTime) {
            int bulletDirection = 180; // 180 grados para ir hacia la izquierda
            int bulletSpeed = 5; // Establece la velocidad de la bala
    
            Bullet b = new Bullet(bulletDirection, bulletSpeed);
            getWorld().addObject(b, getX(), getY());
            shotsFired++;
            reloadDelayCount = 0; // Tiempo desde el último disparo
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
    

}
