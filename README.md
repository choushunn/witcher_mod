# 巫师三 Mod 批量下载爬虫

这是一个使用 Scrapy 爬虫框架编写的 Python 程序，用于批量下载巫师三游戏的 Mod。该程序可以自动从 Nexus Mods 网站上获取 Mod 的下载链接，并下载 Mod 到本地。

## 安装

1. 克隆本仓库到本地：

   `````
   git clone https://github.com/choushunn/witcher_mod.git
   ```

2. 进入项目目录：

   ````
   cd witcher_mod
   ````

3. 安装程序依赖：

   ````
   pip install -r requirements.txt
   ````

## 使用方法

1. 打开 `settings.py` 文件，并修改以下配置项：

   ````
   GAME_NAME = 'The Witcher 3'
   GAME_NEXUS_ID = 952  # 巫师三在 Nexus Mods 网站上的 ID
   DOWNLOAD_DIR = '/path/to/download/directory'  # 下载目录
   CONCURRENT_REQUESTS = 16  # 并发请求数量
   ````

2. 运行程序：

   ````
   scrapy crawl nexus_mods
   ````

3. 程序会自动爬取 Nexus Mods 网站上的 Mod 信息，并下载到指定的下载目录中。

## 注意事项

- 如果需要登录 Nexus Mods 网站才能下载某些 Mod，你需要在 `settings.py` 中配置你的登录信息。
- 请尊重 Mod 制作者的版权，不要将下载的 Mod 用于商业用途或未经授权的任何用途。
- 使用本程序下载 Mod 的风险由用户自行承担，作者不对因使用本程序而导致的任何后果负责。

## 贡献

如果你有任何建议或发现了 Bug，欢迎提出问题或创建 Pull Request。
