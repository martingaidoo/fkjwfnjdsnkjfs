import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class tanque here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class tanque extends mileurista
{
    private int speed;
    
    /**
     * Act - do whatever the tanque wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    
    public tanque(){
    
    speed = Greenfoot.getRandomNumber(3)+1;
    }
    public void act()
    {
        setLocation(getX()+speed, getY());        
        checkCollision2();
        girar();
    }
}
