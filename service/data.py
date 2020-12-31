import os, zipfile


def get_file_list(path):
    if os.path.isdir(path):
        for item in os.listdir(path):
            p1 = os.path.join(path, item)
            if os.path.isdir(p1):
                size = "文件夹"
            else:
                size = str(os.path.getsize(p1))
            yield (item, size)


def get_zipfile_list(path):
    zf = zipfile.ZipFile(path)
    zfiles = zf.infolist()
    for f in zfiles:
        name = f.filename
        #  防止乱码
        name = name.encode("cp437").decode("gbk")
        size = str(f.file_size)
        yield (name, size)


def uncompress(spath, tpath):
    zf = zipfile.ZipFile(spath)
    zflist = zf.namelist()
    for name in zflist:

        # 避免中文乱码
        name1 = name.encode("cp437").decode("gbk")
        name1.replace("/", "\\")
        print(name1)
        fpath = os.path.join(tpath, name1)
        print(fpath)
        if fpath.endswith("\\"):
            os.mkdir(fpath)
        else:
            (basename, filename) = os.path.split(fpath)
            if not os.path.exists(basename):
                os.makedirs(basename)
            with open(fpath, "wb+") as f:
                f.write(zf.read(name))

        zf.close()


def compress(files, spath, tpath):
    print(files)
    print(spath)
    print(tpath)
    spath = spath + "\\"
    f = zipfile.ZipFile(tpath, "w", zipfile.ZIP_DEFLATED)
    for fpath in files:
        if os.path.isfile(fpath):
            relativepath = fpath.replace(spath, '')
            print(relativepath)
            f.write(fpath, relativepath)
        else:
            for dirpath, dirnames, filenames in os.walk(fpath):
                for filename in filenames:
                    fullpath = os.path.join(dirpath, filename)
                    relativepath = fullpath.replace(spath, '')
                    print(relativepath)
                    f.write(fullpath, relativepath)

    f.close()
