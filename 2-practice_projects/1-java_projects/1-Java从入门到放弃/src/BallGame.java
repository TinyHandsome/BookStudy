import java.awt.*;
import javax.swing.*;

public class BallGame extends JFrame{
	
	// ����ͼƬ
	Image ball = Toolkit.getDefaultToolkit().getImage("image/ball.png");
	Image desk = Toolkit.getDefaultToolkit().getImage("image/desk.jpg");
	
	double x = 100;		// С��ĺ�����
	double y = 100;		// С���������
	boolean right = true;		// ����
	
	
	// ���ƴ��ڵķ���
	public void paint(Graphics g){
		System.out.println("���ڱ�����һ��");
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
	
	// ���ڼ���
	void launchFrame(){
		setSize(856, 500);
		setLocation(50, 50);
		setVisible(true);
		
		// �ػ�����
		while(true){
			repaint();
			try{
				Thread.sleep(40);		// 40ms����Լ1s����25��
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
	
	public static void main(String[] args){
		System.out.println("Happy Game��");
		BallGame game = new BallGame();
		game.launchFrame();
	}

}
