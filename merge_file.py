from hdfs.client import Client
def main():
    client = Client("http://192.168.204.132:50070/")
    lists = client.list(hdfs_path="/user/hadoop/input", status=True)
    files_name = []
    output_path = "/user/hadoop/output"
    write_files = "/user/hadoop/output/result.txt"
    for l in lists:
        files_name.append(l[0])
    #存储所有txt后缀的文件
    txt_file_lists = filter(files_name,"abc")
    #读取txt后缀的文件内容
    txt_buff = ""
    for name in txt_file_lists:
        with client.read("{}{}".format("/user/hadoop/input/",name), length=20, encoding='utf-8') as obj:
            for i in obj:
                txt_buff += i+"\n"
    #写入到hdfs中
    #路径，数据，编码
    # client.statue
    #如何文件已经存在 检查看看数据是否写入进去了
    for l in client.list(hdfs_path=output_path, status=True):
        full_path = "{}/{}".format(output_path,l[0])
        # print(full_path)
        # print(write_files)
        if full_path == write_files:#找到了这个文件
            print(f"文件存在：{full_path}")
            with client.read(write_files,length=300,encoding="utf-8") as obj:
                for i in obj:
                    print(i);
                return
    #如果文件不存在就写进去
    print(f"写入文件{write_files} 大小:{len(txt_buff)}")
    client.write(write_files, data=txt_buff, encoding='utf-8')

def filter(files_name,conditions):
    result_lists = []
    for name  in files_name:
        suffix_index = name.find(".")
        suffix = name[suffix_index+1:]
        # print(name,suffix)
        if suffix != conditions:
            # print(f"ADD {name} ")
            result_lists.append(name)

    return result_lists
if __name__ == '__main__':
     main()


#参考资料：https://www.cnblogs.com/harelion/p/5398146.html
