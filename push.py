#encoding:utf8
#python
__author__='xxxspy'
from sinastorage.bucket import SCSBucket
import sinastorage
import hashlib
import os
PATH_SPLITER='/'
def pathjoin(*args):
    return PATH_SPLITER.join(args).decode('gbk')
def splitpath(p):
    rp=[]
    ps=os.path.split(p)
    rp.insert(0,ps[-1])
    while ps[0]:
        ps=os.path.split(ps[0])
        rp.insert(0,ps[-1])
    return rp

def file_exist(bucket,filename):
    try:
        bucket[filename]
    except KeyError:
        return False
    return True

def push(dirname):
    '''
    把dirname文件夹下所有文件都以相同的结构同步到sae云存储中
    比如，在dirname下有如下文件：
        dirname/a/test.txt
        dirname/test.txt
    推送到sae的云存储中的文件结构就是：
        /a/test.txt
        /test.txt
    注意空文件夹不推送
    '''
    akey=os.environ['SAE_STORAGE_ACCESS_KEY']
    skey=os.environ['SAE_STORAGE_SECRET_KEY']
    bucketname=os.environ['SAE_BUCKET_NAME']
    sinastorage.setDefaultAppInfo(akey,skey)
    bucket=SCSBucket(bucketname,secure=False)
    fpaths=[]
    for root,dirs,files in os.walk(dirname):
        for f in files:
            local_fpath=os.path.join(root,f)
            ps=splitpath(root)
            ps[0]=''
            ps.append(f)
            fpath=pathjoin(*ps)
            print (fpath)
            fpaths.append(fpath)
            if not fpath.startswith(PATH_SPLITER):
                fpath =PATH_SPLITER+fpath
            if file_exist(bucket,fpath):
                meta=bucket.meta(fpath)
                sae_sha1=['Content-SHA1']
                fdata=open(local_fpath,'rb').read()
                if len(fdata)==0 and meta['Size']==0:
                    pass
                else:
                    sha1=hashlib.sha1()
                    sha1.update(fdata)
                    if sae_sha1 != sha1.hexdigest():
                        bucket.putFile(fpath,local_fpath)
            else:
                bucket.putFile(fpath,local_fpath)
    sae_files=bucket.listdir(prefix='')
    for f in sae_files:
        #f=(name, isPrefix, sha1, expiration_time, modify, owner, md5, content_type, size)
        if f[0] not in fpaths:
            print('del '+f[0])
            del bucket[f[0]]
        else:
            print('has ' +f[0])
