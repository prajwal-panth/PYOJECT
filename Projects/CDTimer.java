package Projects;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CDTimer extends JFrame {
    JLabel timeLabel;
    JButton startButton, stopButton, resetButton;
    JRadioButton black, white, defaultTheme;
    JTextField hoursField, minutesField, secondsField;
    Timer timer;
    int timeLeft; // Time in seconds

    CDTimer(String title) {
        super(title);
    }

    public static void main(String[] args) {
        CDTimer ob = new CDTimer("Countdown Timer");
        ob.setdetails();
        ob.setVisible(true);
        ob.setSize(400, 400);
        ob.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void setdetails() {
        timeLabel = new JLabel("Time left: 00:00:00");
        startButton = new JButton("Start");
        stopButton = new JButton("Stop");
        resetButton = new JButton("Reset");
        black = new JRadioButton("BLACK");
        white = new JRadioButton("WHITE");
        defaultTheme = new JRadioButton("Default Theme");
        hoursField = new JTextField("0");
        minutesField = new JTextField("0");
        secondsField = new JTextField("0");

        ButtonGroup group = new ButtonGroup();
        group.add(black);
        group.add(white);
        group.add(defaultTheme);

        setLayout(null);

        timeLabel.setBounds(100, 30, 200, 30);
        hoursField.setBounds(50, 70, 50, 30);
        minutesField.setBounds(110, 70, 50, 30);
        secondsField.setBounds(170, 70, 50, 30);
        startButton.setBounds(30, 110, 80, 30);
        stopButton.setBounds(120, 110, 80, 30);
        resetButton.setBounds(210, 110, 80, 30);
        black.setBounds(30, 150, 80, 30);
        white.setBounds(120, 150, 80, 30);
        defaultTheme.setBounds(210, 150, 120, 30);

        startButton.addActionListener(new TimerListener());
        stopButton.addActionListener(new TimerListener());
        resetButton.addActionListener(new TimerListener());
        black.addActionListener(new ThemeListener());
        white.addActionListener(new ThemeListener());
        defaultTheme.addActionListener(new ThemeListener());

        add(timeLabel);
        add(hoursField);
        add(minutesField);
        add(secondsField);
        add(startButton);
        add(stopButton);
        add(resetButton);
        add(black);
        add(white);
        add(defaultTheme);

        timer = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (timeLeft > 0) {
                    timeLeft--;
                    int hours = timeLeft / 3600;
                    int minutes = (timeLeft % 3600) / 60;
                    int seconds = timeLeft % 60;
                    timeLabel.setText(String.format("Time left: %02d:%02d:%02d", hours, minutes, seconds));
                } else {
                    timer.stop();
                    timeLabel.setText("Time's up!");
                }
            }
        });
    }

    class TimerListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            if (e.getSource() == startButton) {
                int hours = Integer.parseInt(hoursField.getText());
                int minutes = Integer.parseInt(minutesField.getText());
                int seconds = Integer.parseInt(secondsField.getText());
                timeLeft = hours * 3600 + minutes * 60 + seconds;
                timer.start();
            } else if (e.getSource() == stopButton) {
                timer.stop();
            } else if (e.getSource() == resetButton) {
                timer.stop();
                hoursField.setText("0");
                minutesField.setText("0");
                secondsField.setText("0");
                timeLabel.setText("Time left: 00:00:00");
            }
        }
    }

    class ThemeListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            if (e.getSource() == black) {
                getContentPane().setBackground(Color.BLACK);
            } else if (e.getSource() == white) {
                getContentPane().setBackground(Color.WHITE);
            } else if (e.getSource() == defaultTheme) {
                getContentPane().setBackground(null);
            }
        }
    }
}
