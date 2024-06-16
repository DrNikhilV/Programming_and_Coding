package Swings;
import java.awt.*;

import java.awt.event.*; 
public class MouseListenerExample extends Frame implements MouseListener{

Label I; 
Frame f=new Frame();
MouseListenerExample()
{ 
    addMouseListener(this);

I=new Label();

I.setBounds(20,50,100,20);

f.add(I);

f.setSize(300,300); f.setLayout(null);

f. setVisible(true);
} 

public void mouseClicked(MouseEvent e)  
{
I.setText("Mouse Clicked");
}

public void mouseEntered (MouseEvent e) 
{
I.setText("Mouse Entered");
} 

public void mouseExited (MouseEvent e) 
{
     I.setText("Mouse Exited");
}

public void mousePressed(MouseEvent e) 
{ 
  I.setText("Mouse Pressed");
} 

public void mouseReleased (MouseEvent e) 
{
I.setText("Mouse Released");
} 
public static void main(String[] args) 
{ 
    new MouseListenerExample();
}
}