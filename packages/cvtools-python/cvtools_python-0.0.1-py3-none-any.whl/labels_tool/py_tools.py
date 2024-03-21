# encoding=utf8
# author:nxp

import cv2, os, shutil, re
import xml.etree.ElementTree as ET

from loguru import logger as logging
import sys

logging.remove()  # Remove the pre-configured handler
logging.add(sys.stderr, format="<green>{level}</green> <green>{time:MM.DD HH:mm:ss}</green> <blue>{file}:{line}:</blue> <green>{message}</green>")

class py_tools_diy:

    def label_change(self,inpath,outpath,inid,outid,save_res = True):
        '''
        Args:
            inpath:     输入路径
            outpath:    输出路径
            inid:       输入的label号
            outid:      输出的label号
            save_res:   是否保存
        '''

        files = []
        for file in os.listdir(inpath):
            if file.endswith(".txt"):
                files.append(inpath + file)

        '''
        抽取部分种类保存至lists11中
        '''
        list_class = []

        for file in files:
            with open(file, 'r') as f:
                txt = f.readlines()
                f.close()
                if all(txt1.split(' ')[0] in [f'{inid}'] for txt1 in txt):

                    # shutil.copy(file, path + file.split('/')[-1].split('.')[0] + '.txt')
                    # shutil.copy(path22 + file.split('/')[-1].split('.')[0] + '.jpg', path2 + file.split('/')[-1].split('.')[0] + '.jpg')
                    list_class.append(file)

                    logging.info('{}完成！'.format(file))

        logging.info('数据量{}！'.format(len(list_class)))
        '''
        修改标签种类
        '''
        if save_res:
            for file in list_class:
                with open(file, 'r') as f:
                    new_data = re.sub('^{}'.format(inid), f'{outid}', f.read(), flags=re.MULTILINE)    # 将列中的1替换为0
                file11 = file.split('/')[-1]
                with open(outpath + file11, 'w') as f:
                    f.write(new_data)

    def resample(self,fileDir,outDir,innum):

        '''
        Args:
            fileDir:    输入路径
            outDir:     输出路径
            innum:      采样间隔
        '''

        if not os.path.exists(outDir):
            os.mkdir(outDir)

        pathDir = os.listdir(fileDir)[0::innum]
        for ii in pathDir:
            shutil.move(fileDir + ii, outDir + ii)

    def rename(self,inpath,outpath,i,str_name,ext_name):
        '''

        Args:
            inpath:     输入路径
            outpath:    输出路径
            i:          起始id号
            str_name:   重命名后name，'{:06d}BC'
            ext_name:   扩展名（.jpg）

        Returns:

        '''
        # i = 15000
        if not os.path.exists(outpath):
            os.mkdir(outpath)
        filelist = os.listdir(inpath)  # 该文件夹下所有的文件（包括文件夹）
        for files in filelist:  # 遍历所有文件

            Olddir = os.path.join(inpath, files)  # 原来的文件路径
            if os.path.isdir(Olddir):  # 如果是文件夹则跳过
                continue
            filename = ''  # 文件名
            filetype = ext_name  # 文件扩展名
            Newdir = os.path.join(outpath, filename + '{:06d}BC'.format(i) + filetype)  # 新的文件路径
            os.rename(Olddir, Newdir)  # 重命名
            i = i + 1
        return True

    def pic2vid(self, input, output, cap_fps, size):

        '''
        Args:
            input:输入的图片文件夹路径
            output:输出的视频路径及名字
            cap_fps:帧率（1），
            注意！！！
            size要和图片的size一样，但是通过img.shape得到图像的参数是（height，width，channel），但是此处的size要传的是（width，height），这里一定要注意注意不然结果会打不开，比如通过img.shape得到常用的图片尺寸
        '''

        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # 设置输出视频为mp4格式

        # 设置输出视频的参数，如果是灰度图，可以加上 isColor = 0 这个参数
        # video = cv2.VideoWriter('results/result.avi',fourcc, cap_fps, size, isColor=0)
        video = cv2.VideoWriter(output, fourcc, cap_fps, size)

        file_lst = os.listdir(input)
        for filename in file_lst:
            img = cv2.imread(input + filename)
            video.write(img)
        video.release()


    def xml2txt(self,xml_files_path, save_txt_filws_path, classes):

        '''
        Args:
            xml_files_path:  xml文件夹路径
            save_txt_filws_path:    输出文件夹路径
            classes:    类别， classes = ["RBC", "WBC", "Ascaris Egg"]
        '''

        xml_files = os.listdir(xml_files_path)
        for xml_name in xml_files:
            xml_file = os.path.join(xml_files_path, xml_name)
            xxx, _ = os.path.splitext(xml_name)
            out_txt_path = os.path.join(save_txt_filws_path, xxx + '.txt')
            # out_txt_path = os.path.join(save_txt_filws_path, xml_name.split(',')[0] + '.txt')
            out_txt_f = open(out_txt_path, 'w')
            tree = ET.parse(xml_file)
            root = tree.getroot()
            size = root.find('size')
            w = int(size.find('width').text)
            h = int(size.find('height').text)

            for obj in root.iter('object'):
                difficult = obj.find('difficult').text
                cls = obj.find('name').text
                if cls not in classes or int(difficult) == 1:
                    continue
                cls_id = classes.index(cls)
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                     float(xmlbox.find('ymax').text))

                '''
                
                def convert(size, box):import xml.etree.ElementTree as ET
                    x_center = (box[0] + box[1])/2.0
                    y_center = (box[2] + box[3])/2.0
                    x = x_center / size[0]
                    y = y_center / size[1]
                
                    w = (box[1] - box[0]) / size[0]
                    h = (box[3] - box[2]) / size[1]
                
                    return (x,y,w,h)
                
                '''
                x_center = (b[0] + b[1]) / 2.0
                y_center = (b[2] + b[3]) / 2.0
                x = x_center / (w, h)[0]
                y = y_center / (w, h)[1]

                w = (b[1] - b[0]) / (w, h)[0]
                h = (b[3] - b[2]) / (w, h)[1]

                bb = (x, y, w, h)

                out_txt_f.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')



if __name__=='__main__':
    tools1 = py_tools_diy()
    inpath = r'D:\work2\data\low_2_23\undeal_images\鞭虫低倍'
    outpath = r'D:\work2\data\low_2_23\undeal_images\鞭虫低倍'
    tools1.rename(inpath,outpath,'.jpg')
