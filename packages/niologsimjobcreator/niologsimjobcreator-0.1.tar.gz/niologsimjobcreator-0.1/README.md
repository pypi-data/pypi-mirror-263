# 创建任务模板
---
## 参数介绍
- **表1 - 创建任务参数**

| 参数 | 说明 | 类型 | 需要 | 取值 |
| :-----: | :----: | :----: | :-----: | :----: |
| **name** | 用户自定义版本和任务的基准名称，最终的名称为该名称和时间戳的拼接 | string | 是 | 非空 |
| **sim_mode** | 仿真模式 | string | 是 | ["perception_only", "logsim", "e2e_logsim"] |
| **is_conan** | 是否使用Conan | bool | 是 |  |
| **app_version** | app版本 | string | 是 | 非空 |
| **author** | 创建人 | string | 是 | 非空 |
| **scenario_type** | 场景库数据类型 | string | 是 | ["roadtest", "dlb", "proto", "data_collection"] |
| **scene_from** | 数据来源场景库/Issue测试集 | string | 是 | ["scenario", "issue"] |
| **scene_name/scene_id** | 场景名称/ID | set< string > | 二选一 | 非空 |
| **module_type** | 模块类型 | string | 是 | ["主动安全", "NP", "NOP+", "NOP+MAP", "SAPA", "PSP"] |
| **priority** | 任务优先级 | string | 是 | ["HIGH", "MID", "LOW"] |
| reproduce | 是否为复现任务 | bool | 否 | 默认false |
| is_coapp | 是否为伴生数据 | bool | 否 | 默认false |
| evaluate_raw_data | 是否进行原始数据评测 | bool | 否 | 默认false |
| use_ground_truth | 是否采用gt | bool | 否 | 默认false |
| use_auto_triage | 是否触发 auto triage | bool | 否 | 默认false |
| pnc_aggregation | 开转闭报告聚合 | bool | 否 | 默认false |
| generate_hdmap_mode_gt_data_flag | 是否为复现任务 | bool | 否 | 默认false |
| auto_coapp | 自动伴生域/功能域数据判断 | bool | 否 | 默认false |
| extra_run4dgt | 额外执行4dgt仿真 | bool | 否 | 默认false |
| perception_stage | 感知参数，内容见表2 | json | 否 | "perception_only"和"e2e_logsim"模式下必须提供 |
| logsim_stage | logsim参数，内容见表3 | json | 否 | "logsim"和"e2e_logsim"模式下必须提供 |

- **表2 - 感知阶段参数**
  
| 参数 | 说明 | 类型 | 需要 | 取值 |
| :-----: | :----: | :----: | :-----: | :----: |
| **link** | 感知链路 | string | 是 | ["通用感知ArgApp", "通用感知ArgApp（感知+地图定位）", "通用处理Argusppl", "通用感知Argapp (nn + post +ehy)", "通用感知ArgApp_常驻服务版——王飞测试中", "通用处理Argapp（rel_loc+arg_app）", "MapLocApp ArgApp", "PSP二阶段", "纯感知", "自定义"] （注意空格） |
| workflow_id | workflow ID | string | 否 | link为"自定义"时必须提供非空id |
| refresh_perception | 强制刷感知 | bool | 否 | 默认false |
| perception_real_version | 感知版本 | string | 否 |  |
| perception_extra_config | 感知额外参数 | json | 否 |  |

- **表3 - logsim阶段参数**
  
| 参数 | 说明 | 类型 | 需要 | 取值 |
| :-----: | :----: | :----: | :-----: | :----: |
| **link** | logsim链路 | string | 是 | ["通用处理 Logsim", "通用处理 Logsim（老链路）", "通用处理 Logsim（WARROOM专属-常驻版）", "通用处理 Logsim（WARROOM专属-老链路）", "后接管仿真", "LogsimMR 流水线", "Logsim PNC MR 流水线", "规控训练数据链路", "规划模型数据导出链路", "logsim  celery链路", "Logsim GPU链路", "自定义"] |
| **evaluate_params** | 评测项 | set< string > | 是 | 非空 |
| workflow_id | workflow ID | string | 否 | link为"自定义"时必须提供非空id |
| pnc_consistence | 是否验证PNC一致性 | bool | 否 | 默认false |
| consistence_times | 验证次数 | int | 否 | 验证PNC一致性时必须提供，非负整数 |
| evaluation_real_version | 评测版本 | string | 否 |  |
| new_evaluation_real_version | 新评测版本 | string | 否 |  |
| logsim_real_version | Logsim 版本 | string | 否 |  |
| logsim_extra_config | Logsim 额外参数 | json | 否 |  |
| adviz_extra_config | Adviz 额外参数 | json | 否 |  |
## 创建任务
> 展示
1. 在主程序中初始化任务对象(参数“dev”, "prod"指定不同环境)，并设置要创建任务的各参数
![alt text](image-3.png)
    
2. 执行main.py主程序。查看运行结果，返回版本和任务的id以及任务的链接
![alt text](image-1.png)

1. 打开链接，在平台查看新建的任务
![alt text](image-2.png)

## 任务相关查询
1. **查询任务状态**
- 方法: find_job_status( job_id: str ) -> str
- 参数: 任务id
- 返回值: 
  - FINISH（任务执行完成）
  - RUNNING（任务执行中）
  - DOCKER_BUILDING: ... (镜像构建中)
  - FAIL: ... (任务失败)

2. **查询任务进度**
- 方法: find_job_process( job_id: str ) -> float
- 参数: 任务id
- 返回值: 任务进度比值

3. **任务case状态统计**
- 方法: find_case_status( job_id: str ) -> dict
- 参数: 任务id
- 输出: 任务的case各状态统计