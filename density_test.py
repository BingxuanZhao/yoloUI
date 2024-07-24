import xml.etree.ElementTree as ET
import os

def calculate_density(xml_file_path):
    # 检查文件后缀并修改为.xml
    base, ext = os.path.splitext(xml_file_path)
    if ext.lower() == '.png':
        xml_file_path = base + '.xml'

    try:
        # 读取并解析XML文件
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # 提取边界框和name属性
        objects = []
        for obj in root.findall('object'):
            try:
                name = int(obj.find('name').text)
            except ValueError:
                continue  # 如果name无法转换为int，则跳过
            xmin = int(obj.find('bndbox/xmin').text)
            ymin = int(obj.find('bndbox/ymin').text)
            xmax = int(obj.find('bndbox/xmax').text)
            ymax = int(obj.find('bndbox/ymax').text)
            objects.append({'name': name, 'bbox': (xmin, ymin, xmax, ymax), 'element': obj.find('name')})

        # 找出name属性不为0的物体及其边界框
        non_zero_objects = [obj for obj in objects if obj['name'] != 0]
        zero_objects = [obj for obj in objects if obj['name'] == 0]

        # 检查一个边界框是否在另一个边界框内
        def is_within(bbox_inner, bbox_outer):
            return (bbox_outer[0] <= bbox_inner[0] <= bbox_outer[2] and
                    bbox_outer[1] <= bbox_inner[1] <= bbox_outer[3] and
                    bbox_outer[0] <= bbox_inner[2] <= bbox_outer[2] and
                    bbox_outer[1] <= bbox_inner[3] <= bbox_outer[3])

        # 计算并更新每个name属性不为0的区域的密度
        for i, non_zero_obj in enumerate(non_zero_objects):
            bbox = non_zero_obj['bbox']
            bbox_area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
            
            # 统计name属性为0的物体在name属性不为0的物体边界框内的数量
            zero_within_count = sum(
                1 for zero_obj in zero_objects
                if is_within(zero_obj['bbox'], bbox)
            )
            
            # 计算密度
            density = zero_within_count / bbox_area if bbox_area > 0 else 0

            final_density = density * non_zero_obj['name']

            # 更新当前非零物体的name属性
            density_str = f'密度为：{density}'
            non_zero_obj['element'].text = density_str

            # 输出当前更新的信息
            print(f'更新区域 {i+1}/{len(non_zero_objects)}: {density_str}')

        # 保存修改后的XML文件
        tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

        print(f'所有区域密度计算并更新完成。')

    except ET.ParseError as e:
        print(f"XML解析错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

# 示例调用
xml_file_path = 'C:/Users/BxuanZhao/Desktop/aigc/1.xml'
calculate_density(xml_file_path)