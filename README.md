# 介绍

轻小说文库的第三方OPDS实现，基于PathagarBooks/pathagar

# 部署
```
git clone https://github.com/umauc/Wenku8OPDS.git
cd Wenku8OPDS
pip install -r requirements.txt
cp local_settings.example.py local_settings.py
nano local_settings.py # 更改配置
python manage.py migrate
python manage.py createsuperuser
python manage.py addbooks --json data.json
python manage.py runserver # 服务器将运行在http://localhost:8000/上
```

# 重新生成data.json

删除data.json后，执行``` python add.py ```即可（耗时约在20-30min，使用服务器生成的用户请screen）

# 使用项目：

https://github.com/PathagarBooks/pathagar
https://github.com/LanceLiang2018/Wenku8ToEpub-Online
https://github.com/962978926/wenku8_spider
https://github.com/mikulo/miku