# Sanic Server
  
## 设计与依赖说明  
1. 服务体系 -- 基于sanic 22.3.x 以上版本的http/websocket服务框架  
2. python环境 -- 基于3.9的async/await原生异步模型  
3. ORM -- 采用tortoise-orm -- 0.19.1 以上的异步ORM数据模型  
4. 数据库连接驱动 -- 建议MySQL/mariaDB采用aiomysql, postgresql采用asyncpg  
5. 数据迁移工具 -- 使用aerich作为基本的数据迁移工具  
6. 缓存 -- 采用redis作为公有化基础缓存，版本建议 6.x以上  
7. 缓存驱动 -- 官方redis驱动支持，采用连接池模式  
  
## 项目说明  
参照项目目录  
common          -- 公共部分放置目录  
    -- func -- 公共处理方法/函数  
    -- libs     -- 公共库存放位置(不可直接使用\指定继承使用的类或第三方库)  
    -- model_db -- 公共数据模型(公共模型必须指定 abstract = True 以及必要的统一化表名)  
    -- model_rc -- 公共缓存模型  
    -- partner  -- 公共工具或通用的函数(通用的可直接调用的类/方法/函数)  
logs        -- 运行日志存放目录，按服务区分，服务停止情况下，删除后会自动生成  
migrations      -- 数据迁移目录，该目录下的数据一般情况不要删除或手动修改，否则会造成数据模型迁移的问题
test            -- 自测试或脚本运行目录  
非指定的其余目录皆为实际服务目录，以manage_system目录为例：  
    -- config               -- 该服务的配置存放位置  
    -- db_model             -- 该服务的数据模型存放位置  
    -- interface            -- 该服务的接口逻辑存放位置  
    -- rc_model             -- 该服务的缓存模型存放位置  
    -- script               -- 该服务的定时脚本、配置脚本、自定义脚本等的存放位置  
    -- api_base.py          -- 该服务的基础接口授权相关内容  
    -- uri_router.py/api_main.py        -- 该服务的接口路由入口  
-- http_manage_sys.py   -- 服务的启动文件
在项目根目录下 http_XXX.py   -- 可运行服务  以http_加服务名  


## 添加新的可启动的服务  
比如 参照示例，开启一个新的服务 manage_system:  
1. 以服务名称为包名，在根目录下创建服务包目录：manage_system  
2. 在服务包目录下创建配置文件目录: config  
    -- 在config目录下创建对应的服务配置conf_manage_sys.py -- SysConf的配置类, 并继承自BaseConf基础配置类  
    -- 至少需要重写基础配置中 SERVER_NAME(服务名称)、SERVER_ID(服务ID)、RUN_PORT(运行端口) 这三项属性，用于区分以及可并存的服务，其余属性可按需求重写  
    -- 将写好的配置类默认初始化到config.py的__init__.py中，并将数据库配置采用单独变量赋值，以便于aerich迁移工具使用  
sys_db = sys_conf.db_conf  
    -- 数据库或redis缓存重写配置的话必须至少要包含'default'配置  
3. 在服务包目录下创建数据模型目录(如果有使用数据库): db_model  
    -- 如果在配置里单独指定了数据模型文件，请在对应的创建数据模型文件，否则必须指定main.py和others.py至少两个模型文件  
4. 在服务包目录下创建缓存模型目录(如果有使用到缓存): rc_model  
5. 在服务包目录下创建基础接口服务文件(针对于非单例接口模型): api_base.py, 用于写当前服务下的接口公共部分的内容  
6. 在服务包目录下创建基于蓝图的路由入口文件(针对于非单例接口模型): uri_router.py, 用于汇总当前服务下的所有接口路由  
7. 针对于单例接口模型(例如guidance_ws), 直接在服务包目录下创建api_main.py的路由入口文件  
8. 在服务包目录下创建接口逻辑业务目录: interface, 用于写接口，写完接口后需要在uri_router.py里定义路由入口  
9. 如有需要写定时脚本、配置脚本、自定义脚本等，请在服务包目录下创建目录: script, 用于存放这类脚本  
10. 在根目录下创建对应的 http_manage_system.py 的可启动的服务文件  
    -- 注册配置
    -- 注册数据库
    -- 将服务包目录下的uri_router.py里的蓝图服务类注册到根路径的可启动文件里: main_app.blueprint(ManageSystem(version=sys_conf.VER_CODE).obj)  
    -- 注册中间件
    -- 注册异常捕获器
  
## 开发规范说明  
1. 配置类型文件统一放置在config/ 目录下，非共有配置请配置到服务对应的配置文件里或增加服务对应的目录  
2. 定时脚本任务统一放置到script目录，非共有定时脚本请在该目录下建立相应的服务名目录，然后在该目录下创建任务脚本  
3. 公用内容请放置到根目录下的common内，并按照上述列的目录要求存放  
4. ORM model模型根据服务名(对应配置里的SERVER_NAME)放到db_model下对应的服务名目录中，如果该模型在该服务下需要数据迁移，请将文件类添加到配置里的MODEL_LIST配置里  
5. 分模块式api统一写到interface下，uri_router.py文件定义基础路由，对应服务名的目录下写API接口，并按照示例方式注册基础路由:  
('/test', TestHandler.as_view(), '1.00.02') 对应 (路由映射，视图(API)处理函数，接口版本(可选))  
6. 所有枚举类型继承自BaseEnum, 并按照对应的格式定义枚举  
7. 所有的视图(API)处理函数需要继承自api_base.py中定义的基础类或其子类，数据类型响应统一调用answer_json响应数据模型，分页统一采用answer_page响应数据  
8. 所有的测试脚本、一次性使用脚本或可复用脚本统一放置在test目录下，测试脚本请用test_xxx命名，一次性使用script_xxx命名，可复用执行的脚本采用rescript_XXX命名  
9. 根目录下纯http(s)的服务请用http_xxx命名，websocket服务请用ws_xxx命名，融合类型的服务(既有http，也有websocket)请用server_xxx命名，非对外提供接口类型的服务请使用service_xxx命名  
10. 数据表命名规则须按照 统一服务标识_表类型(有类型标注)_表功能 命名，比如，管理服务表统一标识sys  
账户表命名：sys_account  账户登录记录表命名：sys_records_login  
11. 非记录类型的表，建议多使用缓存，减少外键关联  
12. 缓存key命名规则同数据表命名一致，建议单表数据模型使用数据表的表名  
比如管理账户表 sys_account 对应缓存KEY sys_account  
13. 接口开发规范 通常情况下，新增数据或提交验证采用post 常规查询或获取数据采用get 提交数据更新采用put  
14. 在项目中对于文件的读写，应使用相对路径，须避免使用绝对路径  
15. 日志统一采用MultLogger模式，在接口中通过self.log.info('xxxxx')或self.failed('xxxx')调用，或者在MultLogger中自定义文件名输出，添加方式参照info 和 failed  
  
## 关于数据迁移  
数据迁移工具采用与tortoise-orm配套的aerich迁移工具  
1. 在db_model下对应的服务目录下定义好数据模型  
manage_system/sys_account.py --> class SysAccount(Model):
2. 将数据模型所在的文件名添加到配置下的 MODEL_LIST内  
MODEL_LIST = ['main', 'records']  
3. 将数据库配置单独初始化到config/\_\_init__.py内(已添加过的忽略这一步)  
sys_db = sys_conf.db_migration(db_migration对应当前项目可迁移的库模型)  
3. 进入项目根目录，执行 aerich init -t 服务包目录名.config.sys_db(对应在__init__.py中的名称)  初始化数据库连接  更换服务数据库需要从该步骤重新开始执行，在同一数据库服务下，更新或回退，只参照5、6、7步骤  
4. 再执行  aerich init-db  初始化数据库  (首次迁移需要执行这一步，非首次迁移不需要这一步)
5. aerich migrate  生成迁移数据  
6. aerich upgrade  发起迁移  
7. 如有需求需要回退上一个版本执行  aerich downgrade  
  
## 关于服务部署  
目前采用service的方式启停服务，具体的服务配置文件参照项目目录的【服务配置】目录下的文件： 
>采用root账户运行：   
1. 服务名称是定义的文件名，具体指定的运行账户和虚拟环境路径和启动文件路径需要在文件里进行替换  
2. 然后将配置好的服务文件移到 /etc/systemd/system/ 目录下  
3. 执行service 服务名 status/start/stop/restart  操作项目的启停和状态查看  
>采用一般账户运行：  
1. 将服务配置】目录下配置文件内的账户指定注释掉，然后替换虚拟环境路径和启动文件路径  
2. 在用户目录的.config(隐藏目录, 没有则需要手动创建)下创建systemd/user/目录层级  
3. 将修改好的服务配置文件拷贝到账户目录：~/.config/systemd/user/ 目录下  
4. 采用 systemctl --user status/start/stop/restart 服务名 操作服务
