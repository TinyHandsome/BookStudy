import java.awt.*;
import javax.swing.*;

public class BallGame extends JFrame{
	
	// 加载图片
	Image ball = Toolkit.getDefaultToolkit().getImage("image/ball.png");
	Image desk = Toolkit.getDefaultToolkit().getImage("image/desk.jpg");
	
	double x = 100;		// 小球的横坐标
	double y = 100;		// 小球的纵坐标
	boolean right = true;		// 方向
	
	
	// 绘制窗口的方法
	public void paint(Graphics g){
		System.out.println("窗口被画了一次");
		g.drawImage(desk, 0, 0, null);
		g.drawImage(ball, (int)x, (int)y, null);
		
		if(right){
			x = x + 20;
		}
		else{
			x = x - 20;
		}
		
		if(x>856-40-30){
			right = false;
		}
		if(x<40){
			right = true;
		}
	}
	
	// 窗口加载
	void launchFrame(){
		setSize(856, 500);
		setLocation(50, 50);
		setVisible(true);
		
		// 重画窗口
		while(true){
			repaint();
			try{
				Thread.sleep(40);		// 40ms，大约1s绘制25次
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
	
	public static void main(String[] args){
		System.out.println("Happy Game！");
		BallGame game = new BallGame();
		game.launchFrame();
	}

}
