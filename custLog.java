import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class custLog implements ActionListener{
	private static JFrame frame;
	private static JPanel panel;
	private static JLabel label1;
	private static JTextField user;
	private static JLabel label2;
	private static JPasswordField pass;
	private static JButton login;
	
	public static void main(String[] args) {
	    frame = new JFrame();
		panel = new JPanel();
		label1 = new JLabel("UserName: ");
		user = new JTextField();
		label2 = new JLabel("Password: ");
		pass = new JPasswordField();
		login = new JButton("Login");
		
		pass.setBounds(90,50,85,25);
		user.setBounds(90,20, 85, 25);
		login.setBounds(80,90,85,25);
		
		login.addActionListener(new custLog());
		
		
		
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(350,200);
		frame.setVisible(true);
		frame.add(panel);
		
		label1.setBounds(10,20, 80, 25);
		label2.setBounds(10, 50, 80, 25);
		
		panel.setLayout(null);
		panel.add(label1);
		panel.add(user);
		panel.add(label2);
		panel.add(pass);
		panel.add(login);
		
		
		
		
		
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		String user1 = user.getText();
		String pass1 = pass.getText();
		
		
		
		if(user1.equals("Deep123") && pass1.equals("deep123")){
			JOptionPane.showMessageDialog(null,"Login Confirmed!!");
			
		}else {
			JOptionPane.showMessageDialog(null, "Failed!!");
		}
		
		
	}

}
