### Uploader all files in a folder to Aliyun OSS

Must load `OSS_ACCESS_KEY_ID` and `OSS_ACCESS_KEY_SECRET` into environment variables first.

## Install

`pip install oss2-uploader`

## Usage

only executable under `if __name__ == "__main__":`

```
if __name__ == "__main__":

    from oss2_uploader import folder_uploader

    folder_uploader(, , 
        folder_path="./test-folder,
        bucket_name="test-bucket",
        oss_endpoint="oss-ap-southeast-1.aliyuncs.com",
        oss_path="pathname",
    )
```

if `oss_path` is omitted, will use the folder name as prefix in oss