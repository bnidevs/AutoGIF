using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AutoGif_windows
{
    public partial class main_window : Form
    {
        bool recording = false;
        public main_window()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (recording)
            {
                button1.Text = "Start Recording";
                button1.BackColor = System.Drawing.Color.DarkSeaGreen;
                recording = false;
            } else {
                button1.Text = "Stop Recording";
                button1.BackColor = System.Drawing.Color.Red;
                recording = true;
            }
            
        }

        private void timer1_Tick(object sender, EventArgs e)
        {

        }

        private void main_window_Load(object sender, EventArgs e)
        {
            timer1 = new Timer();
            timer1.Interval = 10;
            timer1.Tick += timer1_Tick;
        }
    }
}
