# APP AUTO TEST

[![Join the chat at https://gitter.im/xiaocong/uiautomator](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/xiaocong/uiautomator?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

#### 环境搭建

    ```
    python 2.7
    pip install uiautomator
    pip install beautifulsoup4
    pip install lxml
    ```


### 接口

    * 更新HTML文件
        ```python
        python manage.py updatehtml /file/path/htmldir
        ```

    * 把HTML转换成XML
        ```python
        python manage.py htmltoxml /file/path/htmldir/html.json
        ```
