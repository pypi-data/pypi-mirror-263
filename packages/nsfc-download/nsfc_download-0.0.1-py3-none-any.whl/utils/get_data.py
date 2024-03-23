
import requests
requests.packages.urllib3.disable_warnings()
class NSFC:
    def __init__(self, id:str):
        self.id = id
        self.index = 1
        self.finish = False
        self.projectName = "error"
        self.get_conclusion_info()
        self.pathlists = []
    def get_conclusion_info(self):
        url = f"https://kd.nsfc.cn/api/baseQuery/conclusionProjectInfo/{self.id}"
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Authorization': 'Bearer undefined',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Origin': 'https://kd.nsfc.cn',
            'Pragma': 'no-cache',
            'Referer': f'https://kd.nsfc.cn/finalDetails?id={self.id}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        response = requests.post(url, headers=headers, verify=False)
        if response.status_code == 200:
            result = response.json()
            if result['code'] == 200:
                projectName = result['data']['projectName']
                self.projectName = projectName
                print(f"项目名称：{projectName}")

    def get_file_url(self, index=1):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Authorization': 'Bearer undefined',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Origin': 'https://kd.nsfc.cn',
            'Pragma': 'no-cache',
            'Referer': f'https://kd.nsfc.cn/finalDetails?id={self.id}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        data = {
            'id': self.id,
            'index': index,
        }
        response = requests.post('https://kd.nsfc.cn/api/baseQuery/completeProjectReport', headers=headers, data=data, verify=False)
        # print(response.text)
        return response.json() # {'code': 200, 'message': None, 'data': {'hasnext': None, 'url': '/report/31/4a380ef04f0419134dfbf132cefe6c69'}}
    def get_file_img(self, url=None):
        url = f"https://kd.nsfc.cn{url}"
        headers = {
            'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'kd.nsfc.cn',
            'Pragma': 'no-cache',
            'Referer': f'https://kd.nsfc.cn/finalDetails?id={id}',
            'Sec-Fetch-Dest': 'image',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows'
        }
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 404:
            # print("图片不存在")
            return False
        return response.content
    def download(self):
        print("开始下载")
        res = self.get_file_url()
        url = res['data']['url']
        print(f"正在下载第{self.index}张图片")
        while not self.finish:
            self.index += 1
            img = self.get_file_img(url)
            if not img:
                self.finish = True
                break
            if img:
                # with open(f"img/{url.split('/')[-1]}.png", "wb") as f:
                #     f.write(img)
                tmp_imgpath = f"{self.projectName}/{self.index - 1}.png"
                try:
                    with open(tmp_imgpath, "wb") as f:
                        f.write(img)
                    self.pathlists.append(tmp_imgpath)
                except Exception as e:
                    print(e)
            res = self.get_file_url(self.index)
            url = res['data']['url']
            print(f"正在下载第{self.index}张图片")
        return self.pathlists
if __name__ == '__main__':
    id = '709232d7be43f7cad6fba63a5fb38b63'
    nsfc = NSFC(id)
    nsfc.download()