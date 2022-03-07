using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AutoGif_windows
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text.Equals("Start Recording"))
            {
                button1.Text = "Stop Recording";
                button1.BackColor = System.Drawing.Color.Red;
            } else
            {
                button1.Text = "Start Recording";
                button1.BackColor = System.Drawing.Color.DarkSeaGreen;
            }
            
        }
    }
}
