from PIL import Image

im = Image.open('pesawat.png')

idx = 1
for i in range(0,20):
	for j in range(0,20):
		im.crop((2+j*28,2+i*28,26+j*28,26+i*28)).resize((25,25), Image.ANTIALIAS).rotate(-90).save('pesawat'+str(idx)+'.png')
		idx += 1

