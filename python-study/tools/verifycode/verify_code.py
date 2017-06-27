#encoding:gbk

import random 
from PIL import Image, ImageDraw, ImageFont, ImageFilter 
import StringIO

#from flask import Flask
 
#map:��str���������ں������е�ÿһ��Ԫ��
numbers = ''.join(map(str, range(10)))
chars = ''.join((numbers)) 
 
def create_validate_code(size=(120, 30), 
                         chars=chars, 
                         mode="RGB", 
                         bg_color=(255, 255, 255), 
                         fg_color=(255, 0, 0), 
                         font_size=18, 
                         font_type="Monaco.ttf", 
                         #font_type="COOPBL.TTF", 
                         length=4, 
                         draw_points=True, 
                         point_chance = 2): 
    '''''
    size: ͼƬ�Ĵ�С����ʽ�����ߣ���Ĭ��Ϊ(120, 30)
    chars: ������ַ����ϣ���ʽ�ַ���
    mode: ͼƬģʽ��Ĭ��ΪRGB
    bg_color: ������ɫ��Ĭ��Ϊ��ɫ
    fg_color: ǰ��ɫ����֤���ַ���ɫ
    font_size: ��֤�������С
    font_type: ��֤�����壬Ĭ��Ϊ Monaco.ttf
    length: ��֤���ַ�����
    draw_points: �Ƿ񻭸��ŵ�
    point_chance: ���ŵ���ֵĸ��ʣ���С��Χ[0, 50]
    ''' 
 
    width, height = size 
    img = Image.new(mode, size, bg_color) # ����ͼ�� 
    draw = ImageDraw.Draw(img) # �������� 
 
    def get_chars(): 
        '''''���ɸ������ȵ��ַ����������б��ʽ''' 
        return random.sample(chars, length) 
 
    def create_points(): 
        '''''���Ƹ��ŵ�''' 
        chance = min(50, max(0, int(point_chance))) # ��С������[0, 50] 
 
        for w in xrange(width): 
            for h in xrange(height): 
                tmp = random.randint(0, 50) 
                if tmp > 50 - chance: 
                    draw.point((w, h), fill=(0, 0, 0)) 
 
    def create_strs(): 
        '''''������֤���ַ�''' 
        c_chars = get_chars() 
        strs = '%s' % ''.join(c_chars) 
 
        font = ImageFont.truetype(font_type, font_size) 
        font_width, font_height = font.getsize(strs) 
 
        draw.text(((width - font_width) / 3, (height - font_height) / 4), 
                    strs, font=font, fill=fg_color) 
 
        return strs 
 
    if draw_points: 
        create_points() 
    strs = create_strs() 
 
    # ͼ��Ť������ 
    params = [1 - float(random.randint(1, 2)) / 100, 
              0, 
              0, 
              0, 
              1 - float(random.randint(1, 10)) / 100, 
              float(random.randint(1, 2)) / 500, 
              0.001, 
              float(random.randint(1, 2)) / 500 
              ] 
    img = img.transform(size, Image.PERSPECTIVE, params) # ����Ť�� 
 
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) # �˾����߽��ǿ����ֵ���� 
 
    return img,strs 

# �����ͼƬ������
def test_func1():
    code_img,code=create_validate_code(font_type="arial.ttf")
    print type(code_img),code
    buf = StringIO.StringIO() 
    code_img.save(buf,'JPEG',quality=70) 
    
    buf_str = buf.getvalue() 
    print type(buf_str)
    try:
        jpeg_file=open("123.jpeg","w")
        jpeg_file.write(buf_str)
        jpeg_file.close()
    except Exception,e:
        print e

# 
def test_func2():
    code_img,code=create_validate_code(font_type="arial.ttf")
    print type(code_img),code
    code_img.save("123s.jpg", "JPEG")
        
if __name__=="__main__":
    #test_func1()
    test_func2()
