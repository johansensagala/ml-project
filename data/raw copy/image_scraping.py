import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

url = 'https://www.google.com/search?q=jatropha+curcas&tbm=isch&ved=2ahUKEwiBlZHTo9WCAxUMbGwGHfJ1CPsQ2-cCegQIABAA&oq=jatropha+curcas&gs_lcp=CgNpbWcQAzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABFCECFiECGC8CWgAcAB4AIABqwGIAfABkgEDMS4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=ZLtcZYHTJozYseMP8uuh2A8&bih=747&biw=1519&rlz=1C1ONGR_enID1019ID1019&hl=en-GB'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    img_elements = soup.find_all('img')

    save_dir = 'downloaded_images'
    os.makedirs(save_dir, exist_ok=True)

    for img in img_elements:
        img_url = urljoin(url, img['src'])
        img_data = requests.get(img_url).content

        img_name = os.path.join(save_dir, os.path.basename(img_url))

        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)

        print(f'Gambar {img_name} berhasil diunduh.')
else:
    print(f'Gagal melakukan permintaan. Kode Status: {response.status_code}')
