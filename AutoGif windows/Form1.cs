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

using GifMotion;
using System.IO;
using AForge.Video;

namespace AutoGif_windows
{
    public partial class main_window : Form
    {
        bool recording;
        ScreenCaptureStream scr;
        List<Image> frame_list = new List<Image>();
        public main_window()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (recording)
            {
                scr.SignalToStop();
                scr.WaitForStop();
                string workingPath = Directory.GetParent(Environment.CurrentDirectory).Parent.Parent.FullName;
                using (GifCreator gifCreator = AnimatedGif.Create(workingPath + "/test.gif", 33))
                {
                    foreach (Image img in frame_list) 
                    {
                        using (img) 
                        {
                            // Add the image to gifEncoder with default Quality
                            Console.WriteLine(img);
                            Console.WriteLine("HULLO GAMERS");
                            //gifCreator.AddFrame(img);
                        } // Image disposed
                    }
                    
                }
                button1.Text = "Start Recording";
                button1.BackColor = System.Drawing.Color.DarkSeaGreen;
                recording = false;
            } else {
                scr.Start();
                button1.Text = "Stop Recording";
                button1.BackColor = System.Drawing.Color.Red;
                recording = true;
            }
            
        }

        private void main_window_Load(object sender, EventArgs e)
        {
            Rectangle screenArea = Rectangle.Empty;
            foreach (System.Windows.Forms.Screen screen in System.Windows.Forms.Screen.AllScreens)
            {
                screenArea = Rectangle.Union(screenArea, screen.Bounds);
            }
            recording = false;
            scr = new ScreenCaptureStream(screenArea);
            scr.NewFrame += new NewFrameEventHandler(video_NewFrame);
        }
        private void video_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            // get new frame
            Bitmap bmp = eventArgs.Frame;
            frame_list.Add(bmp);
        }
    }
}
