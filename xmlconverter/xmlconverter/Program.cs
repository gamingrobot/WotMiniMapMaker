using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml;
using System.IO;
using System.Runtime.CompilerServices;
using Packed_Section_Reader;
using Primitive_File_Reader;

namespace xmlconverter
{
    class Program
    {
        public string PackedFileName = "";
        public static readonly string sver = "0.5";
        public static readonly string stitle = "WoT Mod Tools ";
        public Packed_Section PS = new Packed_Section();
        public Primitive_File PF = new Primitive_File();

        public static readonly Int32 Binary_Header = 0x42a14e65;

        public XmlDocument xDoc;

        string foldername = "";
        string currentfile = "";
        string outfoldername = "";

        static void Main(string[] args)
        {
            if (args.Length != 2)
            {
                args = new string[1];
                args[0] = "";
                args[1] = "";
            }
            new Program().openFolder(args[0], args[1]);
        }

        public void openFolder(string folder, string outfolder)
        {
            Console.WriteLine(folder);
            Console.WriteLine(outfolder);
            System.IO.DirectoryInfo dir = new System.IO.DirectoryInfo(folder);
            foldername = folder;
            outfoldername = outfolder;
            foreach (System.IO.FileInfo file in dir.GetFiles("*.xml"))
            {
                Console.WriteLine("{0}", file.Name);
                currentfile = file.Name;
                string newPath = System.IO.Path.Combine(foldername, currentfile);
                openFile(newPath);
            }
        }

        public void openFile(string file)
        {
            xDoc = new XmlDocument();
            PackedFileName = Path.GetFileName(file);
            PackedFileName = PackedFileName.ToLower();
            //Text = stitle + sver + " - " + PackedFileName;
            FileStream F = new FileStream(file, FileMode.Open, FileAccess.Read);
            BinaryReader reader = new BinaryReader(F);
            Int32 head = reader.ReadInt32();
            if (head == Packed_Section.Packed_Header)
            {
                DecodePackedFile(reader);
            }
            else if (head == Binary_Header)
            {
                ReadPrimitiveFile(file);
                //saveAsToolStripMenuItem.Enabled = true;
                //btnSave.Enabled = true;
            }
            else
            {
                if (PackedFileName.Contains(".xml") || PackedFileName.Contains(".def") || PackedFileName.Contains(".visual") || PackedFileName.Contains(".chunk") || PackedFileName.Contains(".settings") || PackedFileName.Contains(".model"))
                {
                    //txtOut.LoadFile(file, RichTextBoxStreamType.PlainText);
                }
                else
                {
                    throw new IOException("Invalid header");
                }
            }
            reader.Close();
            F.Close();
        }

        public void DecodePackedFile(BinaryReader reader)
        {
            reader.ReadSByte();

            List<string> dictionary = PS.readDictionary(reader);

            XmlNode xmlroot = xDoc.CreateNode(XmlNodeType.Element, PackedFileName, "");

            PS.readElement(reader, xmlroot, xDoc, dictionary);

            xDoc.AppendChild(xmlroot);

            //txtOut.AppendText(FormatXml(xDoc.OuterXml));
            //Console.Write(FormatXml(xDoc.OuterXml));
            string newPath = System.IO.Path.Combine(outfoldername, currentfile);
            System.IO.StreamWriter outfile = new System.IO.StreamWriter(newPath);
            outfile.WriteLine(FormatXml(xDoc.OuterXml));

            outfile.Close();
        }

        public void ReadPrimitiveFile(string file)
        {
            FileStream F = new FileStream(file, FileMode.Open, FileAccess.Read);
            BinaryReader reader = new BinaryReader(F);

            XmlComment ptiComment = xDoc.CreateComment("DO NOT SAVE THIS FILE! THIS CODE IS JUST FOR INFORMATION PUPORSES!");

            XmlNode xmlprimitives = xDoc.CreateNode(XmlNodeType.Element, "primitives", "");

            PF.ReadPrimitives(reader, xmlprimitives, xDoc);

            xDoc.AppendChild(ptiComment);
            xDoc.AppendChild(xmlprimitives);

            F.Close();

            //txtOut.AppendText(FormatXml(xDoc.OuterXml));
            //Console.Write(FormatXml(xDoc.OuterXml));
            string newPath = System.IO.Path.Combine(outfoldername, currentfile);
            System.IO.StreamWriter outfile = new System.IO.StreamWriter(newPath);
            outfile.WriteLine(FormatXml(xDoc.OuterXml));

            outfile.Close();
        }

        private string FormatXml(string sUnformattedXml)
        {
            //load unformatted xml into a dom

            XmlDocument xd = new XmlDocument();
            xd.LoadXml(sUnformattedXml);

            //will hold formatted xml

            StringBuilder sb = new StringBuilder();

            //pumps the formatted xml into the StringBuilder above

            StringWriter sw = new StringWriter(sb);

            //does the formatting

            XmlTextWriter xtw = null;

            try
            {
                //point the xtw at the StringWriter

                xtw = new XmlTextWriter(sw);

                //we want the output formatted

                xtw.Formatting = Formatting.Indented;

                //get the dom to dump its contents into the xtw 

                xd.WriteTo(xtw);
            }
            finally
            {
                //clean up even if error

                if (xtw != null)
                    xtw.Close();
            }

            //return the formatted xml

            return sb.ToString();
        }
    }
}
