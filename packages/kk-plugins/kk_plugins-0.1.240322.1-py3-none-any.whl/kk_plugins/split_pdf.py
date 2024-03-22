import json
import os

import pypdf
from lxml import etree
from pypdf import PdfWriter
from uuid import uuid1


class XmlJieXi:
    def __init__(self):
        self.last_name = ""
        self.last_page_start = 0

    def parse(self, xml_file):
        """
        输入xml文件，返回uuid
        uuid文件内容为json格式，key为文件名，value为起始页和结束页
        :param xml_file:
        :return:
        """
        tree = etree.parse(xml_file)
        root = tree.getroot()

        result_dict = {}

        for child in root:
            if child.tag == "ITEM":
                if self.last_name != "":
                    if result_dict.get(self.last_name) is None:
                        result_dict[self.last_name] = [self.last_page_start, child.attrib["PAGE"]]
                    else:
                        result_dict[self.last_name + str(uuid1())] = [self.last_page_start, child.attrib["PAGE"]]

                self.last_name = child.attrib["NAME"]
                self.last_page_start = child.attrib["PAGE"]
        result_dict[self.last_name] = [self.last_page_start, -1]
        uuid = str(uuid1())
        with open(uuid, 'a+', encoding='utf-8') as f:
            f.write(json.dumps(result_dict, ensure_ascii=False))

        return uuid


class PdfSplit:
    def __split(self, src: str, dst: str, split_range: list):
        if not os.path.exists(src):
            print("文件不存在")
            return
        dst_folder = os.path.dirname(dst)

        if not os.path.exists(dst_folder) and dst_folder != "":
            os.makedirs(dst_folder)

        pdf_reader = pypdf.PdfReader(src)

        pdf_writer = PdfWriter()
        # print(len(pdf_reader.pages))
        if split_range[1] == -1:
            split_range[1] = len(pdf_reader.pages)
        for i in range(int(split_range[0]), int(split_range[1])):
            # print(i)
            pdf_writer.add_page(pdf_reader.pages[i])

        if not dst.endswith(".pdf"):
            dst += ".pdf"

        with open(dst, 'wb') as out:
            pdf_writer.write(out)

    def split_by_xml(self, filename):
        if not filename.endswith(".xml"):
            filename += ".xml"
        result_dir = os.path.basename(filename)[:-4]
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)

        pdf_name = filename.replace(".xml", ".pdf")
        xml_jiexi = XmlJieXi()
        uuid = xml_jiexi.parse(filename)
        with open(uuid, 'r', encoding='utf-8') as f:
            result = f.read()
            result = json.loads(result)
            for key, value in result.items():
                self.__split(pdf_name, os.path.join(result_dir, key + ".pdf"), list(value))
        os.remove(uuid)


# p = PdfSplit()
# p.split_by_xml("xxx")
