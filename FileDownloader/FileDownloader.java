import java.net.*;
import java.io.*;

class UrlData
{
    private String Server;
    private String FilePath;
    private String OutputFileName;
    private int Port;

    public UrlData()
    {
        this.Port = 0;
        this.Server = "";
        this.FilePath = "";
        this.OutputFileName = "";
    }

    public void SetPort(int Port)
    {
        this.Port = Port;
    }

    public int GetPort()
    {
        return this.Port;
    }

    public void SetServer(String Server)
    {
        this.Server = Server;
    }

    public String GetServer()
    {
        return this.Server;
    }

    public void SetFilePath(String FilePath)
    {
        this.FilePath = FilePath;
    }

    public String GetFilePath()
    {
        return this.FilePath;
    }

    public void SetOutputFileName(String OutputFileName)
    {
        this.OutputFileName = OutputFileName;
    }

    public String GetOutputFileName()
    {
        return this.OutputFileName;
    }
}

class FileDownloader
{
    public static UrlData GetUrlData(String Url)
    {
        UrlData Data = new UrlData();
        URL UserUrl;

        try
        {
            UserUrl = new URL(Url);
        }
        catch(MalformedURLException e)
        {
            System.err.println("Error: The URL " + Url +
                               " is not a valid url");
            return null;
        }

        if(UserUrl.getPort() == -1)
        {
            Data.SetPort(80);
        }
        else
        {
            Data.SetPort(UserUrl.getPort());
        }

        Data.SetServer(UserUrl.getHost());
        Data.SetFilePath(UserUrl.getFile());
        Data.SetOutputFileName(Url.substring(Url.lastIndexOf('/')
                                             + 1,
                                             Url.length()));

        return Data;
    }

    public static void GetFile(String Url)
    {
        UrlData Data = GetUrlData(Url);

        if(Data == null)
        {
            return;
        }

        FileOutputStream FileOutputStream = null;
        BufferedInputStream RemoteFileReader = null;
        byte[] ReadBytes = new byte[4*1024];
        int NumReadBytes = 0;
        int TotalBytesRead = 0;

        try
        {
            FileOutputStream =
                new FileOutputStream(Data.GetOutputFileName());
        }
        catch(FileNotFoundException e)
        {
            System.err.println("Error: Could not open output file");
            return;
        }

        try
        {
            RemoteFileReader =
                new BufferedInputStream(new URL(Url).openStream());

            while((NumReadBytes =
                   RemoteFileReader.read(ReadBytes, 0, 4*1024))
                  != -1)
            {
                FileOutputStream.write(ReadBytes, 0, NumReadBytes);
                TotalBytesRead += NumReadBytes;
            }

            System.out.println(Data.GetOutputFileName() +
                               " saved [" +
                               (TotalBytesRead/1024) + "K]");

        }
        catch(MalformedURLException e)
        {
            System.err.println("Error: The specified URL is" +
                               " invalid");
        }
        catch(IOException e)
        {
            System.err.println("Error: An IO exception occurred");
        }
        finally
        {
            try
            {
                if(FileOutputStream != null)
                {
                    FileOutputStream.close();
                }
                if(RemoteFileReader != null)
                {
                    RemoteFileReader.close();
                }
            }
            catch(IOException e)
            {
                System.err.println("Error: Could not close one or" +
                                   " more stream objects");
                return;
            }
        }
    }

    public static void main(String[] args)
    {
        if(args.length < 1)
        {
            System.err.println("Error: Provide at least one" +
                               " url as an argument");
            return;
        }

        for(int i = 0; i < args.length; i++)
        {
            GetFile(args[i]);
        }
    }
}
