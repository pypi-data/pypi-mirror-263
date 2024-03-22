import asyncio
import os
import time

import boto3


class OssUtil:
    def __init__(self, region: str, access_key_id: str, access_key_secret: str, bucket_name: str, endpoint: str):
        self.region = region
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.bucket_name = bucket_name
        self.endpoint = endpoint

    async def _get_connect(self):
        try:
            return boto3.client('s3', region_name=self.region, aws_access_key_id=self.access_key_id, aws_secret_access_key=self.access_key_secret)
        except RuntimeError as e:
            raise '连接失败，请确认连接信息'

    async def _upload_file(self, src_local_path, dest_s3_path):
        """
        上传单个文件
        :param src_local_path:
        :param dest_s3_path:
        :return:
        """
        try:
            with open(src_local_path, 'rb') as f:
                conn = await OssUtil._get_connect(self)
                conn.upload_fileobj(f, self.bucket_name, dest_s3_path)
        except Exception as e:
            print(f'Upload data failed. | src: {src_local_path} | dest: {dest_s3_path} | Exception: {e}')
            return False
        print(f'Uploading file successful. | src: {src_local_path} | dest: {dest_s3_path}')
        return True


if __name__ == '__main__':
    oss = OssUtil(region="us-east-2", access_key_id="AKIAYAV7GTLTG5NPFAM2", access_key_secret="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", bucket_name="weee-qa", endpoint="https://weee-qa.s3.us-east-2.amazonaws.com/QA")
    print(os.getcwd())
    is_success = asyncio.run(OssUtil._upload_file(oss, "../1.png", 'test/' + str(int(time.time()))))
    print(is_success)
