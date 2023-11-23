import os,re
import xml.etree.ElementTree as ET

def getbox(box,w,h):
    xmin=float(box.find("xmin").text)/w
    ymin=float(box.find("ymin").text)/h
    xmax=float(box.find("xmax").text)/w
    ymax=float(box.find("ymax").text)/h
    return ((xmin+xmax)/2,(ymin+ymax)/2,xmax-xmin,ymax-ymin)

def convert(inpath=".",outpath="txt"):
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    filelist=os.listdir(inpath)
    print(filelist)
    regex=re.compile("(.+)\\.xml")
    for file in filelist:
        print(file)
        filename=regex.match(file)
        if(filename):
            txtfile=open(outpath+"/"+filename.group(1)+".txt","w")
            root=ET.parse(inpath+"/"+file).getroot()
            size=root.find("size")
            width=int(size.find("width").text)
            height=int(size.find("height").text)
            for obj in root.iter("object"):
                name=obj.find("name").text
                box=getbox(obj.find("bndbox"),width,height)
                if name =="red":
                    txtfile.write("%s %.6f %.6f %.6f %.6f\n"%(0,*box))
                elif name == "green":
                    txtfile.write("%s %.6f %.6f %.6f %.6f\n" % (1, *box))
                else:
                    txtfile.write("%s %.6f %.6f %.6f %.6f\n" % (2, *box))

            txtfile.close()
        print(file,"converted")

convert("practice_data/labels_backup/robotic_armxml","practice_data/labels_backup/robotic_arm")
#         |      |
#    输入目录 输出目录
