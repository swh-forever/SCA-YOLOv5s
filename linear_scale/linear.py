import numpy as np
anchor = open('./yolo_anchors_kmeans.txt') 
expand_anchor = open('./yolov5_neuron_anchors_kmeans.txt','w') 
ratio=0.5   
base_ratio=3  
box=anchor.read().split(',')
box=np.array(box)
for i in range(0,len(box)):
    box[i]=float(box[i].strip())
box=box.reshape((len(box)//2,2))
new_box=np.zeros((len(box),2))
length = len(box)
new_box[0,0]=int(float(box[0,0])*ratio)
new_box[0,1]=int(float(box[0,1])*ratio)
new_box[-1,0]=int(float(box[-1,0])*base_ratio)
new_box[-1,1]=int(float(box[-1,1])*base_ratio)
print(box)
for i in range(1,length-1):
    new_box[i,0]=(float(box[i,0])-float(box[0,0]))/(float(box[-1,0])-float(box[0,0]))*(new_box[-1,0]-new_box[0,0])+new_box[0,0]
    new_box[i,1]=new_box[i,0]*float(box[i,1])/float(box[i,0])
    new_box[i,0]=int(new_box[i,0])
    new_box[i,1]=int(new_box[i,1])

for i in range(length):
    if i == 0:
        x_y = "%d,%d" % (new_box[i][0], new_box[i][1])
    else:
        x_y = ",  %d,%d" % (new_box[i][0], new_box[i][1])
    expand_anchor.write(x_y)
expand_anchor.close()
anchor.close()

print(new_box)

