import speedtest

test = speedtest.Speedtest()
download = test.download()
upload = test.upload()
downloads=round(((download/1024)/1024),1)
uploads=round(((upload/1024)/1024),1)
print(f"Speed: {downloads} Mb/s \n Upload Speed : {uploads} Mb/s")