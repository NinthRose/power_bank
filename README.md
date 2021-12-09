# power_bank

项目太小，所需存储和查询的数据量很小，感觉没必要用数据库，直接把数据库干掉了。

采用json快照落盘方式存储，只追加，不更改，防止数据丢失。

start:

- `cd power_web`    // 前端vue框架
- `npm install`     // 前端依赖
- `npm run build`   // 前端打包
- `cd -`            
- `python manage.py runserver 127.0.0.1:8001`     // 8001端口启动服务，如果上服务器，ip改为0.0.0.0，外部可访问


debug:

- `cd power_web`
- `npm run dev`      // 调试前端，端口不一致，路由不过去，需要自行测试
