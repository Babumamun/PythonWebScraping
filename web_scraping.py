import requests
#get the website link for scraping
r=requests.get("https://web.facebook.com/?_rdc=1&_rdr.html")
#save in the desktop
write1=open("/Users/mac/Desktop/my_fb","w",encoding="utf-8")
#write the file
write1.write(r.text)
#get the link for image
image=requests.get("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=1200:*")
#save in the desktop
write2=open("/Users/mac/Desktop/my_dog.png","wb")
#get image
write2.write(image.content)
write1.close()
print("done")