# _*_coding:utf8_*_
import os

BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Params = {
    "server": "127.0.0.1",
    "port": 8000,
    'request_timeout': 30,
    "urls": {
        "asset_report_with_no_id": "/asset/report/asset_with_no_asset_id/",  # 新资产待批准区
        "asset_report": "/asset/report/",  # 正式资产表接口
    },
    'asset_id': ('%s/var/.asset_id' % BaseDir).replace('/', os.sep),  # 服务端存储的记录ID，用于更新
    'log_file': ('%s/logs/run_log' % BaseDir).replace('/', os.sep),

    'auth': {
        'user': 'root',
        'token': 'random_str'
    },
}
