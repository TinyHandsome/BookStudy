from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    # 设定工作的线程数：允许的最大值与要处理的数量之间的 最小值，以免创建多余的线程
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
        
    return len(list(res))

if __name__ == '__main__':
    main(download_many)