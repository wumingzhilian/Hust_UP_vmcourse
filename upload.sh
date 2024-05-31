#!/bin/bash

# 设置 Docker Hub 用户名
USERNAME="wumingzhilian"

# 设置父目录，这里是 output 目录下的所有子目录
PARENT_DIR="./output"

# 遍历 output 目录中的每个子目录
for dir in $PARENT_DIR/*; do
    if [ -d "$dir" ]; then
        echo "Processing directory: $dir"
        cd "$dir"
        # 检查是否存在 docker-compose.yml 文件
        if [ -f "docker-compose.yml" ]; then
            # 使用 docker-compose 构建所有服务
            docker-compose build
            # 推送镜像到 Docker Hub
            docker-compose push
        else
            echo "No docker-compose.yml found in $dir"
        fi
        # 返回上一级目录
        cd - # 或者 cd $PARENT_DIR
    fi
done