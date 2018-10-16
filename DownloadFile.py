#! python3
# coding=utf-8
__author__ = 'Duke'

import requests
import sys
import os
import shutil

download_list = [
    {'name': '我不难过-孙燕姿.mp3','url': 'http://m8.music.126.net/20180930115348/6574bad1c5ca5cdad8fb4628773b4155/ymusic/fd1f/92fe/a39f/3fdaf54247d516db3713721f5f31c90d.mp3'},
    {'name': '天黑黑-孙燕姿.mp3', 'url': 'http://m8.music.126.net/20180930115649/6cb4085a638b792d07ec92f73623cf2a/ymusic/f1ca/b3c3/fc30/0b2607fa67337b3094e2e40c280a3f32.mp3'},
    {'name': '开始懂了-孙燕姿.mp3', 'url': 'http://m7.music.126.net/20180930151322/474ffb9516fd1b41df6df29ddbfcd264/ymusic/4f58/468c/dd59/99d8ea6ff1a4f3f90f29d20756bd2f30.mp3'},
    {'name': '我怀念的-孙燕姿.mp3', 'url': 'http://m8.music.126.net/20180930115825/8d58642792632de0dd5357d786834c40/ymusic/a3e6/5dd9/bd97/2efb6c4577cedc89b34d0c086e2cc335.mp3'},
    {'name': '遇见-孙燕姿.mp3', 'url': 'http://m7.music.126.net/20180930151410/28226a7512c54a2b101bcc948e32e57a/ymusic/7c93/5d46/9f82/d9a801a4b57d25e6dd58171a33aaf961.mp3'},
    {'name': '阴天-莫文蔚.mp3', 'url': 'http://m8.music.126.net/20180930151441/821ba2fad5e25efb3f55be78f3d67f9f/ymusic/5f85/6204/e7dd/db0a3e79d134101a577c1329845c5055.mp3'},
    {'name': '忽然之间-莫文蔚.mp3', 'url': 'http://m8.music.126.net/20180930151721/c3e19ddb3ed2d9e787ae5ff3e4c3a81b/ymusic/4d9b/c650/4133/73b6c1f02c5a0dd72edbfedbe24b17f0.mp3'},
    {'name': '红色高跟鞋-蔡健雅.mp3', 'url': 'http://m8.music.126.net/20180930120641/9779ab9a87e5fa9bf575ef8ee724d61f/ymusic/a391/279d/1655/ebc8f929b98e7b29f9e5adc0a31df24f.mp3'},
    {'name': '后会无期-G.E.M.邓紫棋.mp3', 'url': 'http://m8.music.126.net/20180930151748/8e8d7a63f8a85f35103d86bd4297d0dc/ymusic/2c87/6ec3/582e/0d572dcc04f8de34133c0f364b74c30c.mp3'},
    {'name': '泡沫-G.E.M.邓紫棋.mp3', 'url': 'http://m8.music.126.net/20180930121312/36ec49529ff6e1ce9f1a4446974618de/ymusic/de6d/c62c/57a5/785aa8b8ca71546f97b3171c5375f1c2.mp3'},
    {'name': '当你老了 (Live)-李健.mp3', 'url': 'http://m8.music.126.net/20180930121342/8423b55ed467c59a213192789b68eecd/ymusic/0b8c/4ea6/c957/ddf46174d597d368111db3ff9fbdaa7a.mp3'},
    {'name': '袖手旁观 (Live)-李健.mp3', 'url': 'http://m8.music.126.net/20180930121412/e3f863ff190a1df9c8ac1dcad527fa43/ymusic/3e1b/42b3/ea73/76ffad762f710e4ad239fde578f01ec9.mp3'},
    {'name': '贝加尔湖畔-李健.mp3', 'url': 'http://m8.music.126.net/20180930151818/e33a56102a978cb6625392ee898f3852/ymusic/b578/4360/fecf/f71ec9f18617ba142eb7ef8afabbe216.mp3'},
    {'name': '假如爱有天意 (Live)-李健.mp3', 'url': 'http://m8.music.126.net/20180930121533/74e30cd0494b822003d62b2c969405b9/ymusic/dd6a/2c4b/bd1f/c0b0e36bef35416013cdefa878b90bd2.mp3'},
    {'name': '天空-王菲.mp3', 'url': 'http://m8.music.126.net/20180930121559/8871f9222bee8859a11e741111828c8d/ymusic/6302/8ee0/f367/57b293716e90a9344eeb6ee4b1ff35ca.mp3'},
    {'name': '闷-王菲.mp3', 'url': 'http://m8.music.126.net/20180930121625/ee9ba03fa1a79abdec161a118bf86ac1/ymusic/3409/1232/1df9/4ada90b37ae84024a5f74a552f77187f.mp3'},
    {'name': '我愿意-王菲.mp3', 'url': 'http://m8.music.126.net/20180930151857/802a7a5677ded0bee1dd348c37719e89/ymusic/2eb8/c87c/dd48/e30e5c323d53066e911b050dc6e7d2ec.mp3'},
    {'name': '容易受伤的女人(粤)-王菲.mp3', 'url': 'http://m7.music.126.net/20180930151926/106c70045a800fb6aead99f5e9232fbd/ymusic/58ce/57c1/cf59/66aebd9bb0e7fe44b4b59d097877af0a.mp3'},
    {'name': '水调歌头-王菲.mp3', 'url': 'http://m8.music.126.net/20180930121756/133c72885076fcc19499950a6056bf08/ymusic/61a3/e1a0/025c/1e224a5abf87d86b08d76103a98df1eb.mp3'},
    {'name': '人间-王菲.mp3', 'url': 'http://m8.music.126.net/20180930121819/004f176f8a6b0b8b45991944c78e5cb9/ymusic/9399/08cd/a6f4/3248954dbb7caf8738f1d929a37c63d9.mp3'},
    {'name': '红豆-王菲.mp3', 'url': 'http://m7.music.126.net/20180930151954/71bff9abe79b89a4a66d9efc36c8223a/ymusic/ecad/bbc2/60e9/437cc994efc2efbaae2935556bcf941d.mp3'},
    {'name': '因为爱情-陈奕迅.mp3', 'url': 'http://m8.music.126.net/20180930121910/9b9d4f8dcf2bcbc4df12c693d21fb7f8/ymusic/61f8/acca/ae45/098caa71f39e824afb2e899e39d5c4eb.mp3'},
    {'name': '浮夸-陈奕迅.mp3', 'url': 'http://m8.music.126.net/20180930152022/e8875a3e87d4f168405a63b2a50fe3f9/ymusic/920a/4ef8/2d50/ba54d5a60f396d703749dbffdff2b48c.mp3'},
    {'name': '好久不见-陈奕迅.mp3', 'url': 'http://m8.music.126.net/20180930122004/c9a35b765b6900faeb29823ebbae13d4/ymusic/d8ce/08c3/986c/844405c5672efe9b10076bab25d7bce2.mp3'},
    {'name': '夜太黑-林忆莲.mp3', 'url': 'http://m7.music.126.net/20180930152055/b7e54c2bf8fb5c3280264ddf5e457e69/ymusic/47a2/d48a/9a2e/5dafdcc970b065d4efed1ce99f4bc814.mp3'},
    {'name': '远走高飞-林忆莲.mp3', 'url': 'http://m7.music.126.net/20180930152118/7778d232f8b65472324a94061f203b81/ymusic/05b8/ddbe/0a20/849456e72bcc54dd5af855a469599635.mp3'},
    {'name': '听说爱情回来过-林忆莲.mp3', 'url': 'http://101.110.118.69/m7.music.126.net/20180930144553/758fb5a099b698ed768ceda866b0a464/ymusic/3c30/9d16/10ca/7ab56e59edd9f5bef3ecff309a092bbc.mp3'},
    {'name': '再见悲哀-林忆莲.mp3', 'url': 'http://m8.music.126.net/20180930144623/1c3604e4beee0f6413d8f3c7b51e0060/ymusic/a59b/d2df/a48b/73a9c6315d5bbdbabb764f14dcad9eb4.mp3'},
    {'name': '问-林忆莲.mp3', 'url': 'http://m8.music.126.net/20180930144648/fa319758b5073177f94d3811c31a9613/ymusic/3c62/23e2/8bfe/234c5995d9a04e7d5d1b0a3f3cd81f9f.mp3'},
    {'name': '伤痕-林忆莲.mp3', 'url': 'http://m8.music.126.net/20180930144717/79ab4d894abcd158dfb0cdf1da493721/ymusic/9db1/5759/6ca0/f44fff43b1640136ff4b105e335f4937.mp3'},
    {'name': '为你我受冷风吹 (Live)-林忆莲.mp3', 'url': 'http://m7.music.126.net/20180930144741/dbd9dad027ade5198feeb49a66ef521a/ymusic/b354/8e5d/6c7b/31ac06b79f2eba3ac6ca03d61f7478f7.mp3'},
    {'name': '记得-张惠妹.mp3', 'url': 'http://m8.music.126.net/20180930144808/0290204371068610e90647ede0e5b7b9/ymusic/4219/ae15/11c7/5653a449f6e363330bac7afdc1e2b2f7.mp3'},
    {'name': '解脱-张惠妹.mp3', 'url': 'http://m7.music.126.net/20180930144833/c2d1afb0afa24d7a66268d400674026b/ymusic/c651/e4b2/4cff/d77f6b1097bc6156824f8abd77ce7338.mp3'},
    {'name': '趁早-张惠妹.mp3', 'url': 'http://m7.music.126.net/20180930144857/23162dd341c6852453a65f387f142d73/ymusic/cbad/e1e1/7f75/08d0a1e373b9fab11a3e988083841f8c.mp3'},
    {'name': '我最亲爱的-张惠妹.mp3', 'url': 'http://m8.music.126.net/20180930144926/b3fb72f18ce7bfdf1816f109dff09f44/ymusic/0523/76c2/2b74/9ee1009c4b6a6b058ff2b175841fd8ed.mp3'},
    {'name': '如果你也听说-张惠妹.mp3', 'url': 'http://101.110.118.69/m7.music.126.net/20180930144950/8318004334639069ce97516cb7950d52/ymusic/3bc6/4932/f33b/e360f921306a645af2a3f13905057845.mp3'},
    {'name': '听海-张惠妹.mp3', 'url': 'http://m8.music.126.net/20180930145014/661d7c0e649e7d82d1ec02eecedcc6e3/ymusic/2ed6/dbdd/97ae/dd9345a6d7320f7aefa2dc60301af89d.mp3'},
    {'name': '屋顶-温岚.mp3', 'url': 'http://101.110.118.70/m7.music.126.net/20180930145038/212cb9cc8c6262477231b59f1a022e7c/ymusic/d6d3/7aac/9aed/802e6b3a1bd34a18927f4adab563690a.mp3'},
    {'name': '讲你知-张学友.mp3', 'url': 'http://m8.music.126.net/20180930145103/f1497e2c1d6ace63b50f88d81470ffd3/ymusic/1ac9/8dac/cd33/3bc26d271864c8d35b8c1598a062a5cd.mp3'},
    {'name': '情已逝-张学友.mp3', 'url': 'http://m7.music.126.net/20180930145125/1aed80d6a97c4289328f7be8471bea94/ymusic/f41d/74a1/c439/98583e2734be428531a0259e3bf8241b.mp3'},
    {'name': '离开以后-张学友.mp3', 'url': 'http://m7.music.126.net/20180930145150/41f9b1b082d2cd6432afc84eeeb8571b/ymusic/5dac/29a8/8d1f/6761406dcfa2dbb075dc0161b2128fc2.mp3'},
    {'name': '我等到花儿也谢了-张学友.mp3', 'url': 'http://101.110.118.47/m7.music.126.net/20180930145225/2db894e6d723ecdd0a74d8452eda8260/ymusic/6db6/24ac/4022/200757f561eaad396025696504474575.mp3'},
    {'name': '等你等到我心痛-张学友.mp3', 'url': 'http://m7.music.126.net/20180930145255/bc659d904b7797f92bae93bbda14ef0f/ymusic/0728/dfa3/dcd3/9e66df76a49666e41e7a5807005bc329.mp3'},
    {'name': '一路上有你-张学友.mp3', 'url': 'http://101.110.118.68/m7.music.126.net/20180930145343/10b3a84ab1ff12bb62ea53a2aceb0d13/ymusic/fa08/8ea7/948e/4dfb9e415508ef5a91e9af9effc32cb0.mp3'},
    {'name': '心如刀割-张学友.mp3', 'url': 'http://101.110.118.47/m7.music.126.net/20180930145405/a9239902a809c085afe5b5258e322664/ymusic/1851/5a80/e129/ccf572c4e6ee32e98b588b1e32a6b1a3.mp3'},
    {'name': '你最珍贵-张学友.mp3', 'url': 'http://m7.music.126.net/20180930145428/b6d6d6026f3332794f8039f28d3d8ba6/ymusic/0cb2/f41a/ba05/adda2aecbac6f612b1c61b7a40ae0e2d.mp3'},
    {'name': '情书-张学友.mp3', 'url': 'http://m8.music.126.net/20180930145451/af001629c4fdc005727463cf5c6abb4c/ymusic/e8b0/4d43/9594/e02e7036c2d8c042aaee6e5dce5c1e7e.mp3'},
    {'name': '我真的受伤了-张学友.mp3', 'url': 'http://m8.music.126.net/20180930145515/dbd246a44e8470390ddbc8d194b1b7d9/ymusic/8c6b/017b/14b7/2423507154766281b7b2d3aab2649b7e.mp3'},
    {'name': '李香兰-张学友.mp3', 'url': 'http://m8.music.126.net/20180930145538/87ef46a3988ea021cc6fd66e5c170495/ymusic/ccb6/1165/25e9/6c606b0a888ba64700021cc777a26a02.mp3'},
    {'name': '如果这都不算爱-张学友.mp3', 'url': 'http://m7.music.126.net/20180930145601/8b700e66a090f69ba629f8ab1a86f0c8/ymusic/9b00/76e3/c1ff/e33288eba4579f9c62a71c1b4c863c56.mp3'},
    {'name': '秋意浓-张学友.mp3', 'url': 'http://m8.music.126.net/20180930145626/4cdd975de7a74ab79e93b30283febb4b/ymusic/b30c/8eca/48d8/abd890477134bc0e6df8d62a1867e5fb.mp3'},
    {'name': '她来听我的演唱会-张学友.mp3', 'url': 'http://m8.music.126.net/20180930145648/1f82230421c29abfa0d77bde7e64714f/ymusic/344b/c23a/71f9/5c29810e09d2978a0c61dac103b60f7d.mp3'},
    {'name': '慢慢-张学友.mp3', 'url': 'http://m8.music.126.net/20180930145711/309999d819218f6cf37df03b41e363f8/ymusic/b11e/3cf2/b54c/8d9642e82a3d710e534121530569f320.mp3'},
    {'name': '遥远的她-张学友.mp3', 'url': 'http://m7.music.126.net/20180930145743/6edf3397e25771976591d59605119e3e/ymusic/c91b/17f3/70b9/1d8753528eb5196aa11de679df618cc7.mp3'},
    {'name': '白月光-张信哲.mp3', 'url': 'http://m8.music.126.net/20180930145808/a38cc9250169083a0f7f5994f0840954/ymusic/2f83/249c/172a/cc2bf14b621aca436014bf0551fb140e.mp3'},
    {'name': 'Five Hundred Miles.mp3', 'url': 'http://m7.music.126.net/20180930150003/ab2eed6b6298fd15e686371b261fef7d/ymusic/45e8/01d8/d032/4a0c99e016aa019b04b442907e60bd94.mp3'},
    {'name': '新鸳鸯蝴蝶梦.mp3', 'url': 'http://m8.music.126.net/20180930150300/71bf63f3e5858c7529d6e190ecc8a326/ymusic/106f/ea14/3ea6/4525484172e5d3dc660e9db7229bab99.mp3'},
    {'name': '其实都没有-杨宗纬.mp3', 'url': 'http://101.110.118.47/m7.music.126.net/20180930150334/d71c1dbb0790602e66dde87c8db109e3/ymusic/a07b/c7bf/80af/df75f4a43cad43fd890bddfa7828e886.mp3'},
    {'name': '晚睡早起-谢安琪.mp3', 'url': 'http://m7.music.126.net/20180930150410/372dafe123f8f6a6f29186fd52dba012/ymusic/d343/cea7/aa9d/fa6bc37280f868c52a4b58dfa0420d04.mp3'},
    {'name': '潇洒走一回-叶蒨文.mp3', 'url': 'http://m7.music.126.net/20180930150626/e05a338ed689bb12b83c102793f87cc6/ymusic/6f10/0496/93a5/076897ec4fb8550f244ed63e5d80c974.mp3'},
    {'name': '偏偏喜欢你-陈百强.mp3', 'url': 'http://m7.music.126.net/20180930150732/6db2c5af52de8478a63ba399a260ebc0/ymusic/6411/1b1e/507b/8a9523b3b66250160025eb4ae7a3c361.mp3'},
    # {'name': '.mp3', 'url': ''},

]

FOLDER_NAME = "Music"


def downloadFile(file_name, url):
    if 0 == len(file_name):
        return

    targetFile = "./%s/%s" % (FOLDER_NAME, file_name)
    with open(targetFile, "wb") as f:
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()
        print("\n")


def main():
    if os.path.exists(FOLDER_NAME):
        shutil.rmtree(FOLDER_NAME)
    os.makedirs(FOLDER_NAME)

    listSize = len(download_list)
    for i in range(listSize):
        print("Downloading %s  (%s)" % (download_list[i]['name'], ("%d/%d" % (i, listSize))))
        downloadFile(download_list[i]['name'], download_list[i]['url'])

    print("################\n"
          "#              #\n"
          "#  Completed!  #\n"
          "#              #\n"
          "################\n")

if __name__ == "__main__":
    main()
