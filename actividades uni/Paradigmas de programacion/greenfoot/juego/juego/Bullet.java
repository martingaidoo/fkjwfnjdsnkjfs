import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Bullet here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Bullet extends Actor {
    private int speed;

    public Bullet(int direction, int speed) {
        this.speed = speed;
        setRotation(direction);
    }

    public void act() {
        move(speed); // Mueve la bala hacia la izquierda (negativo)
        // Agrega lógica adicional según sea necesario
    }
    
}



