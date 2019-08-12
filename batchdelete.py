import datetime
import os

# 把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12
import time

def strToDateTime(dateStr, format):
    return datetime.datetime.strptime(dateStr, format)

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

# 获取文件的大小,结果保留两位小数，单位为MB
def get_FileSize(filePath):
    # filePath = unicode(filePath, 'utf8')
    filePath = filePath.encode('utf-8')
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


# 获取文件的访问时间
def get_FileAccessTime(filePath):
    filePath = filePath.encode('utf-8')
    return os.path.getatime(filePath)


# 获取文件的创建时间
def get_FileCreateTime(filePath):
    filePath = filePath.encode('utf-8')
    return os.path.getctime(filePath)


# 获取文件的修改时间
def get_FileModifyTime(filePath):
    filePath = filePath.encode('utf-8')
    return os.path.getmtime(filePath)


def scanAndRemoveDir(dir):
    cssN = 0
    d1 = datetime.datetime(2018, 4, 14, 9, 00, 00)
    for (root, dirs, files) in os.walk(dir):
        for file in files:
            filepath = os.path.join(root, file)
            (shotname, extension) = os.path.splitext(file)
            print("extension: ", extension)
            print("file path: ", file)

            if extension == '.scc':
                cssN += 1
                os.remove(filepath)
                print("remove file: ", file)

    # print("delete *.css file in total: ", cssN)
    print("file amount in total: ", cssN)

def recentModify(dir, recent):
    for (root, dirs, files) in os.walk(dir):
        for file in files:
            filepath = os.path.join(root, file)
            (shotname, extension) = os.path.splitext(file)

            # if extension == '.java':
            #     checkModify(filepath, recent)
            # if dir.endswith(dir, "/conf"):
            checkModify(filepath, recent)


def checkModify(filepath, recent):
    modify = TimeStampToTime(get_FileModifyTime(filepath))
    # print("modify: ", modify)
    modify1 = strToDateTime(modify, "%Y-%m-%d %H:%M:%S")
    # print("modify1: ", modify1)
    if (modify1 > recent):
        print("====recent modify file: ", filepath)


if __name__ == '__main__':
    # dir = "E:/xxxxx/coding/renda/importer/src"
    # postfix = ".scc"
    # scanAndRemoveDir(dir)

    # d1 = datetime.datetime(2018,4,14,9,00,00)
    # d2 = datetime.datetime(2018,4,14,9,10,00)
    # t = (d2-d1).total_seconds();
    # print("t: ", t)
    # print("d1: ", d1)

    # d1 = datetime.datetime(2018, 4, 14, 9, 00, 00)
    # modify = "2018-04-19 16:13:15"
    # modify1 = datetime.datetime.strptime(modify, "%Y-%m-%d %H:%M:%S")
    # print("modify1: ", modify1)
    # if(modify1 > d1):
    #     t = (modify1 - d1).total_seconds();
    #     print("t: ", t)

    recent = datetime.datetime(2018, 4, 14, 11, 00, 00)
    #dir_src = "E:/xxxxx/coding/newbag/importer/project/src/com"
    dir_conf = "E:/xxxxx/coding/newbag/importer/project/conf"
    #recentModify(dir_src, recent)
    recentModify(dir_conf, recent)

