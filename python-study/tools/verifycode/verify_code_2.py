#encoding:gbk


import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

_letter_cases = "abcdefghjkmnpqrstuvwxy" # Сд��ĸ��ȥ�����ܸ��ŵ�i��l��o��z
_upper_cases = _letter_cases.upper() # ��д��ĸ
_numbers = ''.join(map(str, range(3, 10))) # ����
init_chars = ''.join((_letter_cases, _upper_cases, _numbers))

def create_validate_code(size=(120, 30),
                         chars=init_chars,
                         img_type="GIF",
                         mode="RGB",
                         bg_color=(255, 255, 255),
                         fg_color=(0, 0, 255),
                         font_size=18,
                         font_type="ae_AlArabiya.ttf",
                         length=4,
                         draw_lines=True,
                         n_line=(1, 2),
                         draw_points=True,
                         point_chance = 2):
    '''
    @todo: ������֤��ͼƬ
    @param size: ͼƬ�Ĵ�С����ʽ�����ߣ���Ĭ��Ϊ(120, 30)
    @param chars: ������ַ����ϣ���ʽ�ַ���
    @param img_type: ͼƬ����ĸ�ʽ��Ĭ��ΪGIF����ѡ��ΪGIF��JPEG��TIFF��PNG
    @param mode: ͼƬģʽ��Ĭ��ΪRGB
    @param bg_color: ������ɫ��Ĭ��Ϊ��ɫ
    @param fg_color: ǰ��ɫ����֤���ַ���ɫ��Ĭ��Ϊ��ɫ#0000FF
    @param font_size: ��֤�������С
    @param font_type: ��֤�����壬Ĭ��Ϊ ae_AlArabiya.ttf
    @param length: ��֤���ַ�����
    @param draw_lines: �Ƿ񻮸�����
    @param n_lines: �����ߵ�������Χ����ʽԪ�飬Ĭ��Ϊ(1, 2)��ֻ��draw_linesΪTrueʱ��Ч
    @param draw_points: �Ƿ񻭸��ŵ�
    @param point_chance: ���ŵ���ֵĸ��ʣ���С��Χ[0, 100]
    @return: [0]: PIL Imageʵ��
    @return: [1]: ��֤��ͼƬ�е��ַ���
    '''

    width, height = size # �� ��
    img = Image.new(mode, size, bg_color) # ����ͼ��
    draw = ImageDraw.Draw(img) # ��������

    def get_chars():
        '''���ɸ������ȵ��ַ����������б��ʽ'''
        return random.sample(chars, length)

    def create_lines():
        '''���Ƹ�����'''
        line_num = random.randint(*n_line) # ����������

        for i in range(line_num):
            # ��ʼ��
            begin = (random.randint(0, size[0]), random.randint(0, size[1]))
            #������
            end = (random.randint(0, size[0]), random.randint(0, size[1]))
            draw.line([begin, end], fill=(0, 0, 0))

    def create_points():
        '''���Ƹ��ŵ�'''
        chance = min(100, max(0, int(point_chance))) # ��С������[0, 100]
       
        for w in xrange(width):
            for h in xrange(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=(0, 0, 0))

    def create_strs():
        '''������֤���ַ�'''
        c_chars = get_chars()
        strs = ' %s ' % ' '.join(c_chars) # ÿ���ַ�ǰ���Կո����
       
        font = ImageFont.truetype(font_type, font_size)
        font_width, font_height = font.getsize(strs)

        draw.text(((width - font_width) / 3, (height - font_height) / 3),
                    strs, font=font, fill=fg_color)
       
        return ''.join(c_chars)

    if draw_lines:
        create_lines()
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

    return img, strs

if __name__ == "__main__":
    code_img,code = create_validate_code(font_type="arial.ttf")
    #code_img.save("validate.gif", "GIF")
    code_img.save("validate.jpg", "JPEG")
    print code