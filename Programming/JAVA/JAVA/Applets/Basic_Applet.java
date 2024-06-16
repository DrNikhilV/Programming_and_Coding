/*Java Program to Create a Basic Applet*/
import java.applet.*;
import java.awt.*;
public class Basic_Applet extends Applet
{
    //Function to initialize the applet
    public void init()
    {
	setBackground(Color.white);
	setLayout(new FlowLayout(FlowLayout.CENTER));
    }
    //Function to draw the string
    public void paint(Graphics g)
    {
	g.drawString("Hello World",100,200);
    }
}
/*
<applet code=Basic_Applet.class width=400 height=400>
</applet>
*/