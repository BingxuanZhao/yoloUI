
import os
from PIL import Image

def txtLabel_to_xmlLabel(classes_file, source_pth, save_xml_pth):
    if not os.path.exists(save_xml_pth):
        os.makedirs(save_xml_pth)
    
    with open(classes_file) as f:
        classes = f.read().splitlines()
    
    print(classes)
    
    for file in os.listdir(source_pth):
        if not file.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
            continue
        
        img_file_path = os.path.join(source_pth, file)
        img_file = Image.open(img_file_path)
        
        txt_file_path = os.path.join(source_pth, file.rsplit('.', 1)[0] + '.txt')
        if os.path.exists(txt_file_path):
            with open(txt_file_path) as f:
                txt_file = f.read().splitlines()
        else:
            print(f"{file} 对应的文本文件未找到")
            continue
        
        xml_file_path = os.path.join(save_xml_pth, file.rsplit('.', 1)[0] + '.xml')
        with open(xml_file_path, 'w') as xml_file:
            width, height = img_file.size
            xml_file.write('<annotation>\n')
            xml_file.write('\t<folder>simple</folder>\n')
            xml_file.write(f'\t<filename>{file}</filename>\n')
            xml_file.write('\t<size>\n')
            xml_file.write(f'\t\t<width>{width}</width>\n')
            xml_file.write(f'\t\t<height>{height}</height>\n')
            xml_file.write(f'\t\t<depth>{3}</depth>\n')  # 修改了depth为3以处理RGB图像
            xml_file.write('\t</size>\n')
            
            for line in txt_file:
                line_split = line.split(' ')
                class_id = int(line_split[0])
                x_center = float(line_split[1])
                y_center = float(line_split[2])
                w = float(line_split[3])
                h = float(line_split[4])
                
                xmax = int((2 * x_center * width + w * width) / 2)
                xmin = int((2 * x_center * width - w * width) / 2)
                ymax = int((2 * y_center * height + h * height) / 2)
                ymin = int((2 * y_center * height - h * height) / 2)
                
                xml_file.write('\t<object>\n')
                xml_file.write(f'\t\t<name>{classes[class_id]}</name>\n')
                xml_file.write('\t\t<pose>Unspecified</pose>\n')
                xml_file.write('\t\t<truncated>0</truncated>\n')
                xml_file.write('\t\t<difficult>0</difficult>\n')
                xml_file.write('\t\t<bndbox>\n')
                xml_file.write(f'\t\t\t<xmin>{xmin}</xmin>\n')
                xml_file.write(f'\t\t\t<ymin>{ymin}</ymin>\n')
                xml_file.write(f'\t\t\t<xmax>{xmax}</xmax>\n')
                xml_file.write(f'\t\t\t<ymax>{ymax}</ymax>\n')
                xml_file.write('\t\t</bndbox>\n')
                xml_file.write('\t</object>\n')
            
            xml_file.write('</annotation>\n')

# if __name__ == '__main__':
#     classes_file = r"/home/saiki/Documents/test-help/classes.txt"
#     txtLabel_to_xmlLabel(r'/home/saiki/Documents/test-help/', r'/home/saiki/Documents/test-help/xml/')
