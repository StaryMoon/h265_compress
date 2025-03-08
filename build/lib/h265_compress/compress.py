#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path
import ffmpeg

def compress_video(source_dir, output_dir):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # 定义正则表达式以解析文件名
    pattern = re.compile(r'^(.+)_(\d+)x(\d+)_(\d+)\.yuv$')

    for filename in os.listdir(source_dir):
        if not filename.lower().endswith('.yuv'):
            continue

        match = pattern.match(filename)
        if not match:
            print(f"文件名不符合预期格式，跳过: {filename}")
            continue

        name, width, height, framerate = match.groups()
        resolution = f"{width}x{height}"

        # 计算码率：宽度 * 长度 * 帧率 * 0.01，再转换为千比特每秒（Kbps）
        bitrate_kbps = int(int(width) * int(height) * int(framerate) * 0.0144) // 1000

        input_path = os.path.join(source_dir, filename)
        output_filename = f"{name}_{resolution}_{framerate}.mp4"
        output_path = os.path.join(output_dir, output_filename)

        # 使用 ffmpeg-python 执行压缩
        try:
            print(f"正在处理文件: {filename}")

            ffmpeg.input(input_path, s=resolution, framerate=30, pix_fmt='yuv420p') \
                .output(output_path, vcodec='libx265', video_bitrate=bitrate_kbps, preset='placebo', tune='psnr', profile='main', level='16.2') \
                .run()

            print(f"成功压缩并保存为: {output_filename}\n")
        except Exception as e:
            print(f"处理文件 {filename} 时发生异常: {e}")

