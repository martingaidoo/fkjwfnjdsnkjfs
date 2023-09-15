import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class tetri1 here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */



public class tetri1 extends Actor {

    int velocidadX;
    int velocidadY;
    int referenciaY;
    int referenciaderX;
    int referenciaizqX;
    
    
    boolean movimientoDerecha = false;
    boolean movimientoIzquierda = false;
    boolean movimientoAbajo = false;
    boolean rotarbandera = false;
    boolean acomodar = false;
    
    
    private int timerInterval = 100; // Intervalo de tiempo en milisegundos
    private int timerCounter = 0;

    public void act() {
    
        timerCounter++;

        // Verificar si ha pasado el intervalo de tiempo deseado
        if (timerCounter >= timerInterval) {
            // Llamar a la función que deseas ejecutar
            gravedad();

            // Reiniciar el contador de temporizador
            timerCounter = 0;
        }
        eventoteclado();
        eventotecladorotar();
    
        // Otras acciones del actor
    }
    
    
    
    
    public tetri1(){
        velocidadX = 102;
        velocidadY = 100;
        referenciaY = 900;
        referenciaderX = 800;
        referenciaizqX = 250;
    }
    
    public void eventoteclado(){
        if (Greenfoot.isKeyDown("right") && !movimientoDerecha && getX() < referenciaderX) {
            setLocation(getX() + velocidadX, getY());
            movimientoDerecha = true;
        } else if (!Greenfoot.isKeyDown("right")) {
            movimientoDerecha = false; 
        }
        
        if (Greenfoot.isKeyDown("left") && !movimientoIzquierda && getX() > referenciaizqX) {
            setLocation(getX() - velocidadX, getY());
            movimientoIzquierda = true;
        } else if (!Greenfoot.isKeyDown("left")) {
            movimientoIzquierda = false; 
        }
        
        if (Greenfoot.isKeyDown("down") && !movimientoAbajo && getY() < referenciaY){
            setLocation(getX(), getY() + velocidadY);
            movimientoAbajo = true;
        }
        else if (!Greenfoot.isKeyDown("down")) {
            movimientoAbajo = false; 
        }
    }
    

    public void eventotecladorotar() {
        if (Greenfoot.isKeyDown("space") && !rotarbandera) {
            setRotation(getRotation() + 90);
            rotarbandera = true;
            acomodar = !acomodar;
    
    
            if (acomodar) {
                setLocation(getX() - 50, getY() - 50);
            } else {
                setLocation(getX() + 50, getY() + 50);
            }
        } else if (!Greenfoot.isKeyDown("space")) {
            rotarbandera = false;
        }
    }

    
    
    public void gravedad() {
        if (getY() < referenciaY){
            setLocation(getX(), getY() + velocidadY);
        }
    }
}
