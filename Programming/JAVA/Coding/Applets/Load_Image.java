import java.awt.*;
import java.applet.*;
public class Load_Image
{ 
    Image image;
    public void init()
    {
	image=getImage(getCodeBase(),"logo.jpeg");
    }
    public void paint(Graphics g)
    {
	g.drawImage(image,0,0,this);
    }
}